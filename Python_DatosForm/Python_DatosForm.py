# 3MLIDTS - BrianAquino-03Python
### Formulario de registro
## Almacenamiento en TXT sin validación 
import tkinter as tk
from tkinter import messagebox
import re

### Definicion de funciones
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
    Telefono = tbTelefono.get()
    Edad = tbEdad.get()
    Estatura = tbEstatura.get()
    ## Obtener el genero de los Radiobuttons
    genero = ""
    if var_genero.get()==1:
        genero = "Hombre"

    elif var_genero.get()==2:
        genero = "Mujer"

    #Validacion de formatos
    if (EnteroValido(Edad)and DecimalValido(Estatura)and TelefonoValido(Telefono)and TextoValido(nombres)and TextoValido(apellidos)):

    #Generar la cadena de caracteres
        datos = "Nombre: "+ nombres +"\n"+"Apellidos: " + apellidos +"\n"+"Telefono: " + Telefono +"\n"+"Edad: " + Edad +"\n"+"Estatura: " + Estatura + "\n"+"Genero: " +genero+"\n" 

    #guardar los datos en un archivo TXT
        with open("C:/Users/briaq/OneDrive/Documents/302024Datos.txt","a") as archivo:
           archivo.write(datos+"\n\n")
        

    #mostrar mensaje de confirmacion
        messagebox.showinfo("Informacion", "Datos guardados con éxito: \n\n" + datos)
        tbNombre.delete(0,tk.END)
        tbApellidos.delete(0,tk.END)
        tbEdad.delete(0,tk.END)
        tbEstatura.delete(0,tk.END)
        tbTelefono.delete(0,tk.END)
        var_genero.set(0)

    else:
        messagebox.showerror("Error", "Algunos de los campos tiene forma invalida")

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

