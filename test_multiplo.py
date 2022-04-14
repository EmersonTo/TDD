"""
importar modulos
"""
from multiplo import multiplo_5, multiplo_7


class TesteExercicio:
    """
    Classe para testar as funçoes de mutiplos 5 e 7
    """

    def test_multiplo5(self):
        """
        funçao teste multiplo5
        """
        resultado = multiplo_5(5)
        assert bool(resultado)

    def test_multiplo7(self):
        """
        funçao teste multiplo7
        """
        resultado = multiplo_7(7)
        assert bool(resultado)
