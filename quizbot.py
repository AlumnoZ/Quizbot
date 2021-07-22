from tkinter import *
from tkinter import messagebox
import quizletautomation as qz
import time
import threading
from selenium.common.exceptions import NoSuchElementException
root = Tk()
user = 'Usuario:'
#root.resizable(width=False, height=False)
root.geometry('480x325')
root.title('Quizbot')
root.configure(bg='#282e3e')
Usuario = Label(root, text='Usuario:',bg='#282e3e',fg='#fff',font=('Arial',15))
Usuario.place(x=180, y=15, anchor="center")
UsuarioE = Entry(root,bg='#646f90',width='25',font=('Arial',10),fg='#fff', relief='flat')
UsuarioE.place(x=140, y=30)
ContraseñaL = Label(root, text='Contraseña:',bg='#282e3e',fg='#fff',font=('Arial',15))
ContraseñaL.place(x=195, y=75, anchor="center")
RecordatorioL = Label(root, text= 'Asegurate de escribir los datos correctamente',bg='#282e3e',fg='#fff',font=('Arial',10))
RecordatorioL.place(x=140, y= 250)
ContraseñaE = Entry(root,bg='#646f90',width='25',font=('Arial',10),fg='#fff', relief='flat')
ContraseñaE.place(x=140, y=90)
NumeroL = Label(root, text='Número de la Lista:',bg='#282e3e',fg='#fff',font=('Arial',15))
NumeroL.place(x=135,y=120)
NumeroE = Entry(root,bg='#646f90',width='25',font=('Arial',10),fg='#fff', relief='flat')
NumeroE.place(x=140, y=150)
NumeroE.insert(0,'Ejemplo: 17')
LinkL = Label(root, text='Link del ejercicio de la lista:',bg='#282e3e',fg='#fff',font=('Arial',15))
LinkL.place(x=135,y=175)
LinkE = Entry(root,bg='#646f90',width='35',font=('Arial',10),fg='#fff', relief='flat')
LinkE.place(x=140, y=210)
LinkE.insert(0,'Ejemplo:https://quizlet.com/000000000/learn')

def Resolver():
    if UsuarioE.get() and ContraseñaE.get() and NumeroE.get() and LinkE.get():
        Boton = Button(root,bg='#c33030', fg='#fff',text='Resolviendo...',font=('Bold',10),relief='flat')
        Boton.place(x=140, y=290)
        qz.SignIn(UsuarioE.get(),ContraseñaE.get(),NumeroE.get())
        time.sleep(3)        
        print('Executed')
        if 'write' in LinkE.get():
            qz.SolveWrite(LinkE.get(),NumeroE.get())
        if 'learn' in LinkE.get():
            qz.SolveLearn(LinkE.get(),NumeroE.get())
        if 'spell' in LinkE.get():
            qz.SolveSpell(LinkE.get(),NumeroE.get())
        else:
            Boton = Button(root,bg='#c33030', fg='#fff',text='Resolver',font=('Bold',10),relief='flat')
            Boton.place(x=140, y=290)
    else:  
        Boton = Button(root,bg='#c33030', fg='#fff',text='Resolver',font=('Bold',10),relief='flat')
        Boton.place(x=140, y=290)
def Recibir():
    th = threading.Thread(target=Resolver)
    th.start()

Boton = Button(root,command=Recibir,bg='#c33030', fg='#fff',text='Resolver',font=('Bold',10),relief='flat')
Boton.place(x=140, y=290)
    
root.mainloop()
