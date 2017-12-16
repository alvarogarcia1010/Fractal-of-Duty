from tkinter import *
from VentanaFinal import VentanaFinal
from random import randrange, choice,randint
import os
from math import *

#--------------------------------------------------------------#FUNCTIONS#----------------------------------------------------------------------------------#
#FOR THE RHOMBUS FRACTAL
def rombo_cuadrado(xi,yi,xf,yf,n=3):
    
    if n==0:
        espacioJuego.create_rectangle(xi,yi,xf,yf,fill="#fc4487",outline="black")
    else:
        l=(xf-xi)/4
        k= l*2
        #Primer par 
        p1x=xi+l 
        p1y=yi-k  
        p2x=xf-l
        p2y=yi 
        #Segundo par 
        p3x= xf 
        p3y= yi+l 
        p4x=xf+k  
        p4y=yf-l 
         #Tercer par 
        p5x=xi+l 
        p5y=yf
        p6x=xf-l 
        p6y=yf+k 
          #Ultimo par 
        p7x=xi-k
        p7y=yi+l 
        p8x=xi 
        p8y=yf-l 
            #Crear fractal
        rombo_cuadrado(xi,yi,xf,yf,0)
        rombo_cuadrado(p1x,p1y,p2x,p2y,n-1)
        rombo_cuadrado(p3x,p3y,p4x,p4y,n-1)
        rombo_cuadrado(p5x,p5y,p6x,p6y,n-1)
        rombo_cuadrado(p7x,p7y,p8x,p8y,n-1)
#FRACRTAL CUADRADO T
def cuadrado_T(xi,yi,xf,yf,n=3):
    if n==0:
        espacioJuego.create_rectangle(xi,yi,xf,yf,fill="#27f7a7",outline="black")
    else:
        l= (xf-xi)
        #Primera esquina
        p1x=xi-(l/4)
        p1y=yi-(l/4)
        p2x=xi+(l/4)
        p2y=yi+(l/4)
                        #Segunda esquina
        p3x=xf-(l/4)
        p3y=yi-(l/4)
        p4x=xf+(l/4)
        p4y=yi+(l/4)
                        #Tercera esquina 
        p5x=xi-(l/4)
        p5y=yf-(l/4)
        p6x=xi+(l/4)
        p6y=yf+(l/4)
        #Cuarta esquina
        
        p7x=xf-(l/4)
        p7y=yf-(l/4)
        p8x=xf+(l/4)
        p8y= yf+(l/4)
        #Crear el fractal
        cuadrado_T(xi,yi,xf,yf,0)
        cuadrado_T(p1x,p1y,p2x,p2y,n-1)
        cuadrado_T(p3x,p3y,p4x,p4y,n-1)
        cuadrado_T(p5x,p5y,p6x,p6y,n-1)
        cuadrado_T(p7x,p7y,p8x,p8y,n-1)
#FRACTAL COPO DE NIEVE
def curvaKoch(xi,yi,xf,yf,n):
    if n==0:
        espacioJuego.create_line(xi,yi,xf,yf)
        return 
        
    elif n>0:
        x1= xi+(xf-xi)/3.0
        y1= yi+(yf-yi)/3.0

        x3= xf-(xf-xi)/3.0
        y3= yf-(yf-yi)/3.0

        x2= (x1+x3)*cos(pi/3)-(y3-y1)*sin(pi/3)
        y2= (y1+y3)*cos(pi/3)+(x3-x1)*sin(pi/3)

        curvaKoch(xi,yi,x1,y1,n-1)
        curvaKoch(x1,y1,x2,y2,n-1)
        curvaKoch(x2,y2,x3,y3,n-1)
        curvaKoch(x3,y3,xf,yf,n-1)
        return 
#Creamos una funcion recursiva para generar un copo usando la funcion establecida anteriormente
def copo(x_vertice1,y_vertice1,lado,n):
    #Esta es la posicion inicial del copo
        #x_vertice1=250
        #y_vertice1=380
        #A estas coordenadas se movera luego
        x_vertice2= (lado*cos((2*pi)/3))+x_vertice1
        y_vertice2= (lado*sin((2*pi)/3))+y_vertice1

        x_vertice3= (lado*cos(pi/3))+x_vertice1
        y_vertice3= (lado*sin(pi/3))+y_vertice1

        curvaKoch(x_vertice1,y_vertice1,x_vertice2,y_vertice2,n)
        curvaKoch(x_vertice2,y_vertice2,x_vertice3,y_vertice3,n)
        curvaKoch(x_vertice3,y_vertice3,x_vertice1,y_vertice1,n)

