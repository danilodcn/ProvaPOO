import unittest
from prova02 import models

class TestBancoDados(unittest.TestCase):
    def teste_inserir_dados_no_banco(self):
        models.create_tables()