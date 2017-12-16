from tkinter import *
from tkinter import messagebox
from Juego import VentanaJuego
import os

#------------------------------------------FUNCIONES---------------------------------------------
def ValidarUsername(usuario):
        #validador del nombre de usuario
        longitud = len(usuario)
        if usuario.isalnum() and longitud >=5 and longitud<=8:
                return True
        else:
                return False
                
def ContarCaracteres(event):
        #minimo y maximo de cantidad de caracteres que el usuario debe de ingresar
        global cajaNombre, color, username, contador, etiquetaContador
        
        longitud = len(username.get())
        restantes = 7- longitud

        if longitud < 4:
                contador.set("Minimo 5 caracteres!!!\nRestantes " +str(restantes))
                color = "red"
                etiquetaContador.configure(fg= color)
                
                
        if longitud >= 4 and longitud <=7:
                contador.set("Rango permitido!!!\nRestantes "+str(restantes))
                color = "green"
                etiquetaContador.configure(fg= color)
                
        if longitud > 7:
                contador.set("Limite excedido!!!")
                color = "red"
                etiquetaContador.configure(fg= color)
                
                cajaNombre.delete(first = 0, last=END)
                

def IrJuego():
        global username, ventana
        if ValidarUsername(username.get()):
                #luego de pedir el usuario e ingresarlo, abrir la ventana de juego
                Usuario()
                ventana.destroy()
                VentanaJuego()
                
        else:
                messagebox.showwarning("Mensaje", "Usuario no valido\nIntente nuevamente")
                cajaNombre.delete(0, END)
                
def Enter(event):
        IrJuego()
        
def Usuario():
        global directorioActual, username
        archivo = open(directorioActual+"\ArchivosTexto\jugador.txt",'w')
        #escririr sobre el directorio el nombre del usuario para que se guarde
        archivo.write(username.get())
        archivo.close()
        
def GuardarVariables():
        global dificultad, fractal
        #funcion que cra las posible alternativas que el usuario elegira
        datoDificultad = "Facil"
        datoFractal = "CuadradoT"
        
        if dificultad.get()== 1:
                datoDificultad = "Facil"
        elif dificultad.get() == 2:
                datoDificultad = "Dificil"
        elif dificultad.get() == 3:
                datoDificultad = "Maestro"
                
        if fractal.get()== 4:
                datoFractal = "CuadradoT"
        elif fractal.get() == 5:
                datoFractal = "RomboCuadrado"
        elif fractal.get() == 6:
                datoFractal = "Copo"
        
        return datoDificultad, datoFractal,
        
def MostrarVariables():
        #funcion para mostrar opciones que el usuario tiene para jugar
        global dificultad, fractal
        
        global rdBFacil, rdBDificil, rdBMaestro, rdBFractal1, rdBFractal2, rdBFractal3
        
        lista = ObtenerConfig()
        datoDificultad = lista[0]
        datoFractal = lista[1]
        
        if datoDificultad== "Facil":
                dificultad = 1
        elif datoDificultad == "Dificil":
                dificultad = 2
        elif datoDificultad == "Maestro":
                dificultad = 3
                
        if datoFractal== "CuadradoT":
                fractal = 4
        elif datoFractal == "RomboCuadrado":
                fractal = 5
        elif datoFractal == "Copo":
                fractal = 6
        
        return dificultad, fractal

def ObtenerConfig():
        global directorioActual
        #crear el directorio como una lista
        lista=[]
        archivo = open(directorioActual+"\ArchivosTexto\configuraciones.txt",'r')
        datos = archivo.readlines()
        for info in datos:
                if info[-1] == "\n":
                        info = info[:-1]
                lista.append(info)
        archivo.close()
        return lista
        
        
