import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_7_ovi import kotus_noun_7_ovi

class TestInflectionType7(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_7_ovi("ovi")

        expected = InflectionInfo(nominative="ovi",
                                  nominative_plural="ovet",
                                  genitive="oven",
                                  genitives_plural=["ovien"],
                                  partitives=["ovea"],
                                  partitives_plural=["ovia"],
                                  accusatives=["ovi",
                                               "oven"],
                                  accusative_plural="ovet",
                                  inessive="ovessa",
                                  inessives_plural=["ovissa"],
                                  elative="ovesta",
                                  elatives_plural=["ovista"],
                                  illatives=["oveen"],
                                  illatives_plural=["oviin"],
                                  adessive="ovella",
                                  adessives_plural=["ovilla"],
                                  ablative="ovelta",
                                  ablatives_plural=["ovilta"],
                                  allative="ovelle",
                                  allatives_plural=["oville"],
                                  essives=["ovena"],
                                  essives_plural=["ovina"],
                                  translative="oveksi",
                                  translatives_plural=["oviksi"],
                                  abessive="ovetta",
                                  abessives_plural=["ovitta"],
                                  instructives_plural=["ovin"],
                                  comitatives_plural=["ovine"])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_7_ovi("arpi",
                                g.gradate_kotus_e_sopu_sovun)

        expected = InflectionInfo(nominative="arpi",
                                  nominative_plural="arvet",
                                  genitive="arven",
                                  genitives_plural=["arpien"],
                                  partitives=["arpea"],
                                  partitives_plural=["arpia"],
                                  accusatives=["arpi",
                                               "arven"],
                                  accusative_plural="arvet",
                                  inessive="arvessa",
                                  inessives_plural=["arvissa"],
                                  elative="arvesta",
                                  elatives_plural=["arvista"],
                                  illatives=["arpeen"],
                                  illatives_plural=["arpiin"],
                                  adessive="arvella",
                                  adessives_plural=["arvilla"],
                                  ablative="arvelta",
                                  ablatives_plural=["arvilta"],
                                  allative="arvelle",
                                  allatives_plural=["arville"],
                                  essives=["arpena"],
                                  essives_plural=["arpina"],
                                  translative="arveksi",
                                  translatives_plural=["arviksi"],
                                  abessive="arvetta",
                                  abessives_plural=["arvitta"],
                                  instructives_plural=["arvin"],
                                  comitatives_plural=["arpine"])

        ensure_inflections_equal(expected, data)


    def test_with_umlaut_gradation(self):
        data = kotus_noun_7_ovi("tähti",
                                g.gradate_kotus_f_satu_sadun)

        expected = InflectionInfo(nominative='tähti',
                                  nominative_plural='tähdet',
                                  genitive='tähden',
                                  genitives_plural=['tähtien'],
                                  partitives=['tähteä'],
                                  partitives_plural=['tähtiä'],
                                  accusatives=['tähti',
                                               'tähden'],
                                  accusative_plural='tähdet',
                                  inessive='tähdessä',
                                  inessives_plural=['tähdissä'],
                                  elative='tähdestä',
                                  elatives_plural=['tähdistä'],
                                  illatives=['tähteen'],
                                  illatives_plural=['tähtiin'],
                                  adessive='tähdellä',
                                  adessives_plural=['tähdillä'],
                                  ablative='tähdeltä',
                                  ablatives_plural=['tähdiltä'],
                                  allative='tähdelle',
                                  allatives_plural=['tähdille'],
                                  essives=['tähtenä'],
                                  essives_plural=['tähtinä'],
                                  translative='tähdeksi',
                                  translatives_plural=['tähdiksi'],
                                  abessive='tähdettä',
                                  abessives_plural=['tähdittä'],
                                  instructives_plural=['tähdin'],
                                  comitatives_plural=['tähtine'])

        ensure_inflections_equal(expected, data)

    # There are no singular words in this class that end in a consonant

    def test_toholampi_regression(self):
        data = kotus_noun_7_ovi("Toholampi", g.gradate_kotus_h_kumpi_kumman)
        ensure(data.abessive).equals("Toholammetta")
