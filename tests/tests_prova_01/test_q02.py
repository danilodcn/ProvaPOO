import random
from unittest import TestCase
from prova01.q01 import Pais, NotEditable
from prova01.q02 import Continente


class TesteQuestao02(TestCase):
    def setUp(self) -> None:
        self.nomes = ["Brasil", "Argentina", "Uruguai", "Paraguay", "EUA", "Equador"]
        self.populacoes = [random.randint(2000, 100000) for _ in self.nomes]
        self.dimensoes = [random.uniform(200000, 10000000) for _ in self.nomes]

        self.paises = {
            Pais(nome, pop, dimensao) for nome, pop, dimensao in zip(
                self.nomes,
                self.populacoes,
                self.dimensoes
            )
        }


    def test_adiciona_paises(self) -> None:
        america = Continente('America')
        america.adicionar(*self.paises)

        self.assertEqual(america.paises, self.paises)

    def teste_calcula_dimensao_total_continente(self) -> None:
        america = Continente('America')
        america.adicionar(*self.paises)

        esperado = sum(self.dimensoes)

        dimensao = america.dimensao()
        self.assertAlmostEqual(dimensao, esperado, places=5)

    def teste_calcula_populacao_total_continente(self) -> None:
        america = Continente('America')
        america.adicionar(*self.paises)

        esperado = sum(self.populacoes)

        populacao = america.populacao()
        self.assertAlmostEqual(populacao, esperado, places=5)
    
    def teste_retorna_pais_mais_populoso(self):
        america = Continente('America')
        america.adicionar(*self.paises)

        esperado = max(self.populacoes)

        encontrado = america.mais_populoso()

        self.assertEqual(esperado, encontrado.populacao)

    def teste_retorna_pais_menos_populoso(self):
        america = Continente('America')
        america.adicionar(*self.paises)

        esperado = min(self.populacoes)

        encontrado = america.menos_populoso()

        self.assertEqual(esperado, encontrado.populacao)

    def teste_retorna_maior_pais(self):
        america = Continente('America')
        america.adicionar(*self.paises)

        esperado = max(self.dimensoes)

        encontrado = america.maior_pais()

        self.assertEqual(esperado, encontrado.dimensao)

    def teste_retorna_menor_pais(self):
        america = Continente('America')
        america.adicionar(*self.paises)

        esperado = min(self.dimensoes)

        encontrado = america.menor_pais()

        self.assertEqual(esperado, encontrado.dimensao)

    def teste_calculo_razao_terriorial(self):
        america = Continente('America')
        america.adicionar(*self.paises)

        maior = max(self.dimensoes)
        menor = min(self.dimensoes)
        esperado = maior / menor

        encontrado = america.razao_territorial()

        self.assertEqual(esperado, encontrado)