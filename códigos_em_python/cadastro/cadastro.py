# Mini sistema para cadastro e separação de alunos em turmas
from time import sleep
import os

turma = []
turma2 = []
turma3 = []

def menu():
    while True:
        print("=-"*20)
        print("1 - Cadastrar aluno\n2 - Listar alunos\n3 - Sair")
        print("=-"*20)
        op = int(input("Digite a opção desejada: "))
        if op == 1:
            return(cad())
        elif op == 2:
            print("Abrindo lista de alunos...")
            sleep(2)
            print("1 - Turma A\n2 - Turma B\n3 - Turma C\n4 - Voltar")
            escolha = int(input("Escolha a turma que deseja listar os alunos: "))
            if escolha == 1:
                with open("turmaA.txt", "r") as turmaA:
                    for linha in turmaA:
                        print(linha, end="")    
            elif escolha == 2:
                with open("turmaB.txt", "r") as turmaB:
                    for linha in turmaB:
                        print(linha, end="")
            elif escolha == 3:
                with open("turmaC.txt", "r") as turmaC:
                    for linha in turmaC:
                        print(linha, end="")
        elif op == 3:
            print("Finalizando...")
            sleep(2)
            break
        elif op == 4:
            print("Voltando...")
            sleep(2)
            return(menu())
def cad():
    while True:
        print("=-"*20)
        print("1 - Turma A\n2 - Turma B\n3 - Turma C") 
        print("=-"*20)
        escolha = int(input("Escolha a turma que deseja cadastrar o aluno: "))
        sleep(2)
        if escolha == 1:
            nome = str(input("Digite o nome do aluno: "))
            turma.append(nome)
            with open("turmaA.txt", "a") as turmaA:
                turmaA.write(f"{nome}\n")
            print("Aluno cadastrado com sucesso na turma Turma A!")
            return(menu())
            
        elif escolha == 2:
            nome = str(input("Digite o nome do aluno: "))
            turma2.append(nome)
            with open("turmaB.txt", "a") as turmaB:
                turmaB.write(f"{nome}\n")
            print("Aluno cadastrado com sucesso na turma Turma B!")
            return(menu())
        
        elif escolha == 3:
            nome = str(input("Digite o nome do aluno: "))
            turma3.append(nome)
            with open("turmaC.txt", "a") as turmaC:
                turmaC.write(f"{nome}\n")
            print("Aluno cadastrado com sucesso na turma Turma C!")
            return(menu())

menu()

        
        