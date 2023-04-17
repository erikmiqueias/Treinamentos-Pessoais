from time import sleep

print("Bem Vindo ao Calculador de IMC!")
sleep(1)

while True:
    print("=-=" * 10)
    print("Calculadora de IMC!")
    sleep(2)
    print("=-=" * 10)
    print('''[1] - Calcular IMC\n[2] - Sair''')
    
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
    
        alt = float(input("Digite sua altura: "))
        peso = float(input("Digite seu peso: "))
        if alt and peso != 0:
            
            imc = peso / (alt * alt)
            
            if imc < 16:
                print(f"Seu IMC é de {imc:.2f}. Você está com baixo peso muito grave!")
            elif imc < 18.5:
                print(f"Seu IMC é de {imc:.2f}. Você está abaixo do peso!")
            elif imc >= 18.5 and imc < 25:
                print(f"Seu IMC é de {imc:.2f}. Você está no peso ideal!")
            elif imc >= 25 and imc < 30:
                print(f"Seu IMC é de {imc:.2f}. Você está com sobrepeso!")
            elif imc >= 30 and imc < 40:
                print(f"Seu IMC é de {imc:.2f}. Você está com obesidade!")
            elif imc >= 40:
                print(f"Seu IMC é de {imc:.2f}. Você está com obesidade mórbida!")
            elif alt and peso == 0:
                print("Saindo...")
                sleep(2)
                break
        elif alt and peso == 0:
            print("Saindo...")
            sleep(2)
            break 
    elif opcao == 2:
        print("Saindo...")
        sleep(2)
        break
    else:
        print("Opção inválida! Tente novamente!")
        sleep(2)
        continue

        

        