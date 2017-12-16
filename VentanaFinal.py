from tkinter import *
from tkinter import messagebox
import os

#------------------------------------------FUNCIONES---------------------------------------------
def MostrarVariables():
        global usuario,puntaje,tiempo
        
        lista = ObtenerConfig()
        usuario = lista[0]
        puntaje = lista[1]
        tiempo = lista[2]
        

def ObtenerConfig():
        global directorioActual
        lista=[]
        #se manda a leer la configuracion elegida por el usuario la cual se guaro en un directorio
        archivo = open(directorioActual+"\\ArchivosTexto\\resultados.txt",'r')
        datos = archivo.readlines()
        for info in datos:
                if info[-1] == "\n":
                        info = info[:-1]
                lista.append(info)
        archivo.close()
        return lista
		
def OrdenarLista(lista):
	#Bucle para determinar cuantas veces vamos a recorrer la lista
	for recorrido in range(1, len(lista)):
		#Bucle para recorrer las posiciones de los elementos 
		for posicion in range(0, len(lista)-recorrido): 	#Cada vez recorra una posicion menos
			
			#Se compara cada elemento con el elemento siguiente para determinar cual es mayor
			if lista[posicion][1] < lista[posicion+1][1]:
				#Si el elemento en el que estamos posicionado es mayor entonces
				#Guardamos este elemento en una variable temporaria
				elemento = lista[posicion]
				#Redefinimos el elemento donde estamos posicionados con el menor
				lista[posicion] = lista[posicion+1]
				#El elemento siguiente es el que almacenamos en la variable temporaria
				lista[posicion+1] = elemento
		#Hacemos esto por cada elemento de la lista, cada vez recorriendo un elemento menos ya que nos hemos asegurado
		#Que los elementos que quedan en las ultimas posiciones son mayores a los demas
		
	#Retornamos la lista ya ordenada
	return lista
	
def CrearTop10():
        #clista donde se guarda los mejores 10 puntajes
	topDiez = []
	
	archivo = open(directorioActual+"\\ArchivosTexto\\Highscore.txt", "r")
	usernames = archivo.readlines()

	for usuario in usernames:
		if usuario[-1] == "\n":
			usuario = usuario[:-1]
	
		userInList = usuario.split(",")
	
		usuarioTemporal = userInList[0],int(userInList[1]),int(userInList[2])
		topDiez.append(usuarioTemporal)

	topDiez = OrdenarLista(topDiez)

	return topDiez
	
def Insert():
        global r
        r.insert(INSERT, "N°\tUsuario\t\tPuntaje\t\tTiempo\n\n")
        lista = CrearTop10()
        for elemento in range(0,10):
                try:
                        r.insert(INSERT, str(elemento+1)+"\t"+str(lista[elemento][0])+"\t\t"+str(lista[elemento][1])+"\t\t"+str(lista[elemento][2])+"\n")
                except:
                        pass
                

def Salir():
        #salir del juego
        global ventana
        ventana.destroy()
        
        
def Enter1(event):
        SalirPuntajes()
        
def SalirPuntajes():
        #salir de la ventana de puntajes
        global root
        root.destroy()

#----------------------------------------VENTANA HIGHSCORE-------------------------------------------	
def IrPuntajes():
        global ventana, directorioActual,root, colorFondo, colorLetra, colorResultado, fuenteTitulo, fuenteEtiqueta, fuenteTexto, r
        
        #Parametros iniciales de la ventana
        root = Toplevel(ventana)
        root.title("Highscore")
        root.geometry("400x400+450+150")
        root.iconbitmap(directorioActual+"\Imagenes\FOD.ico")

        root.configure(background = colorFondo)
        
        # Provoca que la ventana tome el focus
        root.focus_set()
        
        #Desabilita ventana principal hasta que esta sea destruida
        root.grab_set()
        #Se sobrepone a la principal 
        root.transient(master=ventana)
        
        etiquetaTitulo = Label(root, text = "FRACTAL OF DUTY V1.0", bg = colorFondo, fg = colorLetra, font = (fuenteTitulo, 16)).place(x = 75, y = 15)
        
        etiquetaPuntajes = Label(root, text = "Mejores Puntajes", bg = colorFondo, fg = colorLetra, font = (fuenteEtiqueta, 14)).place( x = 100, y = 60)

        r = Text(root, width =48, height=15)
        Insert()
        r.place(x=5, y=100)
        r.config(state =DISABLED)

        
        
		
        botonSalir = Button(root, text = "Salir", command = SalirPuntajes, bg = "green" , fg = "white" ,font =(fuenteEtiqueta, 12), activeforeground="blue", cursor="hand2" ).place(x = 175, y = 350)
        
        root.bind("<Return>", Enter1)
        
        root.mainloop()

