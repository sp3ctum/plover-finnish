from .base import *
from .kotus_noun_17_vapaa import kotus_noun_17_vapaa

def kotus_noun_18_maa(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in a double vowel
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    reference = kotus_noun_17_vapaa(word, gradation_fn)
    return reference._replace(illative = root + v + s("han"),
                              illatives_plural = [root + s("ihin")])