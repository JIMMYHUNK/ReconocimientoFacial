import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import pymysql
from forms.registro.registrar import Registrar
import util.generic as utl
from forms.master.form_master import MasterPanel
from forms.logins.form_login_designer import FormLoginDesigner

class FormLogin(FormLoginDesigner):

    def verificar(self):
        bd=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="bd2"

        )
        fcursor =bd.cursor()
        fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+self.usuarioLogin.get()+"' and contrasena='"+self.passwordLogin.get()+"'")
        
        
        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de Sesion Correcto",message="Usuario y Contraseña correcta")
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showinfo(title="Inicio de Sesion Incorrecto",message="Usuario y Contraseña Incorrecta")
        bd.close()



    def userRegister(self):
        self.ventana.destroy()
        Registrar()


    def __init__(self):
       super().__init__()