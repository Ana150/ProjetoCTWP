nome = "Ana"        #Texto é str() no python
idade = 18          #Inteiro é int() no python
altura = 1.64       #Real é float() no python
maiorDeIdade = True # Boolean

print("Seu nome é", nome, "você tem", idade, "e tem", altura, "cm de altura")

#mudando o tipo
valor1 = "10"
#valor1 = int(valor1)
valor2 = "20" #nesse caso a variavel é definida como texto
#valor2 = int(valor2) #convertendo texto para inteiro
#resposta = int(valor1) + int(valor2)
resposta = float(valor1) + float(valor2)

#fomas de exibir um print
print("Resultado:", valor1, "+", valor2, "=", resposta)
print("Resultado: {} + {} = {}".format(valor1, valor2, resposta))
print("Resultado: {0} + {1} = {2} -> {2}".format(valor1, valor2, resposta))
print("Resultado: {v1} + {v2} = {r} -> {r:.2f}".format(v1 = valor1, v2 = valor2, r = resposta))
#:.2f - Número com 2 casas decimais
#:.3f - Número com 3 casas decimais
#:10.2f - Número com 2 casas decimais em 10 bites

a = 56.6
b = 3456.877
c = 2.0

print(f"Valor de a = {a:20.2f} \nValor de b ={b:20.2f} \nValor de c = {c:20.2f}")
print("RS {:10.2f}".format(a))
print("RS {:10.2f}".format(b))
print("RS {:10.2f}".format(c))

x = 23
print(f"Valor de x = {x:6}")
print(f"Valor de x = {x:06}")

#Verificando o tipo das variaveis
valor = 45
print(valor, type(valor))
valor = "Nossa"
print(valor, type(valor))
