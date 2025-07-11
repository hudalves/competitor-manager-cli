import questionary
import os
import colorama
colorama.init()
from tabulate import tabulate
Verm="\033[1;31m"
Verde="\033[1;32m"
Amar="\033[1;33m"
Azul="\033[1;34m"
Reset="\033[0;m"

def mostralinha():  
    print("-" * 90)
def limpar():
    os.system('cls')
def tabela():
    mostralinha()
    with open('dados.txt','r') as RD:
        lista = [linha.strip().split(',') for linha in RD if linha.strip()]
        return lista
def exibir_tabela ():
    limpar()
    mostralinha()
    print(f"{Azul}Lista de Competidores{Reset}")
    mostralinha()
    with open('dados.txt','r') as RD:
        lista = [linha.strip().split(',') for linha in RD if linha.strip()]
        cabeçalho=['Modalidade','Gênero','RG','CPF',"Nome",'Idade','Peso']
        print(tabulate(lista, headers=cabeçalho, tablefmt='rounded_grid', stralign='center', numalign='center'))  
def remover():
    limpar()
    mostralinha()
    print(f"{Azul}Remover Competidor {Reset}")
    mostralinha()
    D1 = {}
    with open("dados.txt", "r") as RD:
        for linha in RD:
            campos = linha.strip().split(",")
            if len(campos) >= 7:
                D1[campos[2]] = campos  
    exibir_tabela()
    try:
        rg = input("Digite o RG do competidor a ser removido: ").strip()
        if len(str(rg)) != 9 :
            print(f"{Verm}RG deve conter 9 dígitos.{Reset}")
            return 
        elif rg not in D1:
            print(f"{Verm}RG não encontrado. {Reset}")
            return
    except:
            print(f"{Verm}RG deve conter apenas números. {Reset}")
            return
            
    conf=input(f"Tem certeza que deseja remover o competidor? {D1[rg][4]} (s/n): ")
    if conf.lower() == 's':
        del D1[rg]
        print(f"{Verde}Competidor removido com sucesso! {Reset}")
        with open("dados.txt", "w") as WR:
            for campos in D1.values():
                WR.write(",".join(campos) + "\n")
    else:
        print(f"{Amar}Operação cancelada. {Reset}")    
        return    
def adicionar():
    limpar()
    mostralinha()
    print(f"{Azul}Adicionar Competidor {Reset}")
    mostralinha()
    with open('dados.txt','a') as AR:
        modalidade = questionary.select(
            "Escolha uma modalidade:",
            choices=[
                "Boxe",
                "Muay Thai",
                "Jiu Jitsu",
                "Judô",
                "MMA"
            ]
        ).ask()
    with open('dados.txt','a') as AR:
        genero = questionary.select(
            "Escolha o sexo:",
            choices=[
                "Masculino",
                "Feminino"
            ]
        ).ask()
        try:
            lista = tabela()
            rg = int(input("RG: "))
            if len(str(rg)) != 9 :
                print(f"{Verm}RG deve conter 9 dígitos. {Reset}")
                return
            if any(linha[2] == str(rg) for linha in lista):
                print(f"{Verm}RG já cadastrado. {Reset}")
                return
        except ValueError:
            print(f"{Verm}RG deve conter apenas números. {Reset}")
            return
        try:
            cpf = int(input("CPF: "))
            if len(str(cpf)) != 11:
                print(f"{Verm}CPF deve conter 11 dígitos. {Reset}")
                return
            if any(linha[3] == str(cpf) for linha in lista):
                print(f"{Verm}CPF já cadastrado. {Reset}")
                return
        except ValueError:
            print(f"{Verm}CPF deve conter apenas números. {Reset}")
            return
        try:
            nome = str(input("Nome: "))
        except ValueError:
            print(f"{Verm}Nome deve conter apenas letras. {Reset}")
            return
        try:
            idade = int(input("Idade: "))
            if idade < 18:
                print(f"{Verm}Idade minima de 18 anos. {Reset}")
                return
        except ValueError:
            print(f"{Verm}Idade deve conter apenas números. {Reset}")
            return
    with open('dados.txt','a') as AR:
        if genero == 'Feminino': 
                    peso = questionary.select(
            "Escolha a categoria de peso:",
            choices=[
                "Peso palha(até 52.1kg)",
                "Peso mosca(até 56.7kg)",
                "Peso galo(até 61.2kg)",
                "Peso pena(até 65.8kg)",
                "Peso leve(até 70.3kg)",
                "Peso meio-médio(até 77.1kg)",
                "Peso médio(até 83.9kg)",
            ]
        ).ask()       
        elif genero == 'Masculino':
                    peso = questionary.select(
            "Escolha a categoria de peso:",
            choices=[
                "Peso mosca(até 56.7kg)",
                "Peso galo(até 61.2kg)",
                "Peso pena(até 65.8kg)",
                "Peso leve(até 70.3kg)",
                "Peso meio-médio(até 77.1kg)",
                "Peso médio(até 83.9kg)",
                "Peso meio-pesado(até 93.0kg)",
                "Peso pesado(até 120.2kg)"
            ]
        ).ask()
               
        
        AR.write(f'\n{modalidade},{genero},{rg},{cpf},{nome},{idade},{peso}')
        print(f"{Verde}Competidor adicionado com sucesso! {Reset}")
        input("Pressione Enter para continuar...")
        limpar()
        return titulo()
    
