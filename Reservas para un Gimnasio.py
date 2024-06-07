import msvcrt
import os
import csv

def titulo(texto: str):
    print(f"\033[33m{texto.upper()}\033[0m")

def error(texto: str):
    print(f"\033[33m {texto.upper()}\033[0m")

def exito(texto: str):
    print(f"\033[32m {texto.upper()}\033[0m")


clases=[
    ("Pesas","LUN-MIE 8:30-10:00 a.m",10),
    ("Zumba","MAR-JUE 3:30-5.40 p.m",20),
    ("Nutricion","VIE 6:00-7:30 a.m",2),
    ("Crossfit","SAB 11:30-12:55 p.m",10)
]
reservas= []
usuarios= {}
n_usuario= 100
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""
          💪Sistema de Gestión FITLIFE💪
          -----------------------------------------------
          1) Registrar un nuevo usuario.
          2) Reservar una clase
          3) Consultar clases disponibles.
          4) Consultar reservas de un usuario.
          0) Salir del programa
        """)
    opcion= input("Seleccione: ")

    if opcion=="0":
        titulo("Adios")
        break
    elif opcion=="1":
        titulo("Registrar usuario")
        nombre= input("Ingrese nombre de usuario: ").title()
        if nombre not in usuarios.values():
            usuarios[n_usuario]= nombre
            exito(f"Usuario {n_usuario} registrado")
            n_usuario+=100
        else:
            error("Usuario ya registrado")
    elif opcion=="2":
        titulo("Reservar una clase")
        codigo= int(input("Ingrese codigo de usuario: "))
        if codigo in usuarios:
            curso= input("Ingrese curso para inscribir: ").capitalize()
            centinelacurso= False
            centinelacupos= False
            for c in clases:
                if c[0].capitalize()==curso:
                    centinelacurso= True
                    if c[2]>0:
                        centinelacupos= True
                        reservas.append([codigo,usuarios[codigo],c[0],c[1]])
                        exito("Reserva realizada")
                        actualizacioncupo= (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacioncupo)
                        with open('Reporte reservas.csv','w', newline='',encoding='uft-8') as a:
                            escribir= csv.writer(a, delimiter=",")
                            escribir.writerows(reservas)
                        break

            if centinelacurso==False:
                error("No existe el curso")
            if centinelacupos==False:
                error("No existe cupos")
        else:
            error("Codigo no existe")
    elif opcion=="3":
        titulo("Consultar clases disponibles")
        for c in clases:
            print(f"{c[0]} Horario: {c[1]} Cupos: {c[2]}")
    elif opcion=="4":
        titulo("Consultar reservas de un usuario")
        if len(reservas)>0:
            codigo = int(input("Ingrese codigo de usuario: "))
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]} Curso: {r[2]} Horario: {r[3]}")
                    centinela= True
            if centinela== False:
                error("El codigo no tiene reservas asociadas")
    elif opcion=="5":
        titulo("Listado usuarios")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u} : {usuarios[u]}")
    else:
        error("❌ OPCION NO VALIDA ❌")
