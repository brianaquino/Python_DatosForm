import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

### Definicion de funciones
def insertarRegistro(nombres, apellidos,edad, telefono, estatura,genero):
    try: 
        conexion = mysql.connector.connect(
            host = "localhost",
            port = "3306",
            user = "root",
            password = "root",
            database = "practica_7"
            )

        cursor = conexion.cursor()
    #crear el query
        query  = "INSERT INTO registros (Nombre, Apellidos, Edad, Estatura, Telefono,  Genero)" + "VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombres, apellidos, edad, estatura, telefono, genero)
    #ejecucion del query
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("Información", "Datos guardados en la base de datos")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")

def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    var_genero.set(0)
    
def borrar():
    limpiar_campos()

def guardar_valores():
    #obtener valores desde los entrys
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    telefono = tbTelefono.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    ## Obtener el genero de los Radiobuttons
    genero=""
    

    datos = "Nombre: "+ nombres +"\n"+"Apellidos: " + apellidos +"\n"+"Telefono: " + telefono +"\n"+"Edad: " + edad +"\n"+"Estatura: " + estatura + "\n"+"Genero: " + genero+"\n"
    if var_genero.get()==1:
        genero = "Hombre"

    elif var_genero.get()==2:
        genero = "Mujer"
    #Validacion de formatos
    if (EnteroValido(edad)and DecimalValido(estatura)and TelefonoValido(telefono)and TextoValido(nombres)and TextoValido(apellidos)):

    #Generar la cadena de caracteres
        
    #guardar los datos en un archivo TXT
       
        insertarRegistro(nombres, apellidos, edad, telefono, estatura, genero)
        messagebox.showinfo("Informacion", "Datos guardados con exito: \n\n"+ datos)
        limpiar_campos()
        
    #mostrar mensaje de confirmacio

    else:
        messagebox.showerror("Error", "Algunos de los campos tiene forma invalida \n\n" + datos)

#funciones de validacion

def EnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def DecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def TelefonoValido(valor):
    return valor.isdigit() and len(valor)==10
def TextoValido(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

## Creación de ventana
ventana = tk.Tk()
ventana.geometry("720x500")
ventana.title("Formulario Vr.01")
#Crear variable para el Radiobutton
var_genero = tk.IntVar()

## Creación de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres: ")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos: ")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad: ")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()

lbGenero=tk.Label(ventana, text="Genero")
lbGenero.pack()
rbHombre=tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer=tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

## Creacion de botones
btnBorrar=tk.Button(ventana, text="Borrar Datos", command=borrar)
btnBorrar.pack()

btnGuardar=tk.Button(ventana, text="Guardar Datos", command=guardar_valores)
btnGuardar.pack()


ventana.mainloop()
