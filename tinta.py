
lado1 = float(input("Informe a largura da area a ser pintada em metros: "))
lado2 = float(input("Informe o comprimento da area a ser pintada em metros: "))

area = lado1 * lado2


litros = area / 2


custo = litros * 14.00


print(f"Area:          {area:10.2f} m²")
print(f"Qtd de litros: {litros:10.2f} litros")
print(f"Custo:       R${custo:10.2f}")