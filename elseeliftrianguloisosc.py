a = int(input('insira o lado a: ')) #o python quando se declara uma variável a transforma no tipo string, mais usado para letras palavras etc, por o int () a transforma em inteiro
b = int(input('insira o lado b: '))
c = int(input('insira o lado c: '))
if a==b==c:
    print ("o triangulo é isósceles")
elif a>b and a>c:
    print("o triangulo nao é isósceles e o maior lado é o a")
    
elif b>a and b>c:
    print("o triangulo nao é isósceles e o lado maior é o b")
    
else:
    print("o triangulo nao é isósceles e o lado maior é o c")
    
input()
   
    
    
#o elif se comporta como um else da if anterior, porém com a capacidade de testar
#mais uma condição, sendo que o else apenas trata como senão de uma condição anterior,
#sem introduzir uma nova condição
#https://www.programiz.com/python-programming/if-elif-else