#FUNCTION TO SEE WHAT FRACTAL WILL POP UP
def fractal_choose():
    global figura
    figura= randint(1,1)


#------------------------------------------BURBUJAS Y FRACTAL---------------------------------------------
class RandomBalls:
    #creacion del espacio donde aparecera las burbujas
       
    def __init__(self, canvas):
            self.canvas = canvas
            
    def CreateBalls(self):
        #se escoje un rango al azar para que cada burbuja aparezca
            self.x1 = randrange(750)
            self.y1 = randrange(340)
            self.x2 = self.x1 + 25
            self.y2 = self.y1 + 25
            self.coords = self.x1, self.y1, self.x2, self.y2
            self.color = choice(color)
            self.id=self.canvas.create_oval(self.coords, fill = self.color)
            
            
    def PutBalls(self, cantidad, lista,colores):
        #se agrega las coordenadas de cada burbuja y los colores a listas
        for i in range(0, cantidad):
            self.i = self.CreateBalls()
            lista.append(self.id)
            colores.append(self.color)
            #se busca si hay sobreposicion entre las burbujas y se eliminan de las listas
            #y se vuelven a crear hasta que ya no exista sobreposicion
            if len(self.canvas.find_overlapping(self.coords[0], self.coords[1], self.coords[2], self.coords[3]))>1:
                self.canvas.delete(self.id)
                variable = lista.index(self.id)
                lista.remove(self.id)
                colores.pop(variable)
                self.i = self.CreateBalls()
                lista.append(self.id)
                colores.append(self.color)
                    
        #print(lista)
        #print(colores)

    def overlap(self, canvas,lista,listacolores):
        #funcion para encontrar sobreposicion entre fractal y burbuja y asi hacer desaparecer a la burbuja
            global puntaje
            idBorrar = None
            posicionBorrar = None
            for i in range (0, len(lista)):
                burbuja = canvas.coords(lista[i])
                if len(self.canvas.find_overlapping(burbuja[0], burbuja[1], burbuja[2], burbuja[3]))>1:
                   
                    posicionBorrar = i
                    idBorrar = lista[i]
             #el puntaje obtenido variara dependiendo de el color de las burbujas que se hagan desaparecer                   
            if posicionBorrar != None:
                
                canvas.delete(idBorrar)
                sumarColor = listacolores[posicionBorrar]
                
                #color=["red","Medium Blue","Deep Pink","Lawn Green","yellow"]
                if sumarColor == "red":
                    #print("ROja, 20")
                    #print(sumarColor)
                    m=listacolores.pop(posicionBorrar)
                    puntaje+=2
                elif sumarColor=="Medium Blue":
                    #print("no roja, 0")
                    #print(sumarColor)
                    m=listacolores.pop(posicionBorrar)
                    puntaje+=4
                elif sumarColor=="Lawn Green":
                    #print("no roja, 0")
                    #print(sumarColor)
                    m=listacolores.pop(posicionBorrar)
                    puntaje+=6
                elif sumarColor=="yellow":
                    #print("no roja, 0")
                    #print(sumarColor)
                    m=listacolores.pop(posicionBorrar)
                    puntaje+=8
                elif sumarColor=="Deep Pink":
                    #print("no roja, 0")
                    #print(sumarColor)
                    m=listacolores.pop(posicionBorrar)
                    puntaje+=10
                #print(idBorrar)
                #print(lista)
                #print(listacolores)
                lista.pop(posicionBorrar)
                #print(listacolores)



        
            
