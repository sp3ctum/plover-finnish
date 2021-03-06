"""Mapping of joukahainen inflection types to those used in kotus."""

from collections import namedtuple
from typing import Dict

from .inflection_types import adjectives as a
from . import gradation as g
from . import inflection_types as i

from .inflection_types.verbs import *

NominalInflection = namedtuple("NominalInflection",
                               ["inflection_fn", "gradation_fn"])
AdjectiveInflection = namedtuple("AdjectiveInflection",
                                 ["inflection_fn", "gradation_fn"])
Conjugation = namedtuple("Conjugation",
                         ["verb_class", "gradation_fn"])

def infl(module, gradation_fn = None) -> NominalInflection:
    "Shorthand for the readability of inflection definitions"
    # The function name is the same as the module name. Let's resolve it so the
    # file is a bit easier to read.
    #
    # sample:
    # stroke_dictionary_creator.inflection.roots.inflection_types.kotus_noun_2_palvelu

    fn_name = module.__name__.split(".")[-1]
    fn      = getattr(module, fn_name)

    return NominalInflection(inflection_fn = fn,
                             gradation_fn = gradation_fn)

def adj(refword: str, gradation_fn = None) -> AdjectiveInflection:
    fn_name    = "joukahainen_adjective_" + refword
    module     = getattr(a, fn_name)
    fn         = getattr(module, fn_name)

    return AdjectiveInflection(inflection_fn = fn,
                               gradation_fn = gradation_fn)

def conj(verb_class, gradation_fn = None) -> Conjugation:
    return Conjugation(verb_class = verb_class,
                       gradation_fn = gradation_fn)

