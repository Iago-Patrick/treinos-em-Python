class user:
    def __init__(user, name, age):
            user.nome = name
            user.idade = age

class numeros:
    def __init__ (num, fist, seg, operação):
        num.num1 = fist
        num.num2 = seg
        num.operação = operação

def inicio():

    print('digite seu nome')
    nome = input()

    print('digite sua idade')
    idade = int(input())

    dados = user(nome, idade)

    print('então seu nome é, ', dados.nome)
    print('e sua idade é, ', dados.idade)
    print('Bem Vindo a calculadora,', dados.nome)

def fist():
    inicio()
    checkout()

def InitCalculadora():
    print('digite os numero que você quer calcular, pressione ENTER entre um e outro.')
    num1 = int(input())
    num2 = int(input())

    print('digite a operação matemarica (/, *, +, -)')
    operação = input()

    dig = numeros(num1,num2,operação)


    if(dig.operação == '*'):
        respostas = dig.num1*dig.num2

    if(dig.operação == '/'):
        respostas = dig.num1 / dig.num2

    if(dig.operação == '+'):
        respostas = dig.num1 + dig.num2

    if(dig.operação == '-'):
        respostas = dig.num1 - dig.num2

    print('o resultado é ',respostas )

def checkout():
    print('pressione s ou n, se essa informação estiver correta.')
    resposta = input()

    if(resposta == 'n'):
        fist()

    if(resposta == 's'):
        InitCalculadora()

fist()