"""
importar modulos
"""
from multiplo import multiplo_5, multiplo_7

while True:
    try:
        numero = int(input("Digite um número natural: "))
        while (numero < 1) or (numero > 999999):
            numero = int(input("Voce deve digitar entre 0 e 999999:  "))
    except Exception as e:
        print("Valor inválido:", e)
    else:
        break

if bool(multiplo_5(numero) & multiplo_7(numero)):
    print("fizzbuzz")
elif bool(multiplo_7(numero)):
    print("buzz")
elif bool(multiplo_5(numero)):
    print("fizz")
else:
    print("esse número não é multiplo de 5 e nem de 7")
