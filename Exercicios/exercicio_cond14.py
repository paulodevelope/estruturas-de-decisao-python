'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao 
longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E'''


nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))
nota3 = float(input('Digite a nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média aluno é: ' ,media)



if media >= 9 and media <=10:
    print('Conceito A se é o bichão APROVADO ')

elif media >= 7 and media <= 9:
    print('Conceito B o importante é passar kkkk  APROVADO')

elif media >=6 and media <=7:
    print('Conceito C EXAMEEEEE !!!!! ')

elif media >= 0 and media <=5:
    print("Conceito D  de DP!!!  REPROVADO ATÉ O PROXIMO SEMESTRE ")