def pesquisar():
    limpar()
    mostralinha()
    print(f"{Azul}Pesquisar Competidor {Reset}")
    mostralinha()
    try:
        termo = str(input("Digite o nome a ser pesquisado: ")).strip().lower()
        if not termo:
            print(f"{Verm}Digite pelo menos uma letra. {Reset}")
            return
    except ValueError:
        print(f"{Verm}Digite apenas letras. {Reset}")
        return
    resultados = []
    with open('dados.txt', 'r') as RD:
        for linha in RD:
            campos = linha.strip().split(',')
            if len(campos) >= 7 and termo in campos[4].lower():
                resultados.append(campos)

    if resultados:
        cabeçalho = ['Modalidade', 'Gênero', 'RG', 'CPF', 'Nome', 'Idade', 'Peso']
        print(tabulate(resultados, headers=cabeçalho, tablefmt='rounded_grid', stralign='center', numalign='center'))
    else:
        print(f"{Verm}Nenhum competidor encontrado. {Reset}")
        return
def titulo():
    mostralinha()
    print(f'''{Amar}
 ██████  █████  ███    ███ ██████  ███████  ██████  ███    ██  █████  ████████  ██████  
██      ██   ██ ████  ████ ██   ██ ██      ██    ██ ████   ██ ██   ██    ██    ██    ██ 
██      ███████ ██ ████ ██ ██████  █████   ██    ██ ██ ██  ██ ███████    ██    ██    ██ 
██      ██   ██ ██  ██  ██ ██      ██      ██    ██ ██  ██ ██ ██   ██    ██    ██    ██ 
 ██████ ██   ██ ██      ██ ██      ███████  ██████  ██   ████ ██   ██    ██     ██████  
 {Reset}''')
    mostralinha()
    return
def atualizar():
    limpar()
    mostralinha()
    print(f"{Azul}Atualizar Competidor {Reset}")
    mostralinha()
    D1 = {}
    with open("dados.txt", "r") as RD:
        for linha in RD:
            campos = linha.strip().split(",")
            if len(campos) >= 7:
                D1[campos[2]] = campos  
    exibir_tabela()
    rg = input("Digite o RG do competidor a ser atualizado: ").strip()
    if len(str(rg)) != 9 :
        print(f"{Verm}RG deve conter 9 dígitos. {Reset}")
        return
    elif not rg.isdigit():
        print(f"{Verm}RG deve conter apenas números. {Reset}")
        return
    elif rg not in D1:
        print(f"{Verm}RG não encontrado. {Reset}")
        return
    conf=input(f"Tem certeza que deseja atualizar o competidor? {D1[rg][4]} (s/n): ")
    if conf.lower() == 's':
        modalidade = questionary.select(
            "Escolha uma modalidade:",
            choices=[
                "Boxe",
                "Muay Thai",
                "Jiu Jitsu",
                "Judô",
                "MMA"
            ]
        ).ask()
        genero = questionary.select(
            "Escolha o sexo:",
            choices=[
                "Masculino",
                "Feminino"
            ]
        ).ask()
        try:
            nome = str(input("Nome: "))
        except ValueError:
            print(f"{Verm}Nome deve conter apenas letras. {Reset}")
            return
        try:
            idade = int(input("Idade: "))
            if idade < 18:
                print(f"{Verm}Idade minima de 18 anos. {Reset}")
                return
        except ValueError:
            print(f"{Verm}Idade deve conter apenas números. {Reset}")
            return
        with open('dados.txt','a') as AR:
            if genero == 'Feminino': 
                        peso = questionary.select(
                "Escolha a categoria de peso:",
                choices=[
                    "Peso palha(até 52.1kg)",
                    "Peso mosca(até 56.7kg)",
                    "Peso galo(até 61.2kg)",
                    "Peso pena(até 65.8kg)",
                    "Peso leve(até 70.3kg)",
                    "Peso meio-médio(até 77.1kg)",
                    "Peso médio(até 83.9kg)",
                ]
            ).ask()       
            elif genero == 'Masculino':
                        peso = questionary.select(
                "Escolha a categoria de peso:",
                choices=[
                    "Peso mosca(até 56.7kg)",
                    "Peso galo(até 61.2kg)",
                    "Peso pena(até 65.8kg)",
                    "Peso leve(até 70.3kg)",
                    "Peso meio-médio(até 77.1kg)",
                    "Peso médio(até 83.9kg)",
                    "Peso meio-pesado(até 93.0kg)",
                    "Peso pesado(até 120.2kg)"
                ]
            ).ask()
        D1[rg] = [modalidade, genero, rg, D1[rg][3], nome, idade, peso]
        with open("dados.txt", "w") as WR:
            for campos in D1.values():
                WR.write(",".join(map(str, campos)) + "\n")
        print(f"{Verde}Competidor atualizado com sucesso! {Reset}")
    return
