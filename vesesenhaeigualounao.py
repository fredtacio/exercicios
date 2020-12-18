# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:17:44 2020

@author: Fred
"""

us = input("insira o usuario: ")
se = input("insira a senha: ")
while us==se:
    print ("a senha nao pode ser igual ao usuario")
    us = input("insira o usuario: ")
    se = input("insira a senha: ")
else:
    print ("OK!")