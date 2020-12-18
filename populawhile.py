# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:47:52 2020

@author: Fred
"""

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma 
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma
# taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
 #para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
a= int(input("insira a pop A"))
b=int(input("insira a pop B"))
ca=float(input("insira a taxa de cresc pop A"))
cb=float(input("insira a taxa de cresc pop B"))
ca=ca/100
cb=cb/100
i=0
if a<b:
    while a<b:
        a+=a*ca
        b+=b*cb
        i+=1
    else:
        print(i)
elif b<a:
     while b<a:
         b+=b*cb
         a+=a*ca
         i+=1
     else:
         print(i)