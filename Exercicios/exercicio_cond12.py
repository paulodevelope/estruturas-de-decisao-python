'''faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

valor_hora = float(input('Digite o valor da hora trabalhada R$ '))
total_hora = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salário = valor_hora * total_hora
if salário <= 900:
    print('Isento de descontos total liquido: R$ ', salário)

if salário > 900 and salário <= 1500:
    ir = salário * 5 / 100
    inss = salário * 10 /100
    fgts = salário * 11 /100
    descontos = ir + inss
    sal_liquido = salário - descontos
    print('Salario Bruto R$ ',salário)
    print('IR (5%) R$ ',ir)
    print('INSS (10%) R$ ',inss)
    print('FGTS (11%)', fgts)
    print('Total de descontos R$ ', descontos)
    print('Sálario Líquido R$ ', sal_liquido)
    
if salário > 1500 and salário <= 2500:
    ir = salário * 10 / 100
    inss = salário * 10 /100
    fgts = salário * 11 /100
    descontos = ir + inss
    sal_liquido = salário - descontos
    print('Salario Bruto R$ ',salário)
    print('IR (10%) R$ ',ir)
    print('INSS (10%) R$ ',inss)
    print('FGTS (11%)', fgts)
    print('Total de descontos R$ ', descontos)
    print('Sálario Líquido R$ ', sal_liquido)

if salário >= 2500:
    ir = salário * 5 / 100
    inss = salário * 10 /100
    fgts = salário * 11 /100
    descontos = ir + inss
    sal_liquido = salário - descontos
    print('Salario Bruto R$ ',salário)
    print('IR (20%) R$ ',ir)
    print('INSS (10%) R$ ',inss)
    print('FGTS (11%)', fgts)
    print('Total de descontos R$ ', descontos)
    print('Sálario Líquido R$ ', sal_liquido)
