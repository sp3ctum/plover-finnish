from parsy import *

# root words are simpler to parse in reverse order
def reverse(s): return s[::-1]

def reverse_parse(word, p):
    return_value = p.parse(reverse(word))
    if len(return_value) == 2:
        (root, data) = return_value
        return (reverse(root), data)

    if len(return_value) == 3:
        (root, data, d2) = return_value
        return (reverse(root), data, d2)

    if len(return_value) == 4:
        (root, data, d2, d3) = return_value
        return (reverse(root), data, d2, d3)

    if len(return_value) == 5:
        (root, data, d2, d3, d4) = return_value
        return (reverse(root), data, d2, d3, d4)

    return reverse(return_value)
