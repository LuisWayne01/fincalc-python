import pytest
from fincalc import calcular_roi


def test_roi_lucro_padrao():
    # Arrange & Act
    resultado = calcular_roi(ganho_total=1200.00, custo_total=1000.00)
    # Assert
    assert round(resultado, 2) == 20.00


def test_roi_sem_lucro_empate():
    # Arrange & Act
    resultado = calcular_roi(ganho_total=1000.00, custo_total=1000.00)
    # Assert
    assert round(resultado, 2) == 0.00


def test_roi_prejuizo():
    # Arrange & Act
    resultado = calcular_roi(ganho_total=800.00, custo_total=1000.00)
    # Assert
    assert round(resultado, 2) == -20.00


def test_roi_custo_zero_invalido():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_roi(ganho_total=500.00, custo_total=0.00)


def test_roi_custo_negativo_invalido():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_roi(ganho_total=600.00, custo_total=-500.00)
