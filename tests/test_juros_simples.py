import pytest
from fincalc import calcular_juros_simples


def test_juros_simples_padrao():
    # Arrange & Act
    resultado = calcular_juros_simples(1000.0, 5.0, 2)
    # Assert
    assert abs(resultado - 1100.0) < 1e-2


def test_juros_simples_taxa_zero():
    # Arrange & Act
    resultado = calcular_juros_simples(1000.0, 0.0, 5)
    # Assert
    assert resultado == 1000.0
