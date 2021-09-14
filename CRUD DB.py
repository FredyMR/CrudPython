from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as MessageBox
import sqlite3

#------- FUNCIONES--------#

def conexionBD():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	try:
			miCursor.execute('''
				CREATE TABLE DATOSUSUARIOS (
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					NOMBRE_USUARIO VARCHAR(50),
					PASSWORD VARCHAR(50),
					APELLIDO VARCHAR(50),
					DIRECCION VARCHAR(50),
					COMENTARIOS VARCHAR(100))
					''')
			messagebox.showinfo("BD", "BD Creada con éxito")

	except:

			messagebox.showwarning("¡Atencion!", "La BD Ya existe")

def salirAplicacion():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
	if valor=="yes":
		root.destroy()

def limpiarCampos():
	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentario.delete(1.0, END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	"""miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+miNombre.get()+"','"+miPass.get()+"', '"+miApellido.get()+"', '"+miDireccion.get()+"','"+textoComentario.get("1.0", END)+"')")"""
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
	miConexion.commit()
	messagebox.showinfo("BD", "Registro insertado con éxito")

def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+miId.get())
	elUsuario=miCursor.fetchall()

	for Usuarios in elUsuario:
		miId.set(Usuarios[0])
		miNombre.set(Usuarios[1])
		miPass.set(Usuarios[2])
		miApellido.set(Usuarios[3])
		miDireccion.set(Usuarios[4])
		textoComentario.insert(1.0,Usuarios[5])
	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	"""miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+
		"',PASSWORD='"+miPass.get() +
		"',APELLIDO='"+miApellido.get() +
		"',DIRECCION='"+miDireccion.get() +
		"',COMENTARIOS='"+textoComentario.get("1.0",END) +
		"' WHERE ID="+miId.get())
		"""
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?" + "WHERE ID=" +miId.get(),(datos))
	miConexion.commit()
	messagebox.showinfo("BD", "Registro actualizado con éxito")


def eliminar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+miId.get())
	miConexion.commit()
	messagebox.showinfo("BD", "Registro borrado con exito")

def test():
    MessageBox.showinfo("Licencia", "Desarrollado Por Fredy May Rodriguez") # título, mensaje



root=Tk()
root.title("Python Con BD")
root.iconbitmap("database.ico")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Pestaña
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

#Pestaña
borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

#Pestaña
CRUDMenu=Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Crear", command=crear)
CRUDMenu.add_command(label="Leer", command=leer)
CRUDMenu.add_command(label="Actualizar", command=actualizar)
CRUDMenu.add_command(label="Borrar", command=eliminar)

#Pestaña
AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia", command=test)
# AyudaMenu.add_command(label="Acerca de:")

barraMenu.add_cascade(label="BD", menu=bbddMenu)
barraMenu.add_cascade(label="BorrarMenu", menu=borrarMenu)
barraMenu.add_cascade(label="CRUDMenu", menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

#---------- COMIENZO DE CAMPOS---------------#

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)
cuadroID.config(justify="right")

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(fg="red", show="*", justify="right")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)
cuadroApellido.config(justify="right")

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)
cuadroDireccion.config(justify="right")

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

#---- COMIENZA LAS ETIQUETAS-----#

idlabel=Label(miFrame, text="ID:")
idlabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombrelabel=Label(miFrame, text="Nombre :")
nombrelabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passlabel=Label(miFrame, text="Contraseña :")
passlabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidolabel=Label(miFrame, text="Apellido :")
apellidolabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionlabel=Label(miFrame, text="Direccion :")
direccionlabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariolabel=Label(miFrame, text="Comentario :")
comentariolabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#------------ BOTONES DE PARTE INFERIOR------------#

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

miFrame3=Frame(root)
miFrame3.pack()

root.mainloop()