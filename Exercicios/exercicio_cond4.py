#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = str(input('Digite a letra: '))

if letra == 'a'or letra == 'e' or letra == 'i' or  letra == 'o'or letra == 'u':
    print('Essa letra é uma vogal')
else:
    print('Essa letra é uma consoante')