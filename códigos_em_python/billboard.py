# Mensagem Formatada com Pyfiglet e Termcolor
'''from pyfiglet import figlet_format
from termcolor import colored 

msg = str(input('Digite uma mensagem: '))

print(colored(figlet_format(msg), color='white'))'''

from pyfiglet import figlet_format
from termcolor import colored

branco = 'white' and 'branco'
preto = 'black' and 'preto'
vermelho = 'red' and 'vermelho'
roxo = 'magenta' and 'roxo'
verde = 'green' and 'verde'
amarelo = 'yellow' and 'amarelo'
azure = 'cyan' and 'ciano'
azul = 'blue' and 'azul'

msg = str(input('Digite uma mensagem: '))
escolha = str(input('Digite a cor da mensagem: ')).upper().capitalize().lower()


if escolha == branco or escolha == 'white':
    print(colored(figlet_format(msg), color='white' or 'branco'))
elif escolha == preto or escolha == 'black':
    print(colored(figlet_format(msg), color='black' or 'preto'))
elif escolha == vermelho or escolha == 'red':
    print(colored(figlet_format(msg), color='red' or 'vermelho'))
elif escolha == roxo or escolha == 'magenta':
    print(colored(figlet_format(msg), color='magenta' or 'roxo'))
elif escolha == verde or escolha == 'green':
    print(colored(figlet_format(msg), color='green' or 'verde'))
elif escolha == amarelo or escolha == 'yellow':
    print(colored(figlet_format(msg), color='yellow' or 'amarelo'))
elif escolha == azure == 'cyan':
    print(colored(figlet_format(msg), color='cyan' or 'ciano'))
elif escolha == azul or escolha == 'blue':
    print(colored(figlet_format(msg), color='blue' or 'azul'))
else:
    print('Digite uma opção válida!')
