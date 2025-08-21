from tkinter import *
from tkinter import messagebox

#-------------------#
#-----Funciones-----#
#-------------------#

def nacimiento():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("nacimiento")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "¿En donde nacio?  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=160, y=10)

def medico():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Medico")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Sus datos medicos  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=160, y=10)

def familia():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Familia")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Informacion familiar  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=160, y=10)


def educacion():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Educacion")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Su proceso educativo  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=150, y=10)

def amigos():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Amistades")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Sus amistades  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=170, y=10)

def hobbis():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Hobbis")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Sus hobbis  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=190, y=10)

def horario():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Horario")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Su Horario  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=190, y=10)

def icfes():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("ICFES")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "¿Su preparación para el ICFES 2026?  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 15))
    lb_c.place(x=100, y=10)

def futuro():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Su futuro")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Su proyecto de vida al año 2031  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=100, y=10)

def civil():
    global toplevel_centigrados
    toplevel_centigrados = Toplevel()
    toplevel_centigrados.title("Estado civil")
    toplevel_centigrados.resizable(False, False)
    toplevel_centigrados.geometry("500x100")
    toplevel_centigrados.config(bg="darkgray")

    entry_c = Entry(toplevel_centigrados, textvariable=c)
    entry_c.config(bg="darkgray", fg="darkred", font=("Times New Roman", 18), width=40)
    entry_c.focus_set()
    entry_c.place(x=10,y=60)
# etiqueta para valor en centigrados
    lb_c = Label(toplevel_centigrados, text = "Su estado civil  ")
    lb_c.config(bg="darkgray", fg="darkred", font=("Helvetica", 18))
    lb_c.place(x=170, y=10)


c =StringVar


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

subtitulo2 = Label(frame_1, text="Juan pablo duran santos 10-5")
subtitulo2.config(bg="darkgray", fg="red", font=("Arial",15))
subtitulo2.place(x=10,y=10)

frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=980, height=450)
frame_2.place(x=10,y=230)

img_bt_nacimiento = PhotoImage(file="img_identidad.py/mapa-latino.png")
bt_nacimiento = Button(frame_2, image = img_bt_nacimiento, width=125, height=125, command=nacimiento)
bt_nacimiento.place(x=80, y=30)

img_bt_medico = PhotoImage(file="img_identidad.py/medico.png")
bt_medico = Button(frame_2, image = img_bt_medico, width=125, height=125, command=medico)
bt_medico.place(x=260, y=30)

img_bt_familia = PhotoImage(file="img_identidad.py/familia.png")
bt_familia = Button(frame_2, image = img_bt_familia, width=125, height=125, command=familia)
bt_familia.place(x=440, y=30)

img_bt_libro = PhotoImage(file="img_identidad.py/libro.png")
bt_libro = Button(frame_2, image = img_bt_libro, width=125, height=125, command=educacion)
bt_libro.place(x=610, y=30)

img_bt_amigos = PhotoImage(file="img_identidad.py/amigos.png")
bt_amigos = Button(frame_2, image = img_bt_amigos, width=125, height=125, command=amigos)
bt_amigos.place(x=770, y=30)

img_bt_hobbis = PhotoImage(file="img_identidad.py/hobbis.png")
bt_hobbis = Button(frame_2, image = img_bt_hobbis, width=125, height=125, command=hobbis)
bt_hobbis.place(x=80, y=200)

img_bt_reloj = PhotoImage(file="img_identidad.py/reloj.png")
bt_reloj = Button(frame_2, image = img_bt_reloj, width=125, height=125, command=horario)
bt_reloj.place(x=260, y=200)

img_bt_icfes = PhotoImage(file="img_identidad.py/icfes.png")
bt_icfes = Button(frame_2, image = img_bt_icfes, width=125, height=125, command=icfes)
bt_icfes.place(x=440, y=200)

img_bt_2031 = PhotoImage(file="img_identidad.py/2031.png")
bt_2031 = Button(frame_2, image = img_bt_2031, width=125, height=125, command=futuro)
bt_2031.place(x=610, y=200)

img_bt_pareja = PhotoImage(file="img_identidad.py/pareja.png")
bt_pareja = Button(frame_2, image = img_bt_pareja, width=125, height=125, command=civil)
bt_pareja.place(x=770, y=200)

# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()