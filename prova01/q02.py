from typing import List
from prova01.q01 import Pais


class NotEditable(Exception): ...


class Continente(object):

    def __init__(self, nome):
        self.__nome = nome
        self.__paises = set()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def paises(self):
        return self.__paises

    @paises.setter
    def paises(self, value):
        raise NotEditable("Esse objeto não pode ser alterado")

    def adicionar(self, *paises: Pais) -> None:
        # import ipdb; ipdb.set_trace()
        self.paises.update(set(paises))

    def dimensao(self) -> float:
        # import ipdb; ipdb.set_trace()
        return sum(map(lambda pais: pais.dimensao, self.paises))

    def populacao(self) -> int:
        return sum(map(lambda pais: pais.populacao, self.paises))

    def __ordena(self, key: str, descending: bool=False) -> List[Pais]:
        paises = sorted(
            self.paises,
            key=lambda pais: getattr(pais, key),
            reverse=descending
        )

        return paises

    def mais_populoso(self) -> Pais:
        # import ipdb; ipdb.set_trace()
        paises = self.__ordena('populacao', descending=True)
        return paises[0]

    def menos_populoso(self) -> Pais:
        # import ipdb; ipdb.set_trace()
        paises = self.__ordena('populacao', descending=False)
        return paises[0]

    def maior_pais(self) -> Pais:
        paises = self.__ordena('dimensao', descending=True)
        return paises[0]

    def menor_pais(self) -> Pais:
        paises = self.__ordena('dimensao', descending=False)
        return paises[0]

    def razao_territorial(self) -> float:
        paises_ordenados = self.__ordena('dimensao', descending=True)
        maior = paises_ordenados[0]
        menor = paises_ordenados[-1]

        return maior.dimensao / menor.dimensao


