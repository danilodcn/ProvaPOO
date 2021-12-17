from uuid import uuid4 as uuid

class NotEditable(Exception):
    ...

class Pais:
    todos_paises = set()

    def __init__(self, name, population: int, dimension: float):
        self.__name = name
        self.__dimension = dimension
        self.__population = population
        self.__code = uuid()
        self.__fronteira = set()

        Pais.todos_paises.add(self)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
    
    @property
    def population(self):
        return self.__population
    
    @population.setter
    def population(self, population: int):
        self.__population = population

    @property
    def dimension(self):
        return self.__dimension
    
    @dimension.setter
    def dimension(self, dimension: float):
        dimension = dimension

    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self, code: float):
        raise NotEditable("Não é possível alterar o código do país")

    @property
    def fronteira(self):
        return self.__fronteira
    
    @fronteira.setter
    def fronteira(self, fronteira):
        raise NotEditable("Não é possível alterar o objeto")

    def __eq__(self, other):
        return self.__code == other.code

    def __hash__(self) -> int:
        return hash(self.code)

    def __repr__(self):
        return f"<Pais (nome: {self.name}, dimension: {self.dimension})>"

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
        return self.population / self.dimension

    def vizinhos_comuns(self, other):
        # import ipdb; ipdb.set_trace()
        assert isinstance(other, Pais)
        return self.fronteira.intersection(other.fronteira)

