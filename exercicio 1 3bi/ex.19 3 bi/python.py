produto = int(input("Qual o preço do produto: "))
desconto = 5
if produto < 100:
    print("Sem desconto.")
elif produto > 100:
     valor_desconto = produto * desconto / 100
     print(f"Aqui o desconto aplicado: {valor_desconto}")