# ================================
# Quebrada FC Fans 🏪
# ================================

valor_compra = float(input("Digite o valor da compra (R$): "))
valor_pago = float(input("Digite o valor pago pelo cliente (R$): "))

if valor_pago < valor_compra:
    print("\n❌ Pagamento insuficiente!")
    print(f"Faltam R$ {valor_compra - valor_pago:.2f}")

else:
    troco = round(valor_pago - valor_compra, 2)

    print("\n==============================")
    print(f"Troco: R$ {troco:.2f}")
    print("==============================")

    troco_centavos = int(round(troco * 100))

    dinheiro = [
        ("Nota de R$100,00", 10000),
        ("Nota de R$50,00", 5000),
        ("Nota de R$20,00", 2000),
        ("Nota de R$10,00", 1000),
        ("Nota de R$5,00", 500),
        ("Nota de R$2,00", 200),
        ("Moeda de R$1,00", 100),
        ("Moeda de R$0,50", 50),
        ("Moeda de R$0,25", 25),
        ("Moeda de R$0,10", 10),
        ("Moeda de R$0,05", 5),
        ("Moeda de R$0,01", 1)
    ]

    total_notas = 0
    total_moedas = 0

    print("\nQuantidade de notas e moedas:")

    for nome, valor in dinheiro:
        quantidade = troco_centavos // valor

        if quantidade > 0:
            print(f"{nome}: {quantidade}")

            if "Nota" in nome:
                total_notas += quantidade
            else:
                total_moedas += quantidade
            troco_centavos %= valor

    print("\n==============================")
    print(f"Total de notas 💵 R$: {total_notas}")
    print(f"Total de moedas 🪙 R$: {total_moedas}")
    print(f"Total de itens devolvidos 💵 🟡 R$: {total_notas + total_moedas}")
    print("==============================")


    print("\n=======================================")
    print("Obrigado por ajudar o Quebrada FC")
    print("🎁")
    print("\n=======================================")