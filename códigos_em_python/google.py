# Exemplo de Código para buscar urls no google

from googlesearch import search
from time import sleep

print("Enter your query(format: 'www.example.com' or 'example.com' or 'example' or 'www.example' or 'example.com/xyz' or 'example/xyz')")
sleep(2)
query = str(input("Enter your query: "))

for url in search(query):
    print(url)