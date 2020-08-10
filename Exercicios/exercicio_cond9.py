'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

print(num1, num2, num3)

if num1 < num3:
    num1, num3 = num3, num1

if num1 < num2:
    num1, num2 = num2 , num1

if num2 < num3:
    num2, num3 = num3, num2

print(f'a ordem descrescente é {num1}, {num2}, {num3}')