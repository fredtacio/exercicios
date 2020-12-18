# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:30:10 2020

@author: Fred
"""
#Módulos
import math


#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
print("O programa vai calcular o preço e quantidade de litros de tinta necessários")
print("cada metro quadrado necessita de 6 litros de tinta")
area = float(input("insira a área a ser pintada"))
litros=area/6
print ("voce precisa de", litros, "litros de tinta") 
print("digite 1 se deseja compra apenas galoes de 18l, que custam 80 reais cada")
print("digite 2 se deseja compra apenas galoes de 3,6l, que custam 25 reais cada")
print("digite 3 se deseja compra apenas galoes de 19l, e complementar o restante com galao de 3.6")
op = int(input())
if op==1:
    latas=math.ceil(litros/18) #math.ceil arredonda PRA CIMA sempre ex 1.1 vira 2
    print("voce precisara de", latas, "latas de tinta")
    print("isso custará",latas*80, "reais")
    input()
    #calcular o tanto que sobra de tinta
elif op==2:#saudoso else com if dentro
    latas=math.ceil(litros/3.6)
    print("voce precisara de", latas, "latas de tinta")
    print("isso custará",latas*25, "reais")
    input()
     #calcular o tanto que sobra de tinta
elif op==3:
         if litros<3.6:
             print ("Voce necessita de apenas uma lata de 3.6 litros. 25 reais")
             input()
         elif litros<18:
             print ("voce precisa de uma lata de 18 litros, 80 reais")
             input()
         else:
             latas=litros/18
             print("isso custara",round(latas-0.5)*80+25)
             input()
     