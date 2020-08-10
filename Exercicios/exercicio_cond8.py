'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a de9cisão é sempre pelo mais barato.'''

produto1 = float(input('Digite o preço do produto: '))
produto2 = float(input('Digite o preço do produto: '))
produto3 = float(input('Digite o preço do produto: '))

if produto1 < produto2 and produto1 < produto3:
    print('Mais barato',produto1)
elif produto2 < produto1 and produto2 < produto3:
    print('Mais barato',produto2)
else:
    print('Mais barato', produto3)