#---------------------------------------VENTANA FINAL---------------------------------------------
def VentanaFinal():	
        global ventana,directorioActual ,colorFondo, colorLetra, colorResultado, fuenteTitulo, fuenteEtiqueta, fuenteTexto,usuario,tiempo,puntaje

        #Parametros iniciales de la ventana
        ventana = Tk()
        ventana.title("Fractal of Duty V1.0")
        ventana.geometry("700x500+300+100")
        ventana.minsize(700, 500)
        ventana.maxsize(700, 500)
        ventana.configure(background = colorFondo)
        ventana.iconbitmap(directorioActual+"\Imagenes\FOD.ico")

        #CANVAS
        canvas=Canvas(ventana,width=700,height=500)
        canvas.pack()

        #BG
        bg= PhotoImage(file = directorioActual+"\Imagenes\mainbg.png")
        mainbg= canvas.create_image(350,250,image=bg)

        #TITLE
        title= PhotoImage(file = directorioActual+"\Imagenes\\titulo.png")
        canvas.create_image(350,50,image=title)

        #SCOREBOARD
        canvas.create_rectangle(240,310,450,433,fill="black",outline="black")

        mostrarFinal= MostrarVariables()
        #Etiquetas
        #etiquetaTitulo = Label(ventana, text = "FRACTAL OF DUTY V1.0", bg = colorFondo, fg = colorLetra, font = (fuenteTitulo, 20)).place(x = 180, y = 25)
        etiquetaNombre = Label(ventana, text = "Username: ", bg = "black", fg = "white", font = (fuenteEtiqueta, 14)).place( x = 240, y = 325)
        etiquetaPuntaje = Label(ventana, text = "Puntaje: ", bg = "black", fg = "white", font = (fuenteEtiqueta, 14)).place( x = 255, y = 360)
        etiquetaTiempo = Label(ventana, text = "Tiempo: ", bg = "black", fg = "white", font = (fuenteEtiqueta, 14)).place( x = 255, y = 400)

        resultadoNombre = Label(ventana, text = usuario, bg = "black", fg = colorResultado, font = (fuenteTexto, 14)).place( x = 365, y = 320)
        resultadoPuntaje = Label(ventana, text = puntaje, bg = "black", fg = colorResultado, font = (fuenteTexto, 14)).place( x = 365, y = 360)
        resultadoTiempo= Label(ventana, text = tiempo, bg = "black", fg = colorResultado, font = (fuenteTexto, 14)).place( x = 365, y = 400)

        #Imagen
        directorioActual = os.path.dirname(os.path.abspath(__file__))
        imagen = PhotoImage(file = directorioActual+"\Imagenes\logo.gif")
        imagen = imagen.subsample(2,2)
        #etiquetaImagen = Label(ventana, image = imagen, bg = colorFondo)
        #etiquetaImagen.place(x =250, y = 85)
        logo= canvas.create_image(350,180,image=imagen)


        #Boton Jugar
        botonSalir = Button(ventana, text = "Salir", command = Salir, bg = "green" , fg = "white" ,font =(fuenteEtiqueta, 12), activeforeground="blue", cursor="hand2" ).place(x = 200, y = 440)
        botonHighscore = Button(ventana, text = "Highscore", command = IrPuntajes, bg = "green" , fg = "white" ,font =(fuenteEtiqueta, 12), activeforeground="blue", cursor="hand2" ).place(x = 425, y = 440)
        
        ventana.mainloop()

#--------------------------------------VARIABLES PREDEFINIDAS-----------------------------------------
ventana = None
root = None

#Colores
colorFondo = "#9CEDFD"
colorLetra = "#000000"
colorResultado = "red"

#Para el puntaje
usuario=None
puntaje=None
tiempo=None
#Fuentes
fuenteTitulo = "Hobo Std"
fuenteEtiqueta = "Cartoonist"
fuenteTexto = "Comic Sans MS"
#PATH
directorioActual  = os.path.dirname(os.path.abspath(__file__))

#VentanaFinal()
