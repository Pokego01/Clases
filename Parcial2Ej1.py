x=int(2)
y=int(0)
z=int(0)
while x<30:
    print(x)
    x=x+3
    if x%5==0:
        y=y+x
    elif x%2==1:
        z=z+x

print("La suma de los numeros divisibles por 5 son", y)
print("La suma de los numeros impares es:", z)