class Fractal:
    def __init__(self,id,espacioJuego):
        self.first=id 
        self.espacioJuego= espacioJuego
        self.borders= espacioJuego.create_rectangle(f0-13,442,f3+13,492,fill=None,outline="white")
        self.coords= self.espacioJuego.coords(self.borders)
        
    def validation(self,event):
        global new_coords
        
        x= event.x
        y= event.y

    #VALIDATE RIGHT
        if  (x>=new_coords[2] and x<=new_coords[2]+50):
            if (y>=new_coords[1]and y<=new_coords[3]):
                if CambiarFractal()=="CuadradoT":
                    new=cuadrado_T(new_coords[2]+23,new_coords[1]+13,new_coords[2]+48,new_coords[1]+38,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[2]+10,new_coords[1],new_coords[2]+60,new_coords[1]+50]
                elif CambiarFractal()=="RomboCuadrado":
                    new=rombo_cuadrado(new_coords[2]+23,new_coords[1]+13,new_coords[2]+48,new_coords[1]+38,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[2]+10,new_coords[1],new_coords[2]+60,new_coords[1]+50]
                    
                elif CambiarFractal()=="Copo":
                    new=copo(new_coords[2]+33,new_coords[1],43,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[2]+10,new_coords[1],new_coords[2]+60,new_coords[1]+50]

        #VALIDATE MID
        elif x>=new_coords[0] and x<=new_coords[2]:
            if y<new_coords[1] and y>new_coords[1]-50:
                if CambiarFractal()=="CuadradoT":
                    new=cuadrado_T(new_coords[0]+13,new_coords[1]-48,new_coords[0]+38,new_coords[1]-23,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0],new_coords[1]-60,new_coords[0]+50,new_coords[1]-10]
                elif CambiarFractal()=="RomboCuadrado":
                    new=rombo_cuadrado(new_coords[0]+13,new_coords[1]-48,new_coords[0]+38,new_coords[1]-23,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0],new_coords[1]-60,new_coords[0]+50,new_coords[1]-10]
                elif CambiarFractal()=="Copo":
                    new=copo(new_coords[0]+25,new_coords[1]-60,43,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0],new_coords[1]-60,new_coords[0]+50,new_coords[1]-10]

            #VALIDATE MID DOWN
            elif y>=new_coords[3] and y<=new_coords[3]+50:
                if CambiarFractal()=="CuadradoT":
                    new=cuadrado_T(new_coords[0]+13,new_coords[3]+23,new_coords[0]+38,new_coords[3]+48,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0],new_coords[3]+10,new_coords[0]+50,new_coords[3]+60]
                elif CambiarFractal()=="RomboCuadrado":
                    new=rombo_cuadrado(new_coords[0]+13,new_coords[3]+23,new_coords[0]+38,new_coords[3]+48,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0],new_coords[3]+10,new_coords[0]+50,new_coords[3]+60]
                elif CambiarFractal()=="Copo":
                    new=copo(new_coords[0]+25,new_coords[3]+10,43,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0],new_coords[3]+10,new_coords[0]+50,new_coords[3]+60]

        #VALIDATE LEFT
        elif x<=new_coords[0] and x>=new_coords[0]-50:
            if  (y>=new_coords[1]and y<=new_coords[3]):
                if CambiarFractal()=="CuadradoT":
                    new=cuadrado_T(new_coords[0]-48,new_coords[1]+13,new_coords[0]-23,new_coords[1]+38,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0]-60,new_coords[1],new_coords[0]-10,new_coords[1]+50]
                elif CambiarFractal()=="RomboCuadrado":
                    new=rombo_cuadrado(new_coords[0]-48,new_coords[1]+13,new_coords[0]-23,new_coords[1]+38,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0]-60,new_coords[1],new_coords[0]-10,new_coords[1]+50]
                elif CambiarFractal()=="Copo":
                    new=copo(new_coords[0]-35,new_coords[1],43,n=3)
                    old_coords=new_coords
                    new_coords=[new_coords[0]-60,new_coords[1],new_coords[0]-10,new_coords[1]+50]

#------------------------------------------FUNCIONES---------------------------------------------
def GuardarResultado():
        global directorioActual,puntaje,segundos
        username=NombreUsuario()
        score= puntaje
        
        if Dificultad() == "Facil":
            time = 15-segundos
        elif Dificultad() == "Dificil": 
            time = 25-segundos
        elif Dificultad() == "Maestro": 
            time = 40-segundos
        #dependiendo de la dificultad elegida, el puntaje sera mayor si se elige la dificultad mayor
        
        archivo = open(directorioActual+"\\ArchivosTexto\\resultados.txt",'w')
        archivo.write(username+ "\n")
        archivo.write(str(score)+ "\n")
        archivo.write(str(time)+ "\n")
        archivo.close()
        
