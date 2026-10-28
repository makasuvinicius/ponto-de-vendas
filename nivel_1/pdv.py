print("========================================")
print("     SISTEMA DE CAIXA - LOJA")
print("========================================")


compras = []

while True:
    valor = float(input("Digite o valor da compra (0 para encerrar): R$ "))

    if valor == 0:
        break

    if valor < 0:
        print("Aviso: o valor da compra não pode ser negativo!")
        continue

    while True:
        idade = int(input("Digite a idade do cliente: "))

        if idade < 0:
            print("Aviso: a idade não pode ser negativa!")
        else:
            break

    valor_final = valor

    # Desconto por idade
    if idade >= 65:
        valor_final = valor_final * 0.8

    # Desconto extra por valor
    if valor_final > 100:
        valor_final = valor_final * 0.9

    desconto = valor - valor_final

    # Guardando os dados da compra
    compras.append([valor, idade, desconto, valor_final])

    print(f"Valor final da compra: R$ {valor_final:.2f}")
    print("----------------------------------")

# Resumo do dia
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in compras:
    total_bruto = total_bruto + compra[0]
    total_descontos = total_descontos + compra[2]
    total_final = total_final + compra[3]

print("\n========== RESUMO DO DIA ==========")
print(f"Quantidade de compras: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("===================================")