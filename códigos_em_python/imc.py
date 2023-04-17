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
                print("Seu IMC é de {:.2f}. Você está com baixo peso muito grave!".format(imc))
            elif imc < 18.5:
                print("Seu IMC é de {:.2f}. Você está abaixo do peso!".format(imc))
            elif imc >= 18.5 and imc < 25:
                print("Seu IMC é de {:.2f}. Você está no peso ideal!".format(imc))
            elif imc >= 25 and imc < 30:
                print("Seu IMC é de {:.2f}. Você está com sobrepeso!".format(imc))
            elif imc >= 30 and imc < 40:
                print("Seu IMC é de {:.2f}. Você está com obesidade!".format(imc))
            elif imc >= 40:
                print("Seu IMC é de {:.2f}. Você está com obesidade mórbida!".format(imc))
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

        

        