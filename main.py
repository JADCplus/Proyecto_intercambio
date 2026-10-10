import tkinter as tk
from tkinter import messagebox

usuario_default = "ADMIN"
password_default = "ADMIN01"
confirmacion = False


def login():
    global confirmacion

    def verificar_datos():
        global confirmacion
        usuario = entrada_usuario.get().strip().upper()
        password = entrada_password.get().upper()

        if usuario != usuario_default or password != password_default:
            messagebox.showerror("Error", "Usuario y/o Contrasena incorrectos",
                                 parent=ventana_login)
            entrada_password.delete(0, tk.END)
        else:
            messagebox.showinfo("Usuario correcto", "Bienvenido",
                                parent=ventana_login)
            confirmacion = True
            ventana_login.destroy()

    ventana_login = tk.Tk()
    ventana_login.title("Login")
    ventana_login.geometry("600x350")
    ventana_login.resizable(False, False)

    try:
        icono_login = tk.PhotoImage(file="icono_login.png")
        ventana_login.iconphoto(False, icono_login)
        ventana_login.icono = icono_login
    except tk.TclError:
        pass  # si no existe el icono, sigue sin él

    label_nombre_usuario = tk.Label(ventana_login,
                                    text="Usuario: ",
                                    font=("Times New Roman", 15))
    label_nombre_usuario.place(x=125, y=75)

    entrada_usuario = tk.Entry(ventana_login,
                               font=("Times New Roman", 15))
    entrada_usuario.place(x=250, y=75)

    label_password = tk.Label(ventana_login,
                              text="Password: ",
                              font=("Times New Roman", 15))
    label_password.place(x=125, y=150)

    entrada_password = tk.Entry(ventana_login,
                                font=("Times New Roman", 15),
                                show="*")
    entrada_password.place(x=250, y=150)

    boton_confirmar = tk.Button(ventana_login,
                                text="Iniciar Sesion",
                                font=("Times New Roman", 15),
                                command=verificar_datos)
    boton_confirmar.place(x=250, y=225)

    boton_cerrar = tk.Button(ventana_login,
                             text="Cerrar",
                             font=("Times New Roman", 15),
                             command=ventana_login.destroy)
    boton_cerrar.place(x=500, y=300)

    entrada_usuario.focus_set()

    ventana_login.mainloop()


login()

if confirmacion:
    ventana_principal = tk.Tk()
    ventana_principal.title("Aplicación")
    ventana_principal.geometry("400x400")

    ventana_principal.mainloop()