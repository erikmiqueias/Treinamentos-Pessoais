# Operações de Soma, Subtração e Multiplicação em Bases Numéricas
from time import sleep

print("Bem Vindo à calculadora de operações em bases numéricas!")
sleep(1)
print()

def conversor():
    while True:
        def base_converter(número, base):
            if base == 2:
                return(bin(número)[2:])
            elif base == 8:
                return(oct(número)[2:])
            elif base == 10:
                return(str(número))
            elif base == 16:
                return(hex(número)[2:])
            
        def adição_binária(a, b):
            return base_converter(int(a, 2) + int(b, 2), 2)

        def subtração_binária(a, b):
            return base_converter(int(a, 2) - int(b, 2), 2)

        def multiplicação_binária(a, b):
            return base_converter(int(a, 2) * int(b, 2), 2)

        a = input("Digite o primeiro valor: ")
        base_a = int(input("Digite a base numérica do primeiro valor (2, 8, 10 ou 16): "))
        if base_a not in [2, 8, 10, 16]:
            print("Base numérica inválida, Saindo...")
            sleep(2)
            exit()
        b = input("Digite o segundo valor: ")
        base_b = int(input("Digite a base numérica do segundo valor (2, 8, 10 ou 16): "))
        if base_b not in [2, 8, 10, 16]:
            print("Base numérica inválida, Saindo...")
            sleep(2)
            exit()
            
        try:
            a_bin = base_converter(int(a, base_a), 2)
        except ValueError:
            print("Valor inválido para a base numérica informada.")
            exit()
        try:
            b_bin = base_converter(int(b, base_b), 2)
        except ValueError:
            print("Valor inválido para a base numérica informada.")
            exit()
    
        try:
            soma = adição_binária(a_bin, b_bin)
            subtração = subtração_binária(a_bin, b_bin)
            multiplicação = multiplicação_binária(a_bin, b_bin)
        except ValueError:
            print("Erro ao realizar operação, Saindo...")
            sleep(2)
            exit()
            
        try:
            print("Resultado da soma: ", base_converter(int(soma, 2), base_a))
            print("Resultado da subtração: ", base_converter(int(subtração, 2), base_a))
            print("Resultado da Multiplicação: ", base_converter(int(multiplicação, 2), base_a))
            break
        except ValueError:
            print("Erro ao converter resultado para base numérica original, Saindo...")
            sleep(2)
            exit()
            
            
conversor()            