#função
#uma função é projetado pra realizar uma tarefa especifica 
#encapsulamento de codigo
#parametro e argumentos
#valor de retorno
#modulção

#como criar uma função
#def: é a palavra chave para iniciar uma definição de uma função
#nome_da_funcao
#definição de parametros: eles são valores que você pode passar para a função quando chama-la.
#return

#variavel global
#espaço amplo
#precisa da palavra-chave

import random
numero_aleatorio = random.randrange(11)
print(f"o {numero_aleatorio} que caiu na roleta")

#try:
    #numero = int(input("digite um número:"))
    #resultado = 10 / numero

#except ValueError:
    #print("valor invalido! Você deve digitar numero>")

#except ZeroDivisionError:
    #print("erro: não é possivel dividir por zero.")
#else:
    #print(f"o resultado é: {resultado}")
#finally:
    #print("divisão esta ok")

#def soma(num1 , num2):
    #num1 = 2
    #num2 = 5
    #resultado = num1 + num2
    #return resultado

#def notas(nota1, nota2, nota3, nota4):
    #nota1 = input("qual é a sua primeira nota?")
    #nota2 = input("qual é a sua segunda nota?")
    #nota3 = input("qual é a sua terceira nota?")
    #nota4 = input("qual é a sua quarta nota?")
    #num = 4
    #media = (nota1 + nota2 + nota3 + nota4) // num
    #if media >= 5:
        #print("aprovado")

#def calculo_media(nota1, nota2)
    #media = nota1 + nota2 + nota3 + nota4 / 2
    #return media

#contador = 0
#def incrementar():
    #global contador # indica que estamos usando a variavel global
    #contador =+ 1

#incrementar()
#print(contador) #saida 1