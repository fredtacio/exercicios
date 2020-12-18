# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:18:52 2020

@author: Fred
"""
#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';


nome =""
idade = 151
salario = -5
sexo = ""
ec= ""
while len(nome)<=3:#len(variavel) retorna o comprimento da string, tbm serve pra listas
    nome=input("insira um nome com mais de 3 letras: ")
while idade<0 or idade>150:
    idade=int(input("inisira a idade entre 0 e 150: "))
while salario<0:
        salario=int(input("inisira salario maior q zero: "))
while sexo != "f" and sexo != "m":
    sexo=input("insira sexo f ou m ")
while ec != "s" and ec!= "c" and ec != "v" and ec!= "d":
    ec=input("insira sexo  s c v d")
print("seu nome eh", nome, "sua idade eh", idade, "seu salario eh", salario, "seu sexo eh", sexo, "e seu estado civil eh",ec)
    