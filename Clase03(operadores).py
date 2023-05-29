##operadores aritmeticos
#complex crea un numero complejo
c2= complex(3,-5)


a=20
b=5
print(a == b) #Igual
print(a != b) #Diferente
print(a < b)  #Menor
print(a > b)  #Mayor
print(a <= b) #Menor o Igual
print(a >= b) #Mayor o igual
#En caso de usar palabras este no sera mayor o menor por la cantidad de letras amenos que se use la funcion len()

##Uso del If
bencina = True
encendido = True
edad = 16
if bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede avanzar")
#para que if funcione este necesita 4 espacios o un tab
## para que and arroje un true depende de que ambas variables sean verdaderas pero a la hora de usar o basta con que una sea verdadera
## poner not antes de una variable ya sea verdadera o falsa hara que se niegue dicha propocicion canbiande de true a false y visceversa
if bencina or (encendido and edad>=18):
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede avanzar")

#def es para palabras reservadas y crear nustras propias funciones

def mi_primera_funcion():
    print("esta es mi primera funcion")

mi_primera_funcion()

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1=[1,2,3]
lista2=[4,5,6]
#concatenar
print(concatenar(lista1,lista2))

def multiplicacion(num1,num2):
    return(num1*num2)

x=int(input("Su primer numero a Multiplicar\n"))
y=int(input("Su otro numero a Multiplicar\n"))
print(multiplicacion(x,y))

def suma(s,d):
    return(s+d)

def resta(s,d):
    return(s-d)

s=int(input("Su primer numero a usar\n"))
d=int(input("Su otro numero a usar\n"))

resultado=suma(s,d)
resultado2=resta(s,d)

print("El resultado de la suma de ambos numeros es:", resultado)
print("El resultado de la resta de ambos numeros es:", resultado2)