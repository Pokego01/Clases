import random
numeros= random.randint(40,350)
import random
def cargar():
    lista=[]
    for x in range(20):
        lista.append(random.randint(40,350))
    return lista

def imprimir (lista):
    print(lista)
    
def mezclar(lista):
    random.shuffle(lista)
    
lista=cargar()
print("Lista generada aleatoriamente")
imprimir(lista)
mezclar(lista)
print("La misma lista luego de mezclar")
imprimir(lista)

print(random.choice(range(20)))
