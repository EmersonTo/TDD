"""
Funções para veficar multiplos.
"""


def multiplo_5(numero):
    """
    Função verifca se um número é multiplo de 5.
    """
    resto = numero % 5
    return bool(resto == 0)


def multiplo_7(numero):
    """
     Função verifca se um número é multiplo de 7.
    """
    resto = numero % 7
    return bool(resto == 0)
