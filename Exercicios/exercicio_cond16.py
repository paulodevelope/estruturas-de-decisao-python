
import math

a = float(input("digite o A"))
if (a==0):
  print("A equação não é do segundo grau")
  quit() # termina o programa
b = float(input("digite o B"))
c = float(input("digite o C"))
sinal_b = "+" if (b>0) else ""
sinal_c = "+" if (c>0) else ""
print("a equação é ",a,"x²",sinal_b,b,"x",sinal_c,c,sep="")
delta = b*b - 4*a*c 
if delta < 0:
  print("A equação não tem raízes reais")
elif delta == 0:
  print("A equação tem uma raíz só",-b/2*a)
else:
  print("A equação tem duaz raízes")
  print("Raiz um",(-b-math.sqrt(delta))/2*a)
  print("Raiz um",(-b+math.sqrt(delta))/2*a)