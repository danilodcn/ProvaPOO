import datetime
from typing import List

class BatimentosCardiacos(object):
    def __init__(self, nome, sobrenome, dia, mes, ano):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @sobrenome.setter
    def sobrenome(self, value):
        self.__sobrenome = value

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        self.__dia = value
    
    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, value):
        self.__mes = value
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, value):
        self.__ano = value
    
    def __repr__(self):
        return f'<Object: {self.nome} {self.sobrenome}>'
    
    def calcula_idade(self) -> int:
        now = datetime.datetime.now()
        old = datetime.datetime(self.ano, self.mes, self.dia)
        
        difference = now - old
        duration = difference.total_seconds()

        anos, _ = divmod(duration, 60 * 60 * 24 * 365)

        # import ipdb; ipdb.set_trace()
        return int(anos)

    def frequencia_cardiaca_maxima(self) -> int:
        return 220 - self.calcula_idade()

    def frequencia_cardiaca_alvo(self) -> List[float]:
        maxima = self.frequencia_cardiaca_maxima()
        return [
            maxima * .5,
            maxima * .8
        ]

