def calcular_irrf(salario_bruto: float) -> float:
  
  if salario_bruto <= 2259.20:
    return  0.0
  elif salario_bruto <= 2826.65:
    return (salario_bruto * 0.075) - 169.44
  elif salario_bruto <= 3751.05:
    return (salario_bruto * 0.15) - 381.44
  else: 
    return (salario_bruto * 0.225) - 662.77