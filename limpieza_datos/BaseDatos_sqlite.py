import sqlite3
import tkinter as tk
# creación de la base de datos llamada "Datos"
conn = sqlite3.connect('Datos.db')

# creación del cursor de la base de datos para crear querys
C = conn.cursor()
C.execute('''create table if not exists registro_medico(
              nombre varchar(40),
              edad int,
              sexo varchar(9),
              diagnostico varchar(40))''')
#
C.execute('''create table if not exists datos_generales(
             nombre varchar(20),
             apellido varchar(20),
             edad int,
             telefono numeric(10),
             email varchar(20),
             direccion varchar(40))''')

C.execute('''create table if not exists datos_privados(
             nombre varchar(20),
             apellido varchar(20),
             dni numeric(15),
             direccion varchar(40),
             telefono numeric(10),
             email varchar(20))''')

C.execute('''create table if not exists compras(
             nombre varchar(20),
             apellido varchar(20),
             direccion varchar(20),
             ciudad varchar(20),
             telefono numeric(10),
             email varchar(20),
             tarjeta varchar(20))''')

# Creación de la tabla "datos_sensibles"
C.execute('''CREATE TABLE IF NOT EXISTS datos_sensibles(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre VARCHAR(20),
             apellido VARCHAR(20),
             telefono NUMERIC(10),
             email VARCHAR(20),
             diagnostico VARCHAR(40),
             tarjeta VARCHAR(20),
             dni numeric(20)
             )''')


# Función para determinar si un dato es sensible
def es_dato_sensible(datos):
    # Implementa aquí la lógica para determinar si un dato es sensible
    # Puedes usar condiciones, comparaciones, patrones, etc.
    # Devuelve True si es un dato sensible, False si no lo es

    return "*"

# Función para obtener el valor de un campo del formulario
def obtener_valor_del_formulario(campo):
    # Accede al campo del formulario utilizando la biblioteca tkinter
    # y devuelve el valor ingresado por el usuario
    return campo.get()

conn.commit()

