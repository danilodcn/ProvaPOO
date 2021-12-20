from typing import List
from rich.console import Console

console = Console()

class Menu:
    def __init__(self):
        self.opcoes: List[str]= []

    def mostrar_menu(self, msg: str="Escolha uma das opções", input=True, qtd=3):
        console.print('Menu de Opções', style='bold')
        for i, linha in enumerate(self.opcoes, 1):
            self.print(bold=f"{i}.", msg=linha)
        
        if input:
            try:
                res = self.input(
                    f"{msg}",
                    qtd=qtd,
                    options=[i for i in range(1, 1 + len(self.opcoes))],
                    type=int
                )
                # import ipdb; ipdb.set_trace()
                return self.opcoes[res-1]

            except Exception as err:
                return "!escape"

        return ""

    def print(self, bold: str="", msg: str=""):
        console.print(f"[bold]{bold} [/bold]", style='bold green', end=" ")
        console.print(msg.title())
    
    def input(self, msg: str='', qtd=3, options=[], type=str):
        for i in range(1, qtd+1):
            try:
                res = type(console.input(f"{msg}\n>>> "))
                if not options or res in options:
                    return res

            except Exception as err:
                self.print(bold=f"Houve um erro. ", msg=f"{err}")

            if i < qtd:
                msg = 'Tente novamente'
                if options:
                    opcoes = ", ".join(options)
                    msg=f"opções possíveis são {opcoes}"
                self.print(bold=f"Tentativa {i+1}/{qtd}: ", msg=msg)   

        raise Exception("erro")
            
