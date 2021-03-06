from .base import *
from .kotus_noun_5_risti import kotus_noun_5_risti

def kotus_noun_6_paperi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("i"))

    inflections = kotus_noun_5_risti(word, gradation_fn)
    return inflections._replace(genitives_plural    = [root + s("ien"),
                                                       root + s("eiden"),
                                                       root + s("eitten")],
                                partitives          = [root + end_vowel + s("a")],
                                partitives_plural   = [root + s("eita"),
                                                       root + s("eja")],
                                inessives_plural    = [root + s("eissa")],
                                elatives_plural     = [root + s("eista")],
                                illatives           = [root + end_vowel + end_vowel + s("n")],
                                illatives_plural    = [root + s("eihin")],
                                adessives_plural    = [root + s("eilla")],
                                ablatives_plural    = [root + s("eilta")],
                                allatives_plural    = [root + s("eille")],
                                essives_plural      = [root + s("eina")],
                                translatives_plural = [root + s("eiksi")],
                                abessives_plural    = [root + s("eitta")],
                                instructives_plural = [root + s("ein")],
                                comitatives_plural  = [root + s("eine")])
    return inflections
