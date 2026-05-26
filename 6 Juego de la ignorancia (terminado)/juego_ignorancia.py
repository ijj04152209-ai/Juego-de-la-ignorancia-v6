#Importar librerias necesarias
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
from conceta_BD import *

#Definición de pantalla
pantalla = Tk()
pantalla.withdraw()
pantalla.resizable(1,1)
pantalla.geometry("1200x700")
pantalla.config(background="Black")
pantalla.title("Ignorancia-BD")
pista = Image.open("./im/pista.png")
pista = pista.resize((1200,500))

canvas = Canvas(pantalla, width=1200, height=500, bd=0, highlightthickness=0)
canvas.place(x=0,y=230)
img_pista = ImageTk.PhotoImage(pista)
canvas.create_image(0, 0, image=img_pista, anchor="nw")



seleccion=()
str_preg=StringVar()
str_res1=StringVar()
str_res2=StringVar()
str_res3=StringVar()
str_res4=StringVar()
str_sig=StringVar()
str_anterior = StringVar()
correcto=0
contador_preguntas = 0
x1=10
x2=10
x3=10
x4=10
turno=1
continua=True
gano=''


def recupera_jugadores_juego():
    jugadores = recupera_jugadores()
    
    print("Jugadores registrados:")
    
    for jugador in jugadores:
        print("ID:", jugador[0],
              "Nombre:", jugador[1],
              "Puntos:", jugador[2])

    return jugadores

def tabla_puntos():
    jugadores = recupera_jugadores()

    ventana = Toplevel(pantalla)
    ventana.title("Tabla de jugadores")
    ventana.geometry("400x250")
    ventana.config(bg="#1C1C1C")

    titulo = Label(ventana, text="Tabla de puntos",
    font=("Helvetica",20,"bold"),
    bg="Dark Red",
    fg="Light Grey")

    titulo.pack(pady=10)

    for jugador in jugadores:
        texto = "Jugador: "+str(jugador[1])+"    Puntos: "+str(jugador[2])

        lbl = Label(ventana,
        text=texto,
        font=("Helvetica",18,"bold"),
        bg="Grey",
        fg="Dark Red",
        )

        lbl.pack(pady=5)

def asignar_puntos():
    posiciones = []

    posiciones.append((nombres_jugadores[0], x1))
    posiciones.append((nombres_jugadores[1], x2))
    posiciones.append((nombres_jugadores[2], x3))

    posiciones.sort(key=lambda x:x[1], reverse=True)

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()

    #1er lugar = 3 puntos
    cursor.execute("UPDATE jugadores SET puntos = puntos + 3 WHERE nombre='"+posiciones[0][0]+"'")

    #2do lugar = 2 puntos
    cursor.execute("UPDATE jugadores SET puntos = puntos + 2 WHERE nombre='"+posiciones[1][0]+"'")

    #3er lugar = 1 punto
    cursor.execute("UPDATE jugadores SET puntos = puntos + 1 WHERE nombre='"+posiciones[2][0]+"'")

    conn.commit()
    conn.close()

def avanza_jug():
    global x1, x2, x3, continua
    if turno == 1:
        x1 = x1 + 100
        j1.place(x=x1, y=250)
        if x1 >= 1000:
            mostrar_ganador(nombres_jugadores[0])
    elif turno == 2:
        x2 = x2 + 100
        j2.place(x=x2, y=360)
        if x2 >= 1000:
            mostrar_ganador(nombres_jugadores[1])
    elif turno == 3:
        x3 = x3 + 100
        j3.place(x=x3, y=470)
        if x3 >= 1000:
            mostrar_ganador(nombres_jugadores[2])

def opc1():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==1:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1
    str_sig.set(nombres_jugadores[turno-1])

def opc2():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==2:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1
    str_sig.set(nombres_jugadores[turno-1])

def opc3():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==3:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1
    str_sig.set(nombres_jugadores[turno-1])

def opc4():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==4:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1 
    str_sig.set(nombres_jugadores[turno-1])

def ganador_burro():
    if x4 >= 1000:
        mostrar_ganador("El Burro")

def mostrar_ganador(nombre):
    asignar_puntos()

    ventana = Toplevel(pantalla)
    ventana.title("Fin de la carrera")
    ventana.geometry("450x250")
    ventana.config(bg="gold")
    ventana.resizable(False, False)
    ventana.grab_set()

    mensaje = Label(
        ventana,
        text="🎉 Ganador: " + nombre + " 🎉",
        font=("Helvetica", 22, "bold"),
        bg="gold",
        fg="black"
    )
    mensaje.pack(pady=30)

    pregunta = Label(
        ventana,
        text="¿Quieres iniciar otra carrera?",
        font=("Helvetica", 16, "bold"),
        bg="gold",
        fg="black"
    )
    pregunta.pack(pady=10)

    def otra_carrera():
        global x1, x2, x3, x4, turno, contador_preguntas

        x1 = 10
        x2 = 10
        x3 = 10
        x4 = 10
        turno = 1
        contador_preguntas = 0

        j1.place(x=x1, y=250)
        j2.place(x=x2, y=360)
        j3.place(x=x3, y=470)
        bu.place(x=x4, y=570)

        str_sig.set(nombres_jugadores[0])
        str_preg.set("")
        str_res1.set("")
        str_res2.set("")
        str_res3.set("")
        str_res4.set("")
        str_anterior.set("Pregunta anterior: ")

        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)

        categorias.config(state=NORMAL)

        ventana.destroy()

    def salir():
        ventana.destroy()
        pantalla.quit()

    btn_si = Button(
        ventana,
        text="Sí",
        command=otra_carrera,
        font=("Helvetica", 14, "bold"),
        bg="green",
        fg="white",
        width=10
    )
    btn_si.pack(side=LEFT, padx=80, pady=20)

    btn_no = Button(
        ventana,
        text="No",
        command=salir,
        font=("Helvetica", 14, "bold"),
        bg="red",
        fg="white",
        width=10
    )
    btn_no.pack(side=RIGHT, padx=80, pady=20)

