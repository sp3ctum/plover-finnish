import unittest
from ensure import ensure
from . import gradation as g
from .gradation import gradation_function
from .lookup import lookup_verb

def ensure_gives(args, result):
    # It's super hard to read the tests when they get too long. I made this to
    # make it a bit more bearable.
    ensure(lookup_verb(*args)
           .moduses().potential_present().passive).equals(result)

class TestLookup(unittest.TestCase):
    def test_verbs(self):
        # go through each case and make sure gradation works
        ensure_gives(("sanoa",      "punoa"             ), "sanottaneen"     )
        ensure_gives(("aallottaa",  "aavistaa",   "av1" ), "aallotettaneen"  )
        ensure_gives(("uuttaa",     "heittää",    "av1" ), "uutettaneen"     )
        ensure_gives(("väistää",    "muistaa"           ), "väistettäneen"   )
        ensure_gives(("riittää",    "inttää",     "av1" ), "riitettäneen"    )
        ensure_gives(("hiostuttaa", "sulaa",      "av1" ), "hiostutettaneen" )
        ensure_gives(("hoitaa",     "hohtaa",     "av1" ), "hoidettaneen"    )
        ensure_gives(("heilahtaa",  "hujahtaa",   "av1" ), "heilahdettaneen" )
        ensure_gives(("ansoittaa",  "kirjoittaa", "av1" ), "ansoitettaneen"  )
        ensure_gives(("ostaa",      "loistaa"           ), "ostettaneen"     )
        ensure_gives(("huoltaa",    "vuotaa",     "av1" ), "huollettaneen"   )