'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

letra = str(input('Digite a letra: f para feminino ou m para masculino: '))

if letra == 'f':
    print("Sexo feminino")
elif letra == 'm':
    print('Sexo Masculino')
else:
    print('Sexo invalido')
