from unittest import TestCase
from prova01.q03 import BatimentosCardiacos

class TesteQuestao03(TestCase):
    def test_calculo_da_idade(self):
        b = BatimentosCardiacos("Danilo", "da Conceição Nascimento", 7, 3, 1997)

        encontrado = b.calcula_idade()
        esperado = 24

        self.assertEqual(encontrado, esperado)