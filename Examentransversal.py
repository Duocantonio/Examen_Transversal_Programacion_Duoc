import random
import csv
import os
import time

trabajadores=[["Juan Pérez",random.randint(300000,2500000)],["María García",random.randint(300000,2500000)],
            ["Carlos López",random.randint(300000,2500000)],["Ana Martínez",random.randint(300000,2500000)],
            ["Pedro Rodríguez",random.randint(300000,2500000)],["Laura Hernández",random.randint(300000,2500000)],
            ["Miguel Sánchez",random.randint(300000,2500000)],["Isabel Gómez",random.randint(300000,2500000)],
            ["Francisco Díaz",random.randint(300000,2500000)],["Elena Fernández",random.randint(300000,2500000)]
            ]

def asignarsueldos(trabajadores):
    for i in range(len(trabajadores)):
        print(f"Los trabajadores son: {trabajadores[i][0]} | Su sueldo es de: {trabajadores[i][1]}")
        print("="*40)
    print("Sueldos definido")
def clasificarsueldos(trabajadores):
    for i in range(len(trabajadores)):
        if trabajadores[i][1]<=800000:
            rangos="EL rango de sueldo esta por Debajo de $800000 pesos"
        elif trabajadores[i][1]<2000000:
            rangos="El rango del sueldo esta en Medio de  : $800000 , $2500000 pesos"
        else:
            rangos="El rango del sueldo esta por sobre los $2000000 de pesos"
            
        print(F"Los sueldos | Nombre {trabajadores[i][0]} | Sueldo {trabajadores[i][1]} | Rango de sueldo : {rangos}")    
    
def estadisticas(trabajadores):
    sueldoalto= 1
    for i in range(len(trabajadores)):
        if trabajadores[i][1]>sueldoalto:
            sueldoalto=trabajadores[i][1]
    print(F"El sueldo mas alto es de: ${sueldoalto}")
    
    sueldobajo=2500000
    for i in range(len(trabajadores)):
        if trabajadores[i][1]<sueldobajo:
            sueldobajo=trabajadores[i][1]
    print(F"El sueldo mas bajo es de: ${sueldobajo}")
    
    promedios=0
    for i in range(len(trabajadores)):
        promedios=trabajadores[i][1]+promedios
    promedios=promedios/10
    print(f"El promedio de los sueldos de los trabajadores es de ${promedios}")
    
    geometrica= 1
    for i in range(len(trabajadores)):
        geometrica=trabajadores[i][1]*geometrica
        geometrica=geometrica**(1/len(trabajadores))
    print(F"La media geometrica de los sueldos es: ${geometrica}")



def reporte(trabajadores):
    with open("Reporte de sueldos.csv", "w", newline="",encoding="utf-8") as archive:
        escribidor=csv.writer(archive)
        for i in range(len(trabajadores)):
            print("="*40)
            print(f"Nombre: {trabajadores[i][0]} | Sueldo Bruto: {trabajadores[i][1]}")
            print("="*40)
        time.sleep(2)
        os.system("cls")
        for i in range(len(trabajadores)):
            descuentoAFP=trabajadores[i][1]*0.12
            descuentoSALUD=trabajadores[i][1]*0.07
            sueldoliquido=trabajadores[i][1]-descuentoSALUD-descuentoAFP
            escribidor.writerow({f"Nombre: {trabajadores[i][0]} | El Sueldo Bruto: {trabajadores[i][1]} | Descuentos AFP {descuentoAFP} | Descuentos de salud {descuentoSALUD} | Sueldo liquido {sueldoliquido}"})
            print(f"Nombre: {trabajadores[i][0]} | El Sueldo Bruto: {trabajadores[i][1]} | Descuentos AFP {descuentoAFP} | Descuentos de salud {descuentoSALUD} | Sueldo liquido {sueldoliquido}")
        print("Se ha creado un archivo tipo CSV con el reporte")
    
    
    
    
    
    
while True:
    print("="*50)
    print("1.- Asignar sueldos aleatorios")
    print("2.- Clasificar sueldos")
    print("3.- Ver estadisticas")
    print("4.- Reporte de sueldos")
    print("5.- Salir")
    print("="*50)
    try:
        opc=int(input("Ingrese la opcion que desee: "))
        os.system("cls")
    except ValueError:
        print("Ingrese solo numeros de caracter Entero (1,2,3,4 o 5)")
    match opc:
        case 1:
            asignarsueldos(trabajadores)
        case 2:
            clasificarsueldos(trabajadores)
        case 3:
            estadisticas(trabajadores)
        case 4:
            reporte(trabajadores)
        case 5:
            print("Finalizando programa....")
            print("Programa Hecho por Antonio Vedia")
            print("Rut: 21.979.521-1")
            time.sleep(2)
            break
        case _:
            break