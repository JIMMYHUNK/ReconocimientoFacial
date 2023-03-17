import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl

class FormRegisterDesigner:        

    def registros(self):
        pass

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de sesion')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        
        #Frame_logo
        logo = utl.leer_imagen("./imagenes/persona2.png",(200,200))
        frame_logo = tk.Frame(self.ventana,bd=0, width=300, relief=tk.SOLID, padx=10,bg='cornflowerblue')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label = tk.Label(frame_logo,image=logo,bg='cornflowerblue')
        label.place(x=0, y=0,relwidth=1,relheight=1)

        #Frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height=50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro Usuario",font=('Times',30), fg="#666a88", bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        #frame_form_fill 
        frame_form_fill =tk.Frame(frame_form,height=50, bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario =tk.Label(frame_form_fill,text="Usuario", font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times',14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password =tk.Label(frame_form_fill,text="Contraseña", font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times',14),show="*")
        self.password.pack(fill=tk.X, padx=20, pady=10)

        registrar = tk.Button(frame_form_fill,text="Registrar",font=('Times',15,BOLD),bg='darkgoldenrod',bd=0,fg='black',command=self.registros)
        registrar.pack(fill=tk.X,padx=20,pady=20)
        registrar.bind("<Return>",(lambda event: self.registros()))
        self.ventana.mainloop()