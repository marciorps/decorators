

# def depositar_dinheiro():
#     print('depositando dinheiro')

#     def depositando_dolar():
#         print('depositando dolares')

#     def depositando_reais():
#         print('depositando reais')

#     depositando_dolar()
#     depositando_reais()


# depositar_dinheiro()


# def pai(numero):
#     def filho_1():
#         print('Sou filho 1')
#     def filho_2():
#         print('Sou filho 2')
#     if numero == 1:
#         return filho_1
    
# resultado = pai(1)
# resultado()

# Decorators
# def meu_decorator(funcao):
#     def wrapper():
#         print('antes')
#         funcao()
#         print('depois')
#     return wrapper

# @meu_decorator
# def parabenizar():
#     print('Parabéns!')

# parabenizar()


# resultado = meu_decorator(parabenizar)
# resultado()

#Desafio1
## Crie um decorator que ira pegar a função que for passado para ele e imprimir o horario atual
## antes de executar a função que ira usar o módulo datetime para conseguir o horário atual
from datetime import datetime

def decorator(funcao):
    print(datetime.now())
    funcao() 
    print(datetime.now())

@decorator
def cadastro():
    print('Márcio')