def GuardarTop10():
        global directorioActual,puntaje,segundos
        username=NombreUsuario()
        score= puntaje
        
        if Dificultad() == "Facil":
            time = 15-segundos
        elif Dificultad() == "Dificil": 
            time = 25-segundos
        elif Dificultad() == "Maestro": 
            time = 40-segundos
        
        archivo = open(directorioActual+"\\ArchivosTexto\\highscore.txt",'a')
        archivo.write(username+ ",")
        archivo.write(str(score)+ ",")
        archivo.write(str(time)+ "\n")
        archivo.close()     

def ObtenerConfig():
    global directorioActual
    lista=[]
    archivo = open(directorioActual+"\ArchivosTexto\configuraciones.txt",'r')
    datos = archivo.readlines()
    for info in datos:
            if info[-1] == "\n":
                    info = info[:-1]
            lista.append(info)
    archivo.close()
    return lista
 
def PauseGame():
    global playimage,segundos,paused,pausewindow,pausebg
    #pausar el juego

    paused=True
    pausewindow= Toplevel()
    pausewindow.geometry("800x600+275+60")

    pausecanvas= Canvas(pausewindow,bg="black",width=800,height=600)
    pausecanvas.pack(expand=1,fill=BOTH)

    pausecanvasbg=pausecanvas.create_image(400,300,image=pausebg)

    pauseexit= Button(pausecanvas,bg=None,image=playimage,padx=2,pady=2,command=SalirPausa)
    pauseexit.place(x=550,y=490)

    

def SalirPausa():
    global segundos,paused,pausewindow
    paused=False
    Temporizador()
    pausewindow.destroy()
	
def Dificultad():
    lista = ObtenerConfig()
    dificultad = lista[0]
    return dificultad
            
def CambiarFractal():
    # se elige entre los 3 fractales 
    lista = ObtenerConfig()
    fractal = lista[1]
    return fractal

def NombreUsuario():
    #se guarda el nombre de usuario
    global directorioActual
    archivo = open(directorioActual+"\ArchivosTexto\jugador.txt",'r')
    username = archivo.readline()
    archivo.close()
    return username
    
def Temporizador():
    global segundos, tiempo, root, click, paused, idBurbuja
    #se coloca un cronometro el cual varia dependiendo de la dificultad
    
    if paused == False:
        segundos = segundos -1
        if segundos > 0:
            try:
                tiempo["text"] = segundos
                root.after(1000, Temporizador)
            except:
                pass
                    
        elif (segundos == 0):
            try:
                tiempo["text"] = segundos
                saveResult= GuardarResultado()
                saveTop10 = GuardarTop10()
                root.after(700, IrFinal)
            except:
                pass
    else:
            pass
        
def Inicio(event):
    global root, click, espacioJuego,first,new_coords,f0,f1,f3,f4, idBurbuja, idColores,puntaje,labelpuntaje
    burbujas = RandomBalls(espacioJuego)
    #se da inicio al juego con un click
    if click == False:
        root.after(1000, Temporizador)
        if Dificultad() == "Facil":
            burbujas.PutBalls(7, idBurbuja, idColores)
            
                        
        elif Dificultad() == "Dificil":
            burbujas.PutBalls(15, idBurbuja, idColores)
                        
        elif Dificultad() == "Maestro":
            burbujas.PutBalls(25, idBurbuja, idColores)

        click = True
        #print(idBurbuja)
    
        
    elif click==True:
        
        first.validation(event)
        burbujas.overlap(espacioJuego,idBurbuja, idColores)
        labelpuntaje["text"]=puntaje
        if (idBurbuja == []):
            saveResult= GuardarResultado()
            saveTop10 = GuardarTop10()
            root.after(500, IrFinal)
        
        
        
        
                               
def IrFinal():
        global root
        root.destroy()
        VentanaFinal()

