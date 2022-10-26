import pandas
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import mysql.connector
from NormalizarDatos import Algoritmo
import geocoder

def subirArchivos():
    column = leerArchivo()
    data = Algoritmo(column)
    query = "INSERT INTO bogotabasic (address) VALUES (%s)"
    val = list(data)
    val = [[x] for x in val]
    ejecutarQuery(query, val)

## Leer archivo

def buscarDireccion():
    Tk().withdraw()
    filename = askopenfilename()
    return filename

def leerArchivo():
    filename = buscarDireccion()
    df = pandas.read_csv(filename, engine="python")
    return df['direccion']

## Conexion base

def conexionBase():
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="coordinadora"
    )
    return mydb

def ejecutarQuery(query, val):
    conexion = conexionBase()
    cur = conexion.cursor()
    cur.executemany(query, val)
    conexion.commit()
    conexion.close()

def selectQuery(query):
    conexion = conexionBase()
    cur = conexion.cursor()
    cur.execute(query)
    myresult = cur.fetchall()
    myresult = [x for x in myresult]
    cur.close()
    conexion.commit()
    conexion.close()
    return myresult

def verificarDireccion(direccion):
    query = f"SELECT state FROM bogotadeliveries WHERE address = '{direccion}';"
    res = selectQuery(query)
    if not res:
        print("La direccion no esta registrada en la base de datos")
    elif res[0][0] == "T":
        print("La direccion es valida segun la base de datos")
    elif res[0][0] == "F":
        print("La direccion no es valida segun la base de datos")
    else:
        print("Se ha produccido un error")

def getActualLocation():
    g = geocoder.ip('me')
    print(g.latlng)




##verificarDireccion("Nueva direccion")
##getActualLocation()
#subirArchivos()