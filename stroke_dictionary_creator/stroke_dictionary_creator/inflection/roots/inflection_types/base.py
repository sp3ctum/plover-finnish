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
    rest = yield character.at_least(1).concat()
    return [rest, end_vowel]

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
