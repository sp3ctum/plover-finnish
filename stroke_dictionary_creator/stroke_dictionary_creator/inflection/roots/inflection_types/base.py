from parsy import *
from ..tokens import *
from ..noun_inflection_info import InflectionInfo
from ..gradation import identity
from ..parse_utils import reverse_parse

sys.path.append("../../../../plugin/plover_finnish/")
from plover_finnish.vowel_group_service import change_to_same_vowel_group, change_to_same_vowel_group_prefer_umlauts

@generate
def root_and_end_vowel():
    end_vowel = yield vowel
    rest      = yield character.at_least(1).concat()
    return [rest, end_vowel]

@generate
def root_and_vowel_vowel_ending():
    last_vowel           = yield vowel
    second_to_last_vowel = yield vowel
    root                 = yield character.at_least(1).concat()
    return [root, second_to_last_vowel, last_vowel]

@generate
def root_and_ccv_ending():
    # for the word "kynsi"

    last_vowel               = yield vowel
    second_to_last_consonant = yield consonant
    last_consonant           = yield consonant
    root                     = yield character.at_least(1).concat()

    return [root,
            last_consonant,
            second_to_last_consonant,
            last_vowel]

@generate
def root_and_ccvv_ending():
    # for the word "tuntea"

    last_vowel               = yield vowel
    second_to_last_vowel     = yield vowel
    second_to_last_consonant = yield consonant
    last_consonant           = yield consonant
    root                     = yield character.at_least(1).concat()

    return [root,
            last_consonant,
            second_to_last_consonant,
            second_to_last_vowel,
            last_vowel]


@generate
def root_and_double_end_vowel():
    end_vowel = yield vowel
    yield vowel
    root = yield character.at_least(1).concat()
    return [root, end_vowel]

@generate
def root_and_cv_ending():
    # a word like toimi

    end_vowel = yield vowel
    end_consonant = yield consonant
    root = yield character.at_least(1).concat()
    return [root, end_consonant, end_vowel]

@generate
def root_and_vc_ending():
    # a word like ien
    end_consonant = yield consonant
    end_vowel     = yield vowel
    root          = yield character.at_least(1).concat()
    return [root, end_vowel, end_consonant]

@generate
def root_and_cvc_ending():
    # a word like jumalatar
    end_consonant            = yield consonant
    v                        = yield vowel
    second_to_last_consonant = yield consonant
    root                     = yield character.at_least(1).concat()
    return [root, second_to_last_consonant, v, end_consonant]

@generate
def root_and_cvv_ending():
    # a word like esittää, returns the root as "esit"

    end_vowel = yield vowel
    yield vowel
    end_consonant = yield consonant
    root = yield character.at_least(1).concat()
    return [root, end_consonant, end_vowel]

@generate
def optional_consonant_double_vowel():
    start_consonant = yield consonant.optional()
    middle_vowel = yield vowel
    end_vowel = yield vowel
    return [start_consonant, middle_vowel, end_vowel]

def root_and_optional_end_vowel(fallback_vowel):
    @generate
    def parser():
        end_vowel = yield vowel.optional()
        end_vowel = end_vowel if end_vowel is not None else fallback_vowel
        rest = yield character.at_least(1).concat()
        return [rest, end_vowel]
    return parser

@generate
def root_and_Xvc_ending():
    # a word like avoin, paahdin
    end_consonant = yield consonant
    v             = yield vowel
    x             = yield character
    root          = yield character.at_least(1).concat()
    return [root, x, v, end_consonant]
