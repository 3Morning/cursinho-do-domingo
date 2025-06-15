def monstrar_menu():
    print('bem vindo ao programa de calculadora')
    print('+, soma')
    print('-, subtração')
    print('*, multiplição')
    print('/, divição')
    print('0, sair')

def coletar_numeros():
    while True:
            num1 = float(input("escolha seu primeiro numero: "))
            num2 = float(input("escolha seu segundo numero: "))
            return num1, num2
        
def soma(num1, num2):
    resultado = num1 + num2
    return num1 + num2

def sub(num1, num2):
    return num1 - num2
def mut(num1, num2):
    return num1 * num2
def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 0