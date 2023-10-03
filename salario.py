salario = float(input("Digite o valor do salário por hora: "))
horas = int(input("Digite o número de horas trabalhadas no mês: "))


salariob = salario * horas


inss = salariob * 0.11
irrf = (salariob - inss) * 0.27
sindicato = salariob * 0.05


salariol = salariob - inss - irrf - sindicato


print(f"+ Salário Bruto:   R$ {salariob:10.2f}")
print(f"- INSS (11%):      R$ {inss:10.2f}")
print(f"- IRRF (27%):      R$ {irrf:10.2f}")
print(f"- Sindicato (5%):  R$ {sindicato:10.2f}")
print(f"= Salário Líquido: R$ {salariol:10.2f}")