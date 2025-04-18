import art
#  construção das funções de cada operação
def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

# armazenamos as operações em um dicionário e criamos as variáveis de apoio
operations = {'+': add, '-': sub, '*': mult, '/': div,}

def calculator():
    program_on = True # será usado para manter o programa funcionando enquanto for True

    # damos início a construção visual do programa
    print(art.logo)

    while True:
        try:
            num1 = float(input('Informe o primeiro número: '))
        except:
            print('Informe um número!')
        else:
            break

    while program_on:
        try:
            for symbol in operations:
                print(symbol)
            operation_choice = input("Qual operação deseja realizar?\n")
            num2 = float(input('Informe o segundo número: '))
            answer = operations[operation_choice](num1, num2)

        except:
            print('Informe apenas números, não deixe as opções vazias e escolha um operador válido')
            continue

        else:
            print(f'{num1} {operation_choice} {num2} = {answer}')

        choice = input(f'Digite [S] para continuar calculando com {answer}\n[N] novo cálculo\n[F] fechar o programa:\n').upper()

        if choice == 'S':
            num1 = answer
        elif choice == 'N':
            program_on = False
            print('\n' * 25)
            calculator() # usamos recursão para manter a calculadora funcionando
        else:
            return print("Programa encerrado!")

calculator()