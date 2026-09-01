# FinCalc - Sistema de Cálculos Financeiros em Python

def calcular_juros_simples(capital:float, taxa_anual: float, anos: int) -> float:
    """Calcular o montante final obitido por juros simples."""
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros

def calcular_aposentadoria(patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float) -> float:
    """Calcular o patrimonio acumulado para aposentadoria."""
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
        return saldo


    if __name__ == "__main__":
        print("Iniciando o sistema FinCalc...")
        parimmonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
        print(f"Patrimônio Estimado para Aposentadoria: R$ {parimmonio:.2f}")S