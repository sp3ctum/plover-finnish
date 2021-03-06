import sys
from create_dictionary import load_file_as_yaml, load_file_as_json
from toolz import functoolz
from toolz import itertoolz
import inflection.inflection_service as infl
from operator import concat
import math
import collections
from termcolor import cprint
from parsy import ParseError
from glob import glob
import os

sys.path.append("../../word-analyser/")
import word_analyser.tools as tools
import json

def inflected_forms(word):
    """Retuns all the inflected forms of the given word as a set, such as for the
    word vuoto;noun-valo-av1
    """
    try:

        inflection_forms = infl.inflected_forms(word)
        return inflection_forms
    except Exception as e:
        cprint("Error inflecting word %s: %s" % (word, e), "blue")
        return []

def flatten_dictify_matched(subprocess_data):
    def stroke_found(result):
        try:
            return None not in result
        except TypeError:
            pass

    found_strokes = {word_and_stroke[0]: word_and_stroke[1]
                     for words_and_strokes in subprocess_data
                     # each inflected form has its own stroke here
                     for inflections_and_strokes in words_and_strokes
                     for word_and_stroke in inflections_and_strokes
                     if stroke_found(word_and_stroke)}

    # Force the words to always be in the same order. Otherwise git diffs will
    # be inconsistent.
    return collections.OrderedDict(sorted(found_strokes.items()))

def write_to_yaml_file(target_file, strokes):
    return tools.save_results_into_file(strokes, target_file)

def write_to_json_file(target_file, strokes):
    with open(target_file, 'w') as json_file:
        json.dump(strokes, json_file, indent = 2, ensure_ascii=False)

def chunkify(n, sequence):
    length = len(sequence)
    chunk_length = math.floor(length / n)

    # From http://toolz.readthedocs.io/en/latest/api.html#toolz.itertoolz.partition_all
    #
    # Partition all elements of sequence into tuples of length at most n. The
    # final tuple may be shorter to accommodate extra elements.
    lazy_chunks = itertoolz.partition_all(chunk_length, sequence)
    return lazy_chunks

def combine(dictionaries):
    combined = {}
    for d in dictionaries:
        combined.update(d)
    return combined

def load_file(path):
    if ".json" in path:
        return load_file_as_json(path)
    elif ".yaml" in path:
        return load_file_as_yaml(path)

# python create_double_strokes.py  5453,43s user 7,19s system 550% cpu 16:31,25 total
def ignored_words(target_file, existing_files):
    if "QUICK" in os.environ:
        print("Environment variable QUICK has been set. Not collecting list of ignored words.")
        return set()

    def not_my_file(f):
        name = os.path.basename(f)
        print(name, os.path.basename(target_file))
        return name != os.path.basename(target_file)

    others = [f for f in existing_files if not_my_file(f)]
    d = combine(map(load_file, others))
    return set(d.keys())

def wordlist_chunks(cores, target_file_name):
    # To speed up generation of words, ignore all words that are present in the
    # already existing dictionaries
    ignore_words = ignored_words(target_file_name,
                                 glob("../input_dictionaries/*"))
    print("Ignoring %s already created words." % (len(ignore_words)))

    words_raw = tools.get_finnish_wordlist()

    print("Loaded {} Finnish language words and abbreviations.".format(len(words_raw)))

    # Let each core process an ~equal amount of work
    chunks = list(chunkify(n = cores, sequence = words_raw))
    print("Processing all words on {} cores with {} words per core".format(
        cores, len(chunks[0])))
    return (chunks, ignore_words)
