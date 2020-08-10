'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.'''

num = float(input('Digite um numero:'))

if num == round(num):
    print('inteiro')
else:
    print('Decimal')
    print("Arredondado pra baixo: ", round(num-0.5) )
    print("Arredondado pra cima : ", round(num+0.5) )
