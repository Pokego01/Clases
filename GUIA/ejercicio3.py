sueldo_diurno_1 = float(input("¿Cual es el sueldo de dia?"))
sueldo_nocturno_1=float(input("¿Cual es el sueldo de noche?"))
resultado_final =(sueldo_diurno_1*10) + (sueldo_nocturno_1*10)
sueldo_diario_1 = 280000
datos_empleado1 ={
    "turnos_noche":"Lunes, Martes y Miercoles",
    "turnos_dia":"Jueves y Viernes",
    sueldo_diurno_1:12000,
    sueldo_nocturno_1:16000,
    "sueldo diario": resultado_final
}
print("Diccionario inicial:",datos_empleado1)
print(datos_empleado1["turnos_noche"])
print(datos_empleado1["turnos_dia"])
print(datos_empleado1[sueldo_diurno_1])
print(datos_empleado1[sueldo_nocturno_1])

print("Diccionario actualizado:", datos_empleado1)
datos_empleado1["sueldo_semanal_1"] = sueldo_diario_1 * 5
print("Diccionario con el nuevo campo:", datos_empleado1)

sueldo_diurno_2 = float(input("¿Cual es el sueldo de dia?"))
sueldo_nocturno_2 = float(input("¿Cual es el sueldo de noche?"))
resultado_final_2 = (sueldo_diurno_2*10) + (sueldo_nocturno_2*10)
sueldo_diario_2 = 300000
datos_empleado2={
    "turnos_noche2":"Martes,Miercoles,Jueves",
    "turnos_dia2":"Domingo",
    sueldo_diurno_2:12000+2000,
    sueldo_nocturno_2:16000,
    "sueldo_diario2":resultado_final_2
}
print("Diccionario inicial 2:",datos_empleado2)
print(datos_empleado2["turnos_noche2"])
print(datos_empleado2["turnos_dia2"])
print(datos_empleado2[sueldo_diurno_2])
print(datos_empleado2[sueldo_nocturno_2])

print("Diccionario actualizado:",datos_empleado2)
datos_empleado2["sueldo_semanal_2"] = sueldo_diario_2 * 4
print("Diccionario con el nuevo campo:",datos_empleado2)

sueldo_diurno_3 =float(input("¿Cual es el sueldo de dia?"))
sueldo_nocturno_3 =float(input("¿Cual es el sueldo de noche?"))
resultado_final_3 = (sueldo_diurno_3*10) + (sueldo_nocturno_3*10)
sueldo_diario_3 =460000
datos_empleado3={
    "turnos_noche3":"Sabado,Domingo",
    "turnos_dias3":"Miercoles,Jueves,Viernes",
    sueldo_diurno_3 :12000,
    sueldo_nocturno_3 :16000+16000+2000,
    "sueldo_diario":resultado_final_3 
}
print("Diccionario inicial 3",datos_empleado3)
print(datos_empleado3["turnos_noche3"])
print(datos_empleado3["turnos_dias3"])
print(datos_empleado3[sueldo_diurno_3])
print(datos_empleado3[sueldo_nocturno_3])

print("Diccionario actualizado:",datos_empleado3)
datos_empleado3["sueldo_semanal_3"] = sueldo_diario_3*5
print("Diccionario con el nuevo campo",datos_empleado3)