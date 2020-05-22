import re
import csv
import os
from clasepia import CONTACTO
conj_contactos=[]
def Cargar_Archivo():
    with open('contactos_mobil.csv') as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter='|')
        contador_lineas = 0
        for linea in lector:
            if contador_lineas == 0:
                print(f'Los nombres de columna son {", ".join(linea)}')
            else:
                objeto_temporal = CONTACTO({linea[0]},{linea[1]},{linea[2]},{linea[3]},{linea[4]},{linea[5]})
                conj_contactos.append(objeto_temporal)
            contador_lineas += 1
    print(f'Procesadas {len(conj_contactos)} líneas.')
    print(f"{len(conj_contactos)} Contactos Cargados")
def Menu_Principal():
    while True:
        LimpiarPantalla = lambda: os.system('cls')
        print("MENU CONTACTOS")
        print("[1] Agregar un contacto")
        print("[2] Buscar un contacto")
        print("[3] Eliminar un contacto")
        print("[4] Mostrar contactos")
        print("[5] Serializar datos")
        print("[0] Salir")
        _resp= int(input("Opcion: "))
        if _resp == 1:
            Agregar_Contacto()
        elif _resp== 2:
            Buscar_Contacto()
        elif _resp== 3:
            Eliminar_Contacto()
        elif _resp== 4:
            Mostrar_Contactos()
        elif _resp == 5:
            Serializar_Contacto()
        elif _resp == 0:
            print("programa finalizado")
            break
        else:
            print("Opcion Invalida\nIntente de nuevo")
def Validar(txt):
    pass
def Agregar_Contacto():
    pass
def Buscar_Contacto():
    pass
def Eliminar_Contacto():
    pass
def Mostrar_Contactos():
    pass
def Serializar_Contacto():
    pass

Cargar_Archivo()
Menu_Principal()