def sel_preg():
    global str_preg
    global correcto
    tam=len(seleccion)
    if tam!=0:
        n = random.randint(0, tam-1)
        #print(n)
        str_preg.set(seleccion[n][1])
        str_res1.set(seleccion[n][2])
        str_res2.set(seleccion[n][3])
        str_res3.set(seleccion[n][4])
        str_res4.set(seleccion[n][5])
        correcto=seleccion[n][6]
        print(correcto)
        r1.config(state=NORMAL)
        r2.config(state=NORMAL)
        r3.config(state=NORMAL)
        r4.config(state=NORMAL)
    else:
        str_preg.set('Categoria sin preguntas')
        str_res1('')
        str_res2('')
        str_res3('')
        str_res4('')
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)

    #pantalla.update()

def preguntas(event):
    global seleccion, contador_preguntas

    cat = categorias.get()
    cat = cat.replace("('", "").replace("',)", "")

    seleccion = recupera_preguntas(cat)
    sel_preg()

    contador_preguntas = 0
    categorias.config(state=DISABLED)

def pregunta_sig():
    global seleccion, contador_preguntas

    if str_preg.get() != "":
        if correcto == 1:
            respuesta_correcta = str_res1.get()
        elif correcto == 2:
            respuesta_correcta = str_res2.get()
        elif correcto == 3:
            respuesta_correcta = str_res3.get()
        elif correcto == 4:
            respuesta_correcta = str_res4.get()

        str_anterior.set(
            "Pregunta anterior: " + str_preg.get() +
            "\nRespuesta correcta: " + respuesta_correcta
        )

    contador_preguntas = contador_preguntas + 1

    cat = categorias.get()
    cat = cat.replace("('", "").replace("',)", "")

    seleccion = recupera_preguntas(cat)
    sel_preg()

    if contador_preguntas >= 8:
        categorias.config(state=NORMAL)
        ventana_cambio = Toplevel(pantalla)
        ventana_cambio.title("Cambio de categoría")
        ventana_cambio.geometry("500x250")
        ventana_cambio.config(bg="Black")
        ventana_cambio.resizable(False, False)

        titulo = Label(
            ventana_cambio,
            text="¡Cambio de categoría!",
            font=("Helvetica", 24, "bold"),
            bg="Black",
            fg="white"
        )

        titulo.pack(pady=20)

        mensaje = Label(
            ventana_cambio,
            text="Ya puedes elegir una nueva categoría",
            font=("Helvetica", 16),
            bg="Black",
            fg="white"
        )

        mensaje.pack(pady=10)

        btn = Button(
            ventana_cambio,
            text="Continuar",
            font=("Helvetica", 14, "bold"),
            bg="Dark Red",
            fg="white",
            width=15,
            command=ventana_cambio.destroy
        )

        btn.pack(pady=30),

        contador_preguntas = 0
    else:
        categorias.config(state=DISABLED)

def pantalla_registro():
    ventana_registro = Toplevel(pantalla)
    ventana_registro.title("Registro de jugadores")
    ventana_registro.geometry("400x300")
    ventana_registro.config(bg="#232B2B")
    ventana_registro.resizable(False, False)
    ventana_registro.grab_set()

    Label(ventana_registro, text="Registrar jugadores", font=("Helvetica", 18, "bold"), bg="Light Gray").pack(pady=15)

    Label(ventana_registro, text="Jugador 1:", bg="Grey", fg="#1502BE",font=("Helvetica", 12, "bold")).pack()
    entrada1 = Entry(ventana_registro, font=("Helvetica", 12))
    entrada1.pack(pady=5)

    Label(ventana_registro, text="Jugador 2:", bg="Grey", fg="#920000",font=("Helvetica", 12, "bold")).pack()
    entrada2 = Entry(ventana_registro, font=("Helvetica", 12))
    entrada2.pack(pady=5)

    Label(ventana_registro, text="Jugador 3:", bg="Gray", font=("Helvetica", 12, "bold")).pack()
    entrada3 = Entry(ventana_registro, font=("Helvetica", 12))
    entrada3.pack(pady=5)

    def guardar():
        global nombres_jugadores

        nombre1 = entrada1.get()
        nombre2 = entrada2.get()
        nombre3 = entrada3.get()

        if nombre1 == "" or nombre2 == "" or nombre3 == "":
            messagebox.showwarning("Aviso", "Debes escribir los nombres de los 3 jugadores")
        else:
            nombres_jugadores = [nombre1, nombre2, nombre3]
            registrar_jugadores(nombre1, nombre2, nombre3)
            str_sig.set(nombres_jugadores[0])
            categorias.config(state=NORMAL)
            ventana_registro.destroy()
            pantalla.deiconify()

    Button(ventana_registro, text="Iniciar juego", command=guardar, font=("Helvetica", 12, "bold"), bg="Green", fg="White").pack(pady=20)

