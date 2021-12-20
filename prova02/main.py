from re import S
from typing import Dict, List
from menu import Menu
from models import Usuario, Produto


class Main:
    def __init__(self):
        self.user = None

        self.opcoes_deslogado = {
            "novo usuário": self.__novo_usuario,
            "login": self.__login,
            "sair": exit
        }

        self.opcoes_logado = {
            "incluir novo produto": self.__novo_produto,
            "listar produtos": self.__listar_todos_os_produtos,
            "adicionar ao estoque": self.__adicionar_ao_estoque,
            "remover produto": self.__remover_do_estoque,
            "logout": self.__logout
        }

        self.menu = Menu()

    def __menu_todos_produtos(self):
        produtos = self.__listar_produtos()
        opcoes = dict([
            (produto.descricao, i) for i, produto in enumerate(produtos)
        ])

        self.menu.opcoes = list(opcoes.keys())

        resposta = self.menu.mostrar_menu()
        id = opcoes[resposta]

        return produtos[id], opcoes

    def __remover_do_estoque(self):
        produto, opcoes = self.__menu_todos_produtos()
        
        quantidade = self.menu.input(
            msg="Quantidade do produto",
            type=int,
            options=list(opcoes.values())
        )

        if produto.quantidade < quantidade:
            self.menu.print(
                "não é possível fazer a saída de estoque",
                "- quantidade menor que o valor desejado"
            )
        else:
            produto.quantidade -= quantidade
            produto.save()
            self.menu.print("Quantidade removida")

        if produto.quantidade == 0:
            produto.delete_instace()


    def __adicionar_ao_estoque(self):
        produtos = self.__listar_produtos()
        opcoes = dict([
            (produto.descricao, i) for i, produto in enumerate(produtos)
        ])

        self.menu.opcoes = list(opcoes.keys())

        resposta = self.menu.mostrar_menu()
        id = opcoes[resposta]
        produto: Produto = produtos[id]

        quantidade = self.menu.input(
            msg="Quantidade do produto",
            type=int,
            options=list(opcoes.values())
        )

        produto.quantidade += quantidade
        produto.save()
        # import ipdb; ipdb.set_trace()

    def __novo_produto(self):
        descricao = self.menu.input(msg="Qual a descricao do produto")
        quantidade = self.menu.input(msg="Quantidade do produto", type=int)

        Produto.create(
            descricao=descricao,
            quantidade=quantidade,
            user=self.user
        )

        self.menu.print("produto adicionado...")

    def __listar_todos_os_produtos(self):
        produtos = self.__listar_produtos()
        if len(produtos):
            for i, produto in enumerate(produtos, 1):
                txt = f'descrição: {produto.descricao}, '
                txt += f'quantidade: {produto.quantidade}'

                self.menu.print(str(i), txt)

        else:
            self.menu.print("Atualmente sua lista está vazia")

    def __listar_produtos(self):
        if self.user:
            query = Produto.select().join(Usuario).where(
                Usuario.id==self.user.id
            )
            # import ipdb; ipdb.set_trace()
            produtos = [produto for produto in query]

        else: 
            produtos = []

        return produtos

    def __novo_usuario(self):
        username = self.menu.input(msg="Entre com seu nome de usuário")
        password = self.menu.input(msg="Entre com sua senha", password=True)
        try:
            Usuario.get(Usuario.username==username)
            self.menu.print("Usuário já existe")
            opcoes = {
                "sair": lambda: ...,
                "tentar novamente": self.__novo_usuario,
            }
            self.menu.opcoes = list(opcoes.keys())
            resposta = self.menu.mostrar_menu()
            try:
                opcoes[resposta]()
            except:
                ...

        except:
            self.user = Usuario.create(username=username, password=password)
            self.menu.print("Usuário criado")       

    def __login(self):
        username = self.menu.input(msg="Entre com seu nome de usuário")
        password = self.menu.input(msg="Entre com sua senha", password=True)
        # import ipdb; ipdb.set_trace()
        try:
            self.user = Usuario.get(
                Usuario.username==username,
                Usuario.password==password
            )
        except Usuario.DoesNotExist:
            self.menu.print("Usuário ou senha está incorreto")
            opcoes = {
                "sair": lambda: ...,
                "tentar novamente": self.__login,
            }
            self.menu.opcoes = list(opcoes.keys())
            resposta = self.menu.mostrar_menu()
            try:
                opcoes[resposta]()
            except:
                ...

        self.menu.print("usuário logado")
            
        # Usuario.objects.filter(username=username, password=password)


    def __logout(self):
        self.user = None

    def main_loop(self):
        while True:
            if self.user is None:
                self.menu.opcoes = list(self.opcoes_deslogado.keys())

                resposta = self.menu.mostrar_menu()
                # import ipdb; ipdb.set_trace()
                self.opcoes_deslogado[resposta]()

            else:
                self.menu.opcoes = list(self.opcoes_logado.keys())

                resposta = self.menu.mostrar_menu()
                # import ipdb; ipdb.set_trace()
                self.opcoes_logado[resposta]()


if __name__ == "__main__":
    Main().main_loop()
