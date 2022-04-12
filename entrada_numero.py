from multiplo import multiplo5, multiplo7

while True:
    try:
        numero = int(input("Digite um número natural: "))
        while (numero < 1) or (numero > 999999):
            numero = int(input("Voce deve digitar entre 0 e 999999:  "))
    except Exception as e:
         print("Valor inválido:", e)
    else:
        break

if multiplo5(numero) & multiplo7(numero) == True:
    print("fizzbuzz")
elif multiplo7(numero) == True:
    print("buzz")
elif multiplo5(numero) == True:
    print("fizz")
else:
    print("esse número não é multiplo de 5 e nem de 7")
