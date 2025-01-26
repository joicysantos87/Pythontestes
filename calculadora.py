def calculadora():
    print("Bem-vindo à Calculadora!")
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    while True:
        try:
            operacao = int(input("Digite o número da operação desejada (1/2/3/4): "))

            if operacao not in [1, 2, 3, 4]:
                print("Por favor, escolha uma operação válida.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == 1:
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            elif operacao == 2:
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            elif operacao == 3:
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            elif operacao == 4:
                if num2 == 0:
                    print("Erro: divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado:.2f}")

            continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
            if continuar != 's':
                print("Encerrando a calculadora. Até logo!")
                break

        except ValueError:
            print("Entrada inválida. Por favor, insira números e selecione uma operação corretamente.")

if __name__ == "__main__":
    calculadora()
