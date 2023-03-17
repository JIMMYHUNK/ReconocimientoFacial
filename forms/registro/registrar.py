import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import pymysql
from forms.registro.registrar_designer import FormRegisterDesigner
import util.generic as utl


class Registrar(FormRegisterDesigner):        

    def registros(self):
        bd=pymysql.connect(
            host="localhost",
            user="root",
            passwd="",
            db="bd2"

        )
        fcursor =bd.cursor()

        sql="INSERT INTO login(usuario,contrasena) VALUES ('{0}','{1}')".format(self.usuario.get(),self.password.get())
        if self.usuario.get()== '':
            messagebox.showinfo(message="El usuario se encuentra vacio", title="Aviso")
        elif self.password.get()== '':
            messagebox.showinfo(message="La contraseña se encuentra vacia", title="Aviso")
        elif len(self.password.get())<6:
            messagebox.showinfo(message="La contraseña debe tener al menos 6 caracteres", title="Aviso")
        else:

            try: 
                fcursor.execute(sql)
                bd.commit()
                messagebox.showinfo(message="Registro exitoso",title="Aviso")
            except:
                bd.rollback()

                messagebox.showinfo(message="No Registrado",title="Aviso")
        bd.close()




