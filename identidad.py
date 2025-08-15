from tkinter import *
from tkinter import messagebox

# -----------------------------
# Ventana principal de la app
# -----------------------------

# Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto de tipo Tk()

ventana_principal = Tk()

# Titulo de la ventana
ventana_principal.title("Tu identidad")

# Tamaño de la ventana
ventana_principal.geometry("1000x1000")

# deshabilitar boton maximizar de la ventana
ventana_principal.resizable(0,0)

#color de fondo de la ventana
ventana_principal.config(bg="gray")

frame_1 = Frame(ventana_principal)
frame_1.config(bg="ivory2", width=980, height=200)
frame_1.place(x=10,y=10)

# Etiqueta para subtitulo 1 de la app
subtitulo1 = Label(frame_1, text="TU IDENTIDAD")
subtitulo1.config(bg="darkgray", fg="darkred", font=("Arial",50))
subtitulo1.place(x=260,y=50)

frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=980, height=450)
frame_2.place(x=10,y=230)

img_bt_nacimiento = PhotoImage(file="img_identidad.py/mapa-latino.png")
bt_nacimiento = Button(frame_2, image = img_bt_nacimiento, width=150, height=150)
bt_nacimiento.place(x=116, y=7)

img_bt_año = PhotoImage(file="img_identidad.py/biberon.png")
bt_año = Button(frame_2, image = img_bt_año, width=150, height=150)
bt_año.place(x=300, y=7)


# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()