nominals: Dict[str, NominalInflection] = {
    "valo":      infl(i.kotus_noun_1_valo),
    "arvelu":    infl(i.kotus_noun_2_palvelu),
    "autio":     infl(i.kotus_noun_3_valtio),
    "kiiski":    infl(i.kotus_noun_7_ovi),
    "siisti":    infl(i.kotus_noun_5_risti),
    "risti":     infl(i.kotus_noun_5_risti),
    "paperi":    infl(i.kotus_noun_6_paperi),
    "edam":      infl(i.kotus_noun_6_paperi),
    "kalsium":   infl(i.kotus_noun_5_risti),
    "lovi":      infl(i.kotus_noun_7_ovi),
    "toholampi": infl(i.kotus_noun_7_ovi, g.gradate_kotus_h_kumpi_kumman),
    "suksi":     infl(i.kotus_noun_7_ovi),
    "veli":      infl(i.kotus_noun_7_ovi),
    "nalle":     infl(i.kotus_noun_8_nalle),
    "kala":      infl(i.kotus_noun_9_kala),
    "nahka":     infl(i.kotus_noun_9_kala, g.gradate_kotus_d_reikä_reiän),
    "jumala":    infl(i.kotus_noun_10_koira),
    "koira":     infl(i.kotus_noun_10_koira),
    "ylkä":      infl(i.kotus_noun_10_koira, g.gradate_kotus_l_arki_arjen),
    "pitkä":     infl(i.kotus_noun_10_koira),
    "ruoka":     infl(i.kotus_noun_10_koira, g.gradate_kotus_d_reikä_reiän),
    "poika":     infl(i.joukahainen_noun_10_poika),
    "matala":    infl(i.kotus_noun_10_koira),
    "asema":     infl(i.kotus_noun_10_koira),
    "kulkija":   infl(i.kotus_noun_12_kulkija),
    "video":     infl(i.kotus_noun_3_valtio),
    "karahka":   infl(i.kotus_noun_13_katiska),
    "apaja":     infl(i.kotus_noun_11_omena),
    "peruna":    infl(i.kotus_noun_11_omena),
    "korkea":    infl(i.kotus_noun_15_korkea),
    "suurempi":  infl(i.kotus_noun_16_vanhempi, g.gradate_kotus_h_kumpi_kumman),
    "vapaa":     infl(i.kotus_noun_17_vapaa),
    "kamee":     infl(i.kotus_noun_20_filee),
    "pii":       infl(i.kotus_noun_18_maa),
    "suo":       infl(i.kotus_noun_19_suo),
    "askel":     infl(i.kotus_noun_32_sisar),
    "rosé":      infl(i.kotus_noun_21_rosé),
    "spray":     infl(i.kotus_noun_21_rosé),
    "parfait":   infl(i.kotus_noun_22_parfait),
    "huuli":     infl(i.kotus_noun_24_uni),
    "meri":      infl(i.kotus_noun_24_uni),
    "tuohi":     infl(i.kotus_noun_23_lohi),
    "niemi":     infl(i.kotus_noun_25_toimi),
    "pieni":     infl(i.kotus_noun_26_pieni),
    "lumi":      infl(i.kotus_noun_25_toimi),
    "susi":      infl(i.kotus_noun_27_käsi),
    "tosi":      infl(i.kotus_noun_27_käsi),
    "kansi":     infl(i.kotus_noun_28_kynsi),
    "sisar":     infl(i.kotus_noun_32_sisar),
    "hapan":     infl(i.kotus_noun_33_kytkin, g.gradate_kotus_b_kaappi_kaapin),
    "uistin":    infl(i.kotus_noun_33_kytkin),
    "laidun":    infl(i.kotus_noun_33_kytkin, g.gradate_kotus_f_keidas_keitaan),
    "onneton":   infl(i.kotus_noun_34_onneton, g.gradate_kotus_c_kate_katteen),
    "lämmin":    infl(i.kotus_noun_35_lämmin, g.gradate_kotus_h_lumme_lumpeen),
    "vasen":     infl(i.kotus_noun_37_vasen),
    "sisin":     infl(i.kotus_noun_36_sisin),
    "nainen":    infl(i.kotus_noun_38_nainen),
    "vastaus":   infl(i.kotus_noun_39_vastaus),
    "kalleus":   infl(i.kotus_noun_40_kalleus),
    "kaunis":    infl(i.kotus_noun_41_vieras),
    "autuas":    infl(i.kotus_noun_41_vieras),
    "laupias":   infl(i.kotus_noun_41_vieras),
    "vieras":    infl(i.kotus_noun_41_vieras),
    "iäkäs":     infl(i.kotus_noun_41_vieras, g.gradate_kotus_a_hake_hakkeen),
    "ohut":      infl(i.kotus_noun_43_ohut),
    "kevät":     infl(i.kotus_noun_44_kevät),
    "mies":      infl(i.kotus_noun_42_mies),
    "kuollut":   infl(i.kotus_noun_47_kuollut),
    "hame":      infl(i.kotus_noun_48_hame),

    # TODO only has the plural form!
    # "alkeet",

    "tie":       infl(i.kotus_noun_19_suo),
    "lapsi":     infl(i.kotus_noun_7_ovi),
    "hapsi":     infl(i.kotus_noun_7_ovi), # TODO can also be 29 when poetic,
    "loppu":     infl(i.kotus_noun_1_valo, g.gradate_kotus_b_kaappi_kaapin),
    "veitsi":    infl(i.kotus_noun_30_veitsi),
}

adjectives: Dict[str, AdjectiveInflection] = {
    # TODO what to do about these?
    # "None":    infl(i.kotus_noun_1_valo),

    # this contains only the word "lähteisyys", which is not an adjective!
    # "kalleus":   adj("kalleus"),

    # "poikkeava": adj("poikkeava"),

    "arvelu":    adj("arvelu"),
    "asema":     adj("asema"),
    "autio":     adj("autio"),
    "hame":      adj("hame"),
    "iäkäs":     adj("iäkäs"),
    "kala":      adj("kala"),
    "kalsium":   adj("kalsium"),
    "karahka":   adj("karahka"),
    "kaunis":    adj("kaunis"),
    "koira":     adj("koira"),
    "korkea":    adj("korkea"),
    "kulkija":   adj("kulkija"),
    "kuollut":   adj("kuollut"),
    "laupias":   adj("laupias"),
    "loppu":     adj("loppu"),
    "matala":    adj("matala"),
    "nainen":    adj("nainen"),
    "nalle":     adj("nalle"),
    "ohut":      adj("ohut"),
    "onneton":   adj("onneton"),
    "paperi":    adj("paperi"),
    "pieni":     adj("pieni"),
    "pii":       adj("pii"),
    "risti":     adj("risti"),
    "siisti":    adj("siisti"),
    "sisin":     adj("sisin"),
    "susi":      adj("susi"),
    "suurempi":  adj("suurempi"),
    "tosi":      adj("tosi"),
    "uistin":    adj("uistin"),
    "valo":      adj("valo"),
    "vapaa":     adj("vapaa"),
    "vastaus":   adj("vastaus"),
    "vieras":    adj("vieras"),
}

