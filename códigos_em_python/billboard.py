# Mensagem Formatada com Pyfiglet e Termcolor
from pyfiglet import figlet_format
from termcolor import colored 

msg = str(input('Digite uma mensagem: '))

print(colored(figlet_format(msg), color='red'))