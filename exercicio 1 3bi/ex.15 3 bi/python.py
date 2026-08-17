numero1 = int(input("Me dê um numero: "))
numero2 = int(input("Agora o segundo: "))
numero3 = int(input("E o terceiro: "))
if numero1 > numero2 and numero1 > numero3:
    print(f"maior número: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"maior número: {numero2}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"maior número: {numero3}")