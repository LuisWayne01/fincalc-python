from fincalc import calcular_aposentadoria


def test_aposentadoria_padrao():
    # Arrange & Act
    resultado = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    # Assert
    assert resultado > 10000.0


def test_aposentadoria_sem_patrimonio_inicial():
    # Arrange & Act
    resultado = calcular_aposentadoria(0.0, 500.0, 10, 5.0)
    # Assert
    assert resultado > 0.0
