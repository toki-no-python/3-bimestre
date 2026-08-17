idade = int(input("Qual a sua idade?"))
if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 50:
    print("CLT")
elif idade < 100:
    print("idoso")