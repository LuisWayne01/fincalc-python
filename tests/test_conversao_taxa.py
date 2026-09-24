import pytest
from fincalc import converter_taxa_anual_para_mensal


def test_conversao_taxa_positiva():
    taxa_m = converter_taxa_anual_para_mensal(12.6825)
    assert round(taxa_m, 4) == 1.0000


def test_conversao_taxa_nula():
    taxa_m = converter_taxa_anual_para_mensal(0.0)
    assert round(taxa_m, 4) == 0.0


def test_conversao_taxa_abaixo_menos_cem():
    with pytest.raises(ValueError):
        converter_taxa_anual_para_mensal(-150.0)
