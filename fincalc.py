# FinCalc - Sistema de Cálculos Financeiros em Python

def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcular o montante final obitido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_aposentadoria(patrimonio_atual: float,
                           aporte_mensal: float, anos: int, taxa_anual: float) -> float:
    """Calcular o patrimonio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
        return saldo


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcular o montante final obtido por juros compostos"""
    montante = capital * ((1 + (taxa_anual / 100) ** anos))
    return montante


def calcular_irrf(salario_bruto: float) -> float:
    """Calcular o imposto de renda retido na fonte (IRRF)."""
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


def calcular_depreciacao_linear(valor_inicial: float,
                                valor_residual: float,
                                vida_util_anos: int) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    return (valor_inicial - valor_residual) / vida_util_anos

    if __name__ == "__main__":
        print("Iniciando o sistema FinCalc...")
        parimmonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
        print(f"Patrimônio Estimado para Aposentadoria: R$ {parimmonio:.2f}")
        montante = calcular_juros_simples(1000.0, 5.0, 2)
        print(f"Juros Simples: R$ {montante:.2f}")
        montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
        print(f"Juros Compostos: R${montante_comp:.2f}")
        irrf_calculado = calcular_irrf(3000.0)
        print(f"IRRF Retido: R$ {irrf_calculado:.2f}")
        depreciacao = calcular_depreciacao_linear(100000.0, 20000.0, 5)
        print(f"Depreciação Anual: R$ {depreciacao:.2f}")
