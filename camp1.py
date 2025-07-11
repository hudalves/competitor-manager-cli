import questionary
import os
from tabulate import tabulate
import funcoes as fc
fc.titulo()
def menu():
    while True:
        opt = questionary.select(
            "Escolha uma opção:",   
            choices=[
                "Pesquisar competidor",
                "Listar competidores",
                "Adicionar competidor",
                "Remover competidor",
                "Atualizar competidor",
                "Sair do programa"
            ]
            ).ask()
        fc.limpar()
        fc.mostralinha()
        if opt == "Pesquisar competidor":
            fc.pesquisar()
            fc.mostralinha()
        elif opt == "Listar competidores":
            fc.exibir_tabela ()
            fc.mostralinha()
        elif opt == "Adicionar competidor":
            fc.adicionar()
            fc.mostralinha()
        elif opt == "Remover competidor":
            fc.remover()
            fc.mostralinha()
        elif opt == "Atualizar competidor":
            fc.atualizar()
            fc.mostralinha()
        elif opt == "Sair do programa":
            print("Saindo do programa...")
            fc.mostralinha()
            break       
if __name__ == "__main__":
    menu()
