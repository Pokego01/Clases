nombre = input("Cual es el nombre del alumno?\n")
asignatura = input("Cual es la asignatura en la que se evaluo?\n")
lab1 = float(input("Cual fue la nota del laboratorio 1?\n"))
lab2 = float(input("Cual fue la nota del laboratorio 2?\n"))
promedio = float(lab1*0.3 + lab2*0.7)
x = {
    "Nombre":nombre,
    "Asignatura":asignatura,
    "Nota Lab,1":lab1,
    "Nota Lab.2":lab2,
    "Promedio":f"{promedio:.1f}"}
print(x)
