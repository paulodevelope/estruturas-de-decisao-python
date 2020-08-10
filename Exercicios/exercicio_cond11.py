'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
 e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 880,00 (incluindo) : aumento de 20%
salários entre R$ 880,00 e R$ 1000,00 : aumento de 15%
salários entre R$ 800,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Digite o valor do salario atual R$:  '))

if salario <= 880:
    porcento = (20 /100) * 880
    resultado = salario + porcento
    print('O salario antes do rajuste R$ ', salario)
    print('O percentual de aumento é 20%')
    print('O valor do aumneto R$ ', porcento)
    print('O valor do novo salario após o aumento R$ ', resultado)

if salario > 880 and salario <= 1000:
    porcento = (15 / 100) * 1000
    resultado = salario + porcento
    print('O salario antes do rajuste R$ ', salario)
    print('O percentual de aumento é 20%')
    print('O valor do aumneto R$ ', porcento)
    print('O valor do novo salario após o aumento R$ ', resultado)

if salario > 880 and salario <= 1500:
    porcento = (10 / 100) * 1500
    resultado = salario + porcento
    print('O salario antes do rajuste R$ ', salario)
    print('O percentual de aumento é 20%')
    print('O valor do aumneto R$ ', porcento)
    print('O valor do novo salario após o aumento R$ ', resultado)

if  salario >= 1500:
    porcento = (5 / 100) * 1500
    resultado = salario + porcento
    print('O salario antes do rajuste R$ ', salario)
    print('O percentual de aumento é 20%')
    print('O valor do aumneto R$ ', porcento)
    print('O valor do novo salario após o aumento R$ ', resultado)


