from re import S
import sys

from menu import Menu
from q03 import BatimentosCardiacos

class Main:
    def __init__(self):
        self.logado = False

        escape = {}
        self.opcoes_sem_conta = {
            'Criar usuário': self.__cria_usuario,
        }

        self.opcoes_logado = {
            "mudar nome": self.__mudar_nome,
            "mudar data de nascimento": self.__mudar_data_nascimento,
            "calcular idade": self.__calcular_idade,
            "frequencia cardiaca máxima": self.__frequencia_cardiaca_maxima,
            "frequencia cardiaca alvo": self.__frequencia_cardiaca_alvo,
            "logout": self.__logout,
        }
        
        self.relogou = True
        self.menu = Menu()
    
    def main_loop(self):
        while True:
            if self.logado:
                if self.relogou:
                    self.menu.opcoes = list(self.opcoes_logado.keys())
                
                resposta = self.menu.mostrar_menu()
                self.opcoes_logado[resposta]()

            else:
                if self.relogou:
                    self.menu.opcoes = list(self.opcoes_sem_conta.keys())

                resposta = self.menu.mostrar_menu()
                # import ipdb; ipdb.set_trace()
                self.opcoes_sem_conta[resposta]()
    
    def __cria_usuario(self, qtd=3):
        self.menu.print("Insira os dados do usuário:")
        nome = self.menu.input("Insira o Nome")
        sobrenome = self.menu.input("Insira o Sobrenome")
        self.menu.print("Agora vamos a sua data de nascimento")
        dia = self.menu.input("Informe o dia", type=int)
        mes = self.menu.input("Qual o mes?", type=int)
        ano = self.menu.input("e o ano?", type=int)
        for i in range(qtd):
            try:
                self.batimentos = BatimentosCardiacos(
                    nome=nome,
                    sobrenome=sobrenome,
                    dia=int(dia),
                    mes=int(mes),
                    ano=int(ano)
                )

                self.logado = True
            except KeyboardInterrupt:
                exit()
            except:
                self.menu.print(msg="Parece que seus dados nao estão corretos")
                self.menu.print(bold="Vamos tentar novamente")
                self.__cria_usuario(1)
    
    def __mudar_nome(self):
        self.menu.print("Atualização cadastral")
        nome = self.menu.input("Insira o Nome")
        sobrenome = self.menu.input("Insira o Sobrenome")

        self.batimentos.nome = nome
        self.batimentos.sobrenome = sobrenome
    
    def __mudar_data_nascimento(self):
        self.menu.print("Atualização cadastral")
        dia = self.menu.input("Informe o dia", type=int)
        mes = self.menu.input("Qual o mes?", type=int)
        ano = self.menu.input("e o ano?", type=int)

        self.batimentos.dia = dia
        self.batimentos.mes = mes
        self.batimentos.ano = ano

    def __calcular_idade(self):
        idade = self.batimentos.calcula_idade()
        self.menu.print(msg=f"Sua idade é de {idade} anos")

    def __frequencia_cardiaca_alvo(self):
        alvo = self.batimentos.frequencia_cardiaca_alvo()
        variacao = "e ". join(map(str, alvo))
        self.menu.print(msg=f"Sua frequência cardiaca alvo deve esta entre {variacao}")


    def __frequencia_cardiaca_maxima(self):
        maxima = self.batimentos.frequencia_cardiaca_maxima()
        self.menu.print(msg=f"Sua frequência cardiaca maxima é {maxima}")


    def __logout(self):
        self.logado = False


main = Main()
main.main_loop()
