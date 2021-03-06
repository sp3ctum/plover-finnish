from parsy import *

def join(char_list):
    return "".join([c for c in char_list if c is not None])

def steno_sequence(charmap):
    # Returns a parser that parses steno keys in the order that is given in charmap.
    # Disallows characters that are:
    # - not present in the given charmap
    # - given in the reverse (steno) order defined in charmap
    # If nothing matches, raises a ParseError like most parsers by default.

    @generate("steno sequence")
    def steno_sequence_parser():
        # Create successive and optional parsers for each successive steno key.
        # Then join their results into one string.
        char_sequence_parsers = [(string(c) | success("")) for c in charmap]
        chars = yield seq(*char_sequence_parsers).map(join)

        return chars if chars != "" else fail("middle key must exist or be -")

    return steno_sequence_parser

initial_consonants  = steno_sequence("STKPVHR") | success("")
middle_keys         = string("-") | steno_sequence("AO*EI")
end_keys            = steno_sequence("NKSHTReoia") | success("")

stroke = seq(initial_consonants,
             middle_keys,
             end_keys).map(join)
