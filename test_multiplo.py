import pytest

from multiplo import multiplo5, multiplo7

class TesteExercicio:
    def setup(self):
        pass

    def test_multiplo5(self):
        resultado = multiplo5(5)
        assert resultado == True

    def test_multiplo7(self):
        resultado = multiplo7(7)
        assert resultado == True
