#operações aritimeticas:

#---------------------------------------------
#Estruturas Condicionais (if - else)
# if = se
#else = se não

#maria_esta_matriculada_no_curso_de_python = True
#maria_tem_como_vir_presencialmente = False

#if maria_esta_matriculada_no_curso_de_python and maria_tem_como_vir_presencialmente:
    #print ("maria pode ter as aulas")
#else:
    #print("maria não pode vir")


#anos = 15
#if anos <= 17: #anos (15) é menor ou igual a 17?
    #print("ele é muito novo")
#else:
    #print("ele é de maior")

#idade_usuario = 18
#if idade_usuario < 10:
    #print("criança")
#elif idade_usuario < 18:
    #print("adolecente")
#elif idade_usuario < 60:
    #print("adulto")
#else:
    #print("idoso")
#----------------------------------------------------------------
#operações logicas:

#tabela verdade (v = verdadeiro e f = falso)
#|v|V|= v (retorno verdadeiro)
#|v|F|= f (retorno falso)
#|f|v|= f (retorno falso)
#|f|f|= f (retorno falso)

#true and true < ---- o retorno será verdadeiro
#true and false <----o retorno será false

#"e" -> (and)
#maria_tem_matricula_no_curso = False
#maria_vem_presencialmente = True

#print(maria_tem_matricula_no_curso and maria_vem_presencialmente)

#or = ou
#maria_vem_de_Onibus = False
#maria_vem_de_carro = True

#print(maria_vem_de_Onibus or maria_vem_de_carro)

#not <---- negação
#se algo é false (com not) vira verdadeiro
#se algo é verdadeiro (com not) vira false

#-------------------------------------------
#operação de comparação:
# x = 10 <--- isso não uma comparação e sim uma atribuiçáo;
# igualdade (==): 
# a == 10

#diferencia (!=):
#b != 9

#mais e menos (< ou >)
#10 > 20 #false
#10 < 20 #true
#20 > 20 #false

#maior igual e menos igual(<= ou >=)
#20 >= 20 #true
#20 >= 22 #false
#25 >= 22 #true
#-----------------------------------

# operações atribuição:
#soma
#a = 5
#a += 3 #equivalente a: a = a + 3
#print(a)

#subtração
#a = 10
#a -= 4 #equivalente a: a = a - 4
#print (a)# saida: 6
#---------------------------------------------------

nota1 = input("qual é a sua primeira nota?")
nota2 = input("qual é a sua segunda nota?")
nota3 = input("qual é a sua terceira nota?")
nota4 = input("qual é a sua quarta nota?")
num = 4
media = (nota1 + nota2 + nota3 + nota4) // num
if media >= 5:
    print("aprovado")