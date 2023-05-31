set1={100,250,300,1000}
set2={150,250,500,1000}
print("El Set uno seria", set1)
print("El Set 2 es:", set2)
tuple1=tuple(set1)
tuple2=tuple(set2)
tuple1.count(100)

if tuple1.count(100)>=1:
    print("En el primer set se encuentra en digito 100")
else:
    print("El Digito 100 no se encuentra en el set 1")

if tuple2.count(100)>=1:
    print("En el segundo set se encuentra en digito 100")
else:
    print("El Digito 100 no se encuentra en el set 2")

if tuple1.count(500)>=1:
    print("En el primer set se encuentra en digito 500")
else:
    print("El Digito 500 no se encuentra en el set 1")

if tuple1.count(700)>=1:
    print("En el primer set se encuentra en digito 700")
else:
    print("El Digito 700 no se encuentra en el set 1")

if tuple2.count(500)>=1:
    print("En el segundo set se encuentra en digito 500")
else:
    print("El Digito 500 no se encuentra en el set 2")

if tuple2.count(700)>=1:
    print("En el segundo set se encuentra en digito 700")
else:
    print("El Digito 700 no se encuentra en el set 2")

print("El Set 1 con cada uno de sus numeros al cubo seria:", tuple1[0]**3, tuple1[1]**3, tuple1[2]**3, tuple1[3]**3)
print("Los numeros del Set 2 con cada uno de sus numeros al cubo serian:", tuple2[0]**3, tuple2[1]**3, tuple2[2]**3, tuple2[3]**3)
print("La combinacion de ambos sets seria:", tuple1 + tuple2)