#------------------------------------------VENTANA DEL JUEGO--------------------------------------------
def VentanaJuego():
        global tiempo, segundos, root, click, color,first,new_coords,f0,f1,f3,f4
        global espacioJuego, colorFondo, colorLetra, colorResultado, fuenteTitulo, fuenteEtiqueta, fuenteTexto, puntaje,labelpuntaje, pausebg, playimage
        #ventana princiapal 
        root = Tk()
        root.title("Fractal of Duty v1.0")
        root.geometry("800x600+275+60")
        #dimenciones de la ventana de juego y se previene que el usuario intenete agrandar o achicar la ventana
        root.minsize(800, 600)
        root.maxsize(800, 600)
        root.configure(background = colorFondo)
        root.resizable(width=True, height=True)
        root.iconbitmap(directorioActual+"\Imagenes\FOD.ico")


        etiquetaTitulo = Label(root, text = "FRACTAL OF DUTY V1.0", bg = colorFondo, fg = colorLetra, font = (fuenteTitulo, 14)).place(x = 40, y = 25)

        etiquetaNombre = Label(root, text= "Username:", bg = colorFondo, fg = colorLetra, font = (fuenteTexto, 14)).place(x = 500, y = 15)
        
        etiquetaUsername = Label(root, text= NombreUsuario(), bg = colorFondo, fg = "#fff656", font = (fuenteTexto, 14)).place(x = 600, y = 15)
        
        etiquetaDif = Label(root, text= "Dificultad: ", bg = colorFondo, fg = "black", font = (fuenteTexto, 14)).place(x = 40, y = 70)
        
        etiquetaDificultad = Label(root, text= Dificultad(), bg = colorFondo, fg = "#fff656", font = (fuenteTexto, 14)).place(x = 140, y = 70)


        etiquetaTiempo = Label(root,text = "Tiempo" ,bg = colorFondo, fg = colorLetra, font = (fuenteTexto, 14)).place(x = 460, y = 50)
        
        etiquetaPuntaje = Label(root,text = "Puntaje: " ,bg = colorFondo, fg = colorLetra, font = (fuenteTexto, 14)).place(x = 620, y = 50)
        
        espacioJuego = Canvas(root,width=796,height=500,bg="white")
        espacioJuego.place(x=0, y = 100)
        
		        #IMAGENES
        playimage= PhotoImage(file= directorioActual+"\Imagenes\play.png")
        pauseimage= PhotoImage(file= directorioActual+"\Imagenes\pause.png")
        pausebg= PhotoImage(file= directorioActual+"\Imagenes\pausebg.png")

        botonPausa=Button(espacioJuego,image=pauseimage,command=PauseGame)
        botonPausa.place(x=775,y=475)
        
        tiempo = Label(root, text = segundos, bg = colorFondo, fg = "red", font = (fuenteTexto, 14))
        tiempo.place(x = 540, y = 50)

        labelpuntaje = Label(root, text = puntaje, bg = colorFondo, fg = "red", font = (fuenteTexto, 14))
        labelpuntaje.place(x = 700, y = 50)


        


        #CREATING THE FIRST FRACTAL
        if CambiarFractal()== "CuadradoT":
            first=Fractal(cuadrado_T(f0,f1,f3,f4),espacioJuego)
        elif CambiarFractal()== "RomboCuadrado":
            first=Fractal(rombo_cuadrado(f0,f1,f3,f4),espacioJuego)
        elif CambiarFractal()=="Copo":
            first=Fractal(copo(f0+12,f1-13,43,n=3),espacioJuego)
        #se ancla el boton del mouse a el inicio del juego, es decir al hacer click el juego iniciara
        espacioJuego.bind("<Button-1>",Inicio)

    
        new_coords=[f0-13,442,f3+13,492]
        #VALIDATING
        #espacioJuego.bind("<Button-1>",first.validation)
        root.mainloop()


#--------------------------------------VARIABLES PREDEFINIDAS-----------------------------------------	
#STARTING POINTS FOR THE FRACTAL
f0=387
f1=455
f3=f0+25
f4=f1+25

#GLOBAL VARIABLES
figura=None


#Colores
colorFondo = "#6a53c6"
colorLetra = "#000000"
colorResultado = "red"

#Fuentes
fuenteTitulo = "Hobo Std"
fuenteEtiqueta = "Cartoonist"
fuenteTexto = "Comic Sans MS"

directorioActual  = os.path.dirname(os.path.abspath(__file__))

root = None
espacioJuego= None
click = False
tiempo = None
labelpuntaje=None
paused = False

first=None
new_coords=[f0-13,442,f3+13,492]
idBurbuja = []
idColores = []

puntaje = 0

#diferentes dificultadfes y sus tiempos respectivos

if Dificultad() == "Facil":
	segundos = 15
elif Dificultad() == "Dificil": 
	segundos = 25
elif Dificultad() == "Maestro": 
	segundos = 40




color=["red","Medium Blue","Deep Pink","Lawn Green","yellow"]


#VentanaJuego()




        







