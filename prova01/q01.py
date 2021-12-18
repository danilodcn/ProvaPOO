from uuid import uuid4 as uuid

class NotEditable(Exception):
    ...

class Pais:
    __todos_paises = set()

    def __init__(self, nome, populacao: int, dimensao: float):
        self.__nome = nome
        self.__dimensao = dimensao
        self.__population = populacao
        self.__codigo = uuid()
        self.__fronteira = set()

        Pais.__todos_paises.add(self)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__name = nome
    
    @property
    def populacao(self):
        return self.__population
    
    @populacao.setter
    def populacao(self, populacao: int):
        self.__population = populacao

    @property
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao: float):
        dimensao = dimensao

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo: float):
        raise NotEditable("Não é possível alterar o código do país")

    @property
    def fronteira(self):
        return self.__fronteira
    
    @fronteira.setter
    def fronteira(self, fronteira):
        raise NotEditable("Não é possível alterar o objeto")

    def __eq__(self, other):
        return self.codigo == other.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)

    object

    def __repr__(self):
        return f"<Pais (nome: {self.nome}, dimensao: {self.dimensao})>"

    def e_limitrofe(self, other):
        # import ipdb; ipdb.set_trace()
        assert isinstance(other, Pais)
        for pais in self.fronteira: 
            if other == pais:
                return True

        return False

    def add_fronteira(self, *others):
        for pais in others:
            assert isinstance(pais, Pais)
            self.fronteira.add(pais)
            pais.fronteira.add(self)

    def densidade(self):
        return self.populacao / self.dimensao

    def vizinhos_comuns(self, other):
        # import ipdb; ipdb.set_trace()
        assert isinstance(other, Pais)
        return self.fronteira.intersection(other.fronteira)

    def todos_paises(self):
        todos = Pais.__todos_paises
        # import ipdb; ipdb.set_trace()

        return sorted(todos, key=lambda pais: pais.nome, reverse=False)

    def clear(self):
        """
        limpa todos os os países criados até então
        """
        Pais.__todos_paises = set()