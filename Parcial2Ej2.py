N1=float(input("Inscriba las notas del primer alumno\n"))
while N1>7 or N1<1:
        N1=float(input("Inscriba las notas del primer alumno\n"))

N2=float(input("Inscriba las notas del segundo alumno\n"))
while N2>7 or N2<1:
        N2=float(input("Inscriba las notas del segundo alumno\n"))

N3=float(input("Inscriba las notas del tercer alumno\n"))
while N3>7 or N3<1:
        N3=float(input("Inscriba las notas del tercer alumno\n"))

N4=float(input("Inscriba las notas del cuarto alumno\n"))
while N4>7 or N4<1:
        N4=float(input("Inscriba las notas del cuarto alumno\n"))

N5=float(input("Inscriba las notas del quinto alumno\n"))
while N5>7 or N5<1:
        N5=float(input("Inscriba las notas del quinto alumno\n"))

N6=float(input("Inscriba las notas del sexto alumno\n"))
while N6>7 or N6<1:
        N6=float(input("Inscriba las notas del sexto alumno\n"))

N7=float(input("Inscriba las notas del septimo alumno\n"))
while N7>7 or N7<1:
        N7=float(input("Inscriba las notas del septimo alumno\n"))

N8=float(input("Inscriba las notas del octavo alumno\n"))
while N8>7 or N8<1:
        N8=float(input("Inscriba las notas del octavo alumno\n"))
N9=float(input("Inscriba las notas del noveno alumno\n"))
while N9>7 or N9<1:
        N9=float(input("Inscriba las notas del novenoalumno\n"))

N10=float(input("Inscriba las notas del decimo alumno\n"))
while N10>7 or N10<1:
        N10=float(input("Inscriba las notas del Decimo alumno\n"))

Media=N1+N2+N3+N4+N5+N6+N7+N8+N9+N10
print("La media de las notas es:", f"{Media/10:.1f}")

print("Las Siguentes notas Estan sobre la media")
if N1>Media/10:
        print("La nota del alumno 1:", N1)
if N2>Media/10:
        print("La nota del alumno 2:", N2)
if N3>Media/10:
        print("La nota del alumno 3:", N3)
if N4>Media/10:
        print("La nota del alumno 4:", N4)
if N5>Media/10:
        print("La nota del alumno 5:", N5)
if N6>Media/10:
        print("La nota del alumno 6:", N6)
if N7>Media/10:
        print("La nota del alumno 7:", N7)
if N8>Media/10:
        print("La nota del alumno 8:", N8)
if N9>Media/10:
        print("La nota del alumno 9:", N9)
if N10>Media/10:
        print("La nota del alumno 10:", N10)

print("Las Siguentes notas Estan bajo la media")
if N1<Media/10:
        print("La nota del alumno 1:", N1)
if N2<Media/10:
        print("La nota del alumno 2:", N2)
if N3<Media/10:
        print("La nota del alumno 3:", N3)
if N4<Media/10:
        print("La nota del alumno 4:", N4)
if N5<Media/10:
        print("La nota del alumno 5:", N5)
if N6<Media/10:
        print("La nota del alumno 6:", N6)
if N7<Media/10:
        print("La nota del alumno 7:", N7)
if N8<Media/10:
        print("La nota del alumno 8:", N8)
if N9<Media/10:
        print("La nota del alumno 9:", N9)
if N10<Media/10:
        print("La nota del alumno 10:", N10)