def Guardar():
        #abrir la directorio donde se guardara la canfiguracion elegidfa por el usuario
        global directorioActual, root
        #funcion para guardar las opciones que el usuario eligio
        informacion = GuardarVariables()
        #escribir sobre dicho directorio la configuracion deseada
        archivo = open(directorioActual+"\ArchivosTexto\configuraciones.txt",'w')
        archivo.write(informacion[0]+ "\n")
        archivo.write(informacion[1]+ "\n")
        archivo.close()
        
        root.destroy()
        
        
                

#--------------------------------------VENTANA CONFIGURACIONES-----------------------------------------	
def VentanaConfiguracion():
        global root,ventana, colorFondo, colorLetra, colorResultado, fuenteTitulo, fuenteEtiqueta, fuenteTexto, dificultad, fractal, sonido, directorioActual

        global rdBFacil, rdBDificil, rdBMaestro, rdBFractal1, rdBFractal2, rdBFractal3, rdBSi, rdBNo

        #Parametros iniciales de la ventana
        root = Toplevel(ventana)
        root.title("Ventana de Configuraciones")
        root.geometry("400x350+450+150")
        root.configure(background = colorFondo)
        root.iconbitmap(directorioActual+"\Imagenes\FOD.ico")

        # Provoca que la ventana tome el focus
        root.focus_set()
        #Desabilita ventana principal hasta que esta sea destruida
        root.grab_set()
        #Se sobrepone a la principal 
        root.transient(master=ventana)
        
        #Etiquetas de Texto
        etiquetaPuntajes = Label(root, text = "Configuraciones del Juego", bg = colorFondo, fg = colorLetra, font = (fuenteEtiqueta, 14)).place( x = 70, y = 15)
        
        labelDificultad = Label(root, text = "Seleccione dificultad:", bg = colorFondo, fg = "black", font = (fuenteTexto, 11)).place(x= 20, y = 70)
        
        labelFractal = Label(root, text = "Seleccione Fractal:", bg = colorFondo, fg = "black", font = (fuenteTexto, 11)).place(x= 20, y = 140)
		
        l = MostrarVariables()
        l1 = int(l[0])
        l2 = int(l[1])
        
        dificultad = IntVar(value = l1)
        fractal = IntVar(value = l2)
        
        
        #Imagenes de Fractales
        imagenCuadradoT = PhotoImage(file = directorioActual+"\Imagenes\Cuadrado_T.gif")
        imagenCuadradoT= imagenCuadradoT.subsample(4,4)

        imagenRomboCuadrado = PhotoImage(file = directorioActual+"\Imagenes\Rombo_cuadrado.gif")
        imagenRomboCuadrado= imagenRomboCuadrado.subsample(4,4)
                
        imagenCopo = PhotoImage(file = directorioActual+"\Imagenes\Copo.gif")
        imagenCopo= imagenCopo.subsample(4,4)
        
        
        #Opciones dificultad
        rdBFacil= Radiobutton(root, text="Facil",value = 1,variable = dificultad,bg = colorFondo,fg="blue", font=(fuenteTexto, 14)).place(x=50, y=100)
        
        rdBDificil= Radiobutton(root, text="Dificil",value = 2,variable = dificultad,bg = colorFondo,fg="blue", font=(fuenteTexto, 14)).place(x=150, y=100)
        
        rdBMaestro= Radiobutton(root, text="Maestro",value = 3,variable = dificultad,bg = colorFondo,fg="blue", font=(fuenteTexto, 14)).place(x=250, y=100)
        
        #Opciones Fractal
        rdBFractal1= Radiobutton(root, image = imagenCuadradoT,value = 4,variable = fractal,bg = colorFondo)
        rdBFractal1.place(x=20, y=190)
        
        rdBFractal2= Radiobutton(root, image = imagenRomboCuadrado,value = 5,variable = fractal,bg = colorFondo).place(x=140, y=170)
        
        rdBFractal3= Radiobutton(root,image = imagenCopo, value = 6,variable = fractal,bg = colorFondo).place(x=280, y=170)

        
        #Botones
        botonGuardar = Button(root, text = "Guardar y Continuar", command = Guardar, bg = "green" , fg = "white" ,font =(fuenteEtiqueta, 12), activeforeground="blue", cursor="hand2" ).place(x = 200, y = 310)
        
        
        root.mainloop()
        