def obtener_pregunta():
    global preguntas_usadas

    preguntas = recupera_preguntas()  # función que ya tienes

    preguntas_disponibles = []

    for pregunta in preguntas:
        id_pregunta = pregunta[0]

        if id_pregunta not in preguntas_usadas:
            preguntas_disponibles.append(pregunta)

    if len(preguntas_disponibles) == 0:
        messagebox.showinfo("Fin", "Ya no hay más preguntas")
        return None

    pregunta_seleccionada = random.choice(preguntas_disponibles)

    preguntas_usadas.append(pregunta_seleccionada[0])

    return pregunta_seleccionada




#
cats=recupera_categoria()
#definir entrada ppara las preguntas
jugadores=recupera_jugadores_juego()
eti = Label(pantalla, bg="Black", fg="White" ,text="Categorias", font='Helvetica 18 bold')
eti.place(x=10, y=10)
categorias=ttk.Combobox(pantalla,font='Helvetica 18 bold')
style = ttk.Style()
style.configure('TCombobox',font='Helvetica 18 bold')
pantalla.option_add('*TCombobox*Listbox.font', ('Helvetica 18 bold'))
categorias['values']=cats
categorias.place(x=150, y=10)
categorias.bind("<<ComboboxSelected>>", preguntas)
categorias.config(state=DISABLED)


sig = Button(pantalla, text="Siguiente", command=pregunta_sig, font='Helvetica 14 bold ',bg="White", fg="Gray")
sig.place(x=800, y=10)

str_sig.set('Jugador 1')
str_jug = Label(pantalla,  bg="Black", fg="White" , textvariable=str_sig, font='Helvetica 18 bold')
str_jug.place(x=500, y=10)

#Definir
eti = Label(pantalla, bg="Black", fg="White" ,text="Pregunta", font='Helvetica 18 bold')
eti.place(x=10, y=60)

str_preg.set("")
pre = Entry(pantalla, textvariable=str_preg, font='Helvetica 14 bold ', bg='Lavender', width=100,state=DISABLED)
pre.place(x=150, y=60)


str_res1.set("")
r1 = Button(pantalla, textvariable=str_res1, command=opc1, font='Helvetica 14 bold ',bg='Dark Red',fg="white",width=20)
r1.place(x=100, y=110)

str_res2.set("")
r2 = Button(pantalla, textvariable=str_res2, command=opc2, font='Helvetica 14 bold ',bg='Dark Red',fg='white',width=20)
r2.place(x=360, y=110)

str_res3.set("")
r3 = Button(pantalla, textvariable=str_res3, command=opc3, font='Helvetica 14 bold ',bg='Dark Red',fg='white',width=20)
r3.place(x=620, y=110)

str_res4.set("")
r4 = Button(pantalla, textvariable=str_res4, command=opc4, font='Helvetica 14 bold ',bg='Dark Red',fg='white',width=20)
r4.place(x=880, y=110)

str_anterior.set("Pregunta anterior: ")

lbl_anterior = Label(
    pantalla,
    textvariable=str_anterior,
    font=("Helvetica", 13, "bold"),
    bg="khaki",
    fg="Black",
    wraplength=1000,
    justify="left"
)
lbl_anterior.place(x=80, y=160)

ju1 = Image.open("./im/Carro 1.png").convert("RGBA")
ju1 = ju1.resize((80,80))
ju1_img = ImageTk.PhotoImage(ju1)
j1 = canvas.create_image(40, 60, image=ju1_img)

ju2 = Image.open("./im/Carro 2.png").convert("RGBA")
ju2 = ju2.resize((80,80))
ju2_img = ImageTk.PhotoImage(ju2)
j2 = canvas.create_image(40, 170, image=ju2_img)

ju3 = Image.open("./im/Carro 3.png").convert("RGBA")
ju3 = ju3.resize((80,80))
ju3_img = ImageTk.PhotoImage(ju3)
j3 = canvas.create_image( 40, 280, image=ju3_img)

bur = Image.open("./im/burro.png").convert("RGBA")
bur = bur.resize((80,80))
bur_img = ImageTk.PhotoImage(bur)
bu = canvas.create_image(40, 390, image=bur_img)

btn_puntos = Button(pantalla, text="Tabla de puntos", command=tabla_puntos,
font='Helvetica 14 bold', bg="Dark Red", fg="White")

btn_puntos.place(x=950, y=10)




pantalla_registro()
pantalla.mainloop()


