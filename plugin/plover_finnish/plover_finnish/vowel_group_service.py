from functools import partial

# vowel groups
aou = "aou"
äöy = "äöy"

def find(word, char):
    index = word.find(char)
    return index if index > 0 else None

def contains_char(word, character_candidates):
    matches = partial(find, word)
    return any(filter(matches, character_candidates))

def vowel_group(word):
    if contains_char(word, aou):
        return aou
    elif contains_char(word, äöy):
        return äöy

def switch_chars(word, a, b):
    # replaces all occurrences of the character a with the character b
    def replace(char):
        return b if char == a else char
    return "".join([replace(c) for c in word])

def switch_char_groups(word, group_a, group_b):
    for a, b in zip(group_a, group_b):
        word = switch_chars(word, a, b)
    return word

def switch_vowel_group(word):
    if vowel_group(word) == aou:
        return switch_char_groups(word, aou, äöy)
    elif vowel_group(word) == äöy:
        return switch_char_groups(word, äöy, aou)

    # group not recognized, cannot switch it
    return word