#--------------------------------------VENTANA DE INICIO-----------------------------------------
def VentanaInicial():
        global ventana,colorFondo, colorLetra, colorResultado, fuenteTitulo, fuenteEtiqueta, fuenteTexto, directorioActual, username, contador, etiquetaContador, cajaNombre
        
        #Parametros iniciales de la ventana
        ventana = Tk()
        ventana.title("Fractal Of Duty v1.0")
        ventana.geometry("700x500+300+100")
        ventana.iconbitmap(directorioActual+"\Imagenes\FOD.ico")
        ventana.minsize(700, 500)
        ventana.maxsize(700, 500)
        ventana.configure(background = colorFondo)

        ventana.resizable(width=True, height=True)

        username = StringVar()
        contador = StringVar()
        
        #CANVAS
        canvas= Canvas(ventana,width=700,height=500)
        canvas.pack()

        #MAIN IMAGES
        mainbg= PhotoImage(file=directorioActual+"\Imagenes\mainbg.png")
        titulo = PhotoImage(file=directorioActual+"\Imagenes\\titulo.png")

        #PLACE THE BG
        fondomain= canvas.create_image(350,250,image=mainbg)
        etiquetaTitulo= canvas.create_image(350,30,image=titulo)

        #Etiquetas
        
        
        etiquetaNombre = Label(ventana, text = "Username: ", bg = "black", fg = "Deep Pink", font = (fuenteEtiqueta, 14)).place( x = 300, y = 315)
        etiquetaContador = Label(ventana, textvariable = contador, bg = "white", fg = color,width=18, font = (fuenteTexto, 11))
        etiquetaContador.place( x = 270, y = 385)

        #Imagen
        
        imagen = PhotoImage(file = directorioActual+"\Imagenes\logo.gif")
        imagen = imagen.subsample(2,2)
        #etiquetaImagen = Label(ventana, image = imagen, bg = "white").place(x =250, y = 85)
        logo= canvas.create_image(350,175,image=imagen)
        
        #Caja de texto
        cajaNombre = Entry(ventana, textvariable = username, font = (fuenteTexto, 12),justify="center", width=14)
        cajaNombre.place(x=280, y= 350)
        cajaNombre.focus()


        cajaNombre.bind("<Key>", ContarCaracteres)
        
        #Boton Jugar
        botonJugar = Button(ventana, text = "Jugar", command = IrJuego, bg = "green" , fg = "white" ,font =(fuenteEtiqueta, 12), activeforeground="blue", cursor="hand2" ).place(x = 230, y = 440)

        #Boton Ir Configuraciones
        botonConfig = Button(ventana, text = "Configuracion", command = VentanaConfiguracion, bg = "green" , fg = "white" ,font =(fuenteEtiqueta, 12), activeforeground="blue", cursor="hand2" ).place(x = 340, y = 440)

        cajaNombre.bind("<Return>", Enter)
        cajaNombre.bind("<Key>", ContarCaracteres)

        ventana.mainloop()
        
#--------------------------------------VARIABLES PREDEFINIDAS-----------------------------------------
#Colores
colorFondo = "#9CEDFD"
colorLetra = "#000000"
color="red"

#Fuentes
fuenteTitulo = "Hobo Std"
fuenteEtiqueta = "Cartoonist"
fuenteTexto = "Comic Sans MS"

ventana = None
root = None
username = None
contador = None
etiquetaContador= None
cajaNombre = None

directorioActual = os.path.dirname(os.path.abspath(__file__))

#configuraciones
dificultad = None
fractal = None
sonido = None

rdBFacil = None
rdBDificil = None
rdBMaestro = None

rdBFractal1= None
rdBFractal2 = None
rdBFractal3 = None

rdBSi = None
rdBNo = None



        

#-----------------------------------------------MAIN--------------------------------------------------

inicio = VentanaInicial()