verbs: Dict[str, Conjugation] = {
    "punoa":      conj(KotusVerb52Sanoa),
    "aavistaa":   conj(KotusVerb53Muistaa),
    "hidastaa":   conj(KotusVerb53Muistaa),
    "heittää":    conj(KotusVerb53Muistaa, g.gradate_kotus_c_tyttö_tytön),
    "muistaa":    conj(KotusVerb53Muistaa),
    "inttää":     conj(KotusVerb53Muistaa),
    "sulaa":      conj(KotusVerb53Muistaa),
    "hohtaa":     conj(KotusVerb53Muistaa, g.gradate_kotus_f_satu_sadun),
    "hujahtaa":   conj(KotusVerb53Muistaa, g.gradate_kotus_f_satu_sadun),
    "kirjoittaa": conj(KotusVerb53Muistaa, g.gradate_kotus_c_tyttö_tytön),
    "loistaa":    conj(KotusVerb53Muistaa),
    "vuotaa":     conj(KotusVerb55Soutaa, g.gradate_kotus_f_satu_sadun),
    "huutaa":     conj(KotusVerb54Huutaa, g.gradate_kotus_f_satu_sadun),
    "sukeltaa":   conj(KotusVerb54Huutaa, g.gradate_kotus_i_ilta_illan),
    "paleltaa":   conj(KotusVerb54Huutaa, g.gradate_kotus_i_ilta_illan),
    "murtaa":     conj(KotusVerb54Huutaa, g.gradate_kotus_k_virta_virran),
    "juontaa":    conj(KotusVerb54Huutaa, g.gradate_kotus_j_hento_hennon),
    "pahentaa":   conj(KotusVerb54Huutaa, g.gradate_kotus_j_hento_hennon),
    "kaivaa":     conj(KotusVerb56Laulaa),
    "soutaa":     conj(KotusVerb55Soutaa),
    "saartaa":    conj(KotusVerb57Saartaa),
    "laskea":     conj(KotusVerb58Laskea),
    "tuntea":     conj(KotusVerb59Tuntea, g.gradate_kotus_j_hento_hennon),
    "lähteä":     conj(KotusVerb60Lähteä, g.gradate_kotus_f_satu_sadun),
    "sallia":     conj(KotusVerb61Sallia),
    "voida":      conj(KotusVerb62Voida),
    "käydä":      conj(KotusVerb65Käydä),
    "kanavoida":  conj(KotusVerb62Voida),
    "saada":      conj(KotusVerb63Saada),
    "juoda":      conj(KotusVerb64Juoda),
    "nuolaista":  conj(KotusVerb66Rohkaista),
    "mennä":      conj(KotusVerb67Tulla),
    "purra":      conj(KotusVerb67Tulla),
    "katsella":   conj(KotusVerb67Tulla),
    "haravoida":  conj(KotusVerb68Tupakoida),
    "valita":     conj(KotusVerb69Valita),
    "saneerata":  conj(KotusVerb73Salata),
    "aleta":      conj(KotusVerb72Vanheta),
    "haluta":     conj(KotusVerb75Selvitä),
    "juoruta":    conj(KotusVerb74Katketa),
    "salata":     conj(KotusVerb73Salata),
    "katketa":    conj(KotusVerb74Katketa),
    "kohota":     conj(KotusVerb74Katketa),
    "kihistä":    conj(KotusVerb66Rohkaista),
    "kitistä":    conj(KotusVerb66Rohkaista),
    "taitaa":     conj(KotusVerb76Taitaa),
    "juosta":     conj(KotusVerb70Juosta),
    "nähdä":      conj(KotusVerb71Nähdä),
    "kevetä":     conj(KotusVerb72Vanheta, g.gradate_kotus_e_sopu_sovun)
    # TODO irregular (78), see:
    # https://fi.wiktionary.org/wiki/Liite:Verbitaivutus/suomi/kaikaa
    # "kaikaa",
}
