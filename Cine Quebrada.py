import locale
from datetime import datetime

# Configura o idioma para português
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_TIME, '')

# Data do sistema
dia_semana = datetime.now().strftime('%A').lower()

# Preço do ingresso conforme o dia
if dia_semana in ["segunda-feira", "terça-feira", "quarta-feira"]:
    preco_ingresso = 10.00
else:
    preco_ingresso = 15.00

print("=" * 60)
print("🎥 CINE QUEBRADA")
print("=" * 60)
print("Hoje é:", dia_semana.capitalize())
print(f"Valor do ingresso hoje: R$ {preco_ingresso:.2f}")
print("=" * 60)

# FILMES
filmes = {
    "D039": ("O Poderoso Chefão", "Máfia"),
    "D040": ("Clube da Luta", "Drama"),
    "D041": ("A Origem", "Ficção Científica"),
    "D042": ("O Senhor dos Anéis", "Fantasia"),
    "D043": ("Vingadores", "Ação"),
    "D059": ("O Rei Leão", "Animação"),
    "D024": ("Velozes e Furiosos", "Ação")
}

print("FILMES DISPONÍVEIS")
print("=" * 60)

for cod, dados in filmes.items():
    print(f"{cod} - {dados[0]} ({dados[1]})")

print("=" * 60)

codigo_filme = input("Digite o código do filme: ").upper()

if codigo_filme not in filmes:
    print("Filme não encontrado!")
    exit()

quant_ingressos = int(input("Quantidade de ingressos: "))

while quant_ingressos < 1:
    quant_ingressos = int(input("Digite no mínimo 1 ingresso: "))

# COMBOS
combos = {
    "COMBO-005": ("Doritos + Refri Lata", 15.90),
    "COMBO-010": ("Pipoca + Refri Lata", 17.90),
    "COMBO-015": ("Pipoca Doce + Suco Natural", 20.90),
    "COMBO-020": ("Refil Pipoca + 2 Recargas", 25.90),
    "COMBO-001": ("Combo Família", 50.00),
    "COMBO-002": ("Combo Casal", 30.00),
    "COMBO-006": ("Combo Amigos", 40.00),
    "COMBO-034": ("Combo Doces", 35.00)
}

total_combos = 0
lista_combos = []

print("\nCOMBOS DISPONÍVEIS")
print("=" * 60)

for cod, dados in combos.items():
    print(f"{cod} - {dados[0]} - R$ {dados[1]:.2f}")

print("=" * 60)

# Compra de combos
while True:

    resposta = input("\nDeseja comprar algum combo? (S/N): ").upper()

    if resposta == "N":
        break

    elif resposta == "S":

        cod_combo = input("Digite o código do combo: ").upper()

        if cod_combo in combos:

            qtd = int(input("Quantidade: "))

            subtotal = combos[cod_combo][1] * qtd

            total_combos += subtotal

            lista_combos.append(
                (combos[cod_combo][0], qtd, subtotal)
            )

            print("✅ Combo adicionado!")

        else:
            print("❌ Código de combo inválido!")

    else:
        print("Digite apenas S ou N.")

# TOTAIS
total_ingressos = preco_ingresso * quant_ingressos
valor_total = total_ingressos + total_combos

# RESUMO
print("\n")
print("=" * 60)
print("RESUMO DA COMPRA")
print("=" * 60)

print(f"Filme: {filmes[codigo_filme][0]}")
print(f"Gênero: {filmes[codigo_filme][1]}")

print("\nIngressos")
print(f"Quantidade: {quant_ingressos}")
print(f"Subtotal: R$ {total_ingressos:.2f}")

print("\nCombos")

if len(lista_combos) == 0:
    print("Nenhum combo comprado.")

else:

    for combo in lista_combos:

        print("-" * 40)
        print(f"Combo: {combo[0]}")
        print(f"Quantidade: {combo[1]}")
        print(f"Subtotal: R$ {combo[2]:.2f}")

print("-" * 40)
print(f"Total Combos: R$ {total_combos:.2f}")
print("=" * 60)
print(f"TOTAL A PAGAR: R$ {valor_total:.2f}")
print("=" * 60)
print("Obrigado por comprar no Cine Quebrada!")
print("🍿 Aproveite o filme!")
print("=" * 60)