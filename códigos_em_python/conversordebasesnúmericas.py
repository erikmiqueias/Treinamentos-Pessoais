# Conversor de Bases Numéricas
from time import sleep
print("-=-" * 10)
print("Bem Vindo ao conversor de bases numéricas!")
print("-=-" * 10)
sleep(2)

def conv():
    while True:
        n1 = int(input("Digite um número inteiro: "))
        print('''Escolha uma das bases para conversão:
        [ 1 ] converter para BINÁRIO
        [ 2 ] converter para OCTAL
        [ 3 ] converter para HEXADECIMAL''')
        opcao = int(input("Sua opção: "))
        if opcao == 1:
            print("{} convertido para BINÁRIO é igual a {}".format(n1, bin(n1)[2:]))
            op = str(input("Deseja continuar a converter S/N? ")).upper().capitalize()
            if op == 'S':
                print("Retornando as opções...")
                sleep(2)
                return(conv())
            elif op == 'N':
                print("Saindo...")
                sleep(2)  
                break
        elif opcao == 2:
            print("{} convertido para OCTAL é igual a {}".format(n1, oct(n1)[2:]))
            op = str(input("Deseja continuar a converter S/N? ")).upper().capitalize()
            if op == 'S':
                print("Retornando as opções...")
                sleep(2)
                return(conv()) 
            elif op == 'N':
                print("Saindo...")
                sleep(2)   
                break
        elif opcao == 3:
            print("{} convertido para HEXADECIMAL é igual a {}".format(n1, hex(n1)[2:]))
            op = str(input("Deseja continuar a converter S/N? ")).upper().capitalize()
            if op == 'S':
                print("Retornando as opções...")
                sleep(2)
                return(conv())
            elif op == 'N':
                print("Saindo...")  
                sleep(2)    
                break
        else:
            print("Digite uma opção válida entre 1 e 3!")
            op = str(input("Deseja continuar a converter S/N? ")).upper().capitalize()
            if op == 'S':
                print("Retornando as opções...Lembre de escolher uma opção válida!")
                sleep(2)
                return(conv())
            elif op == 'N':
                print("Saindo...")
                sleep(2) 
                break
conv()