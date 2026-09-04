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


def calcular_parcela_price(valor_emprestimo: float,
                           taxa_mensal: float, meses: int) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    i = taxa_mensal / 100
    parcela = valor_emprestimo * (i * ((1 + i) ** meses)) / (((1 + i) ** meses) - 1)
    return parcela


def calcular_valor_futuro(aporte_mensal: float,
                          taxa_mensal: float, meses: int) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    i = taxa_mensal / 100
    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


def converter_taxa_anual_para_mensal(taxa_anual: float) -> float:
    """Converte uma taxa de juros anual equivalente para taxa mensal."""
    taxa_decimal = taxa_anual / 100
    taxa_mensal = ((1 + taxa_decimal) ** (1 / 12)) - 1
    return taxa_mensal * 100

def calcular_margem_liquida(receita_total: float, custos_totais: float) -> float:
    """Calcula a margem de lucro líquida percentual de uma operação."""
    lucro = receita_total - custos_totais
    return (lucro / receita_total) * 100

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
    parcela_price = calcular_parcela_price(100000.0, 1.5, 360)
    print(f"Parcela Tabela Price: R$ {parcela_price:.2f}")
    valor_futuro = calcular_valor_futuro(500.0, 1.0, 120)
    print(f"Valor Futuro Acumulado: R$ {valor_futuro:.2f}")
    depreciacao = calcular_depreciacao_linear(100000.0, 20000.0, 5)
    print(f"Depreciação Anual: R$ {depreciacao:.2f}")
    taxa_anual = 12.0
    taxa_mensal = converter_taxa_anual_para_mensal(taxa_anual)
    print(f"Taxa anual: {taxa_anual:.2f}%")
    print(f"Taxa mensal equivalente: {taxa_mensal:.4f}%")
    receita = 50000.0
    custos = 32000.0
    margem = calcular_margem_liquida(receita, custos)
    print(f"Margem Líquida: {margem:.2f}%")