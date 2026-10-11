import tkinter as tk
from tkinter import messagebox, ttk

usuario_default = "ADMIN"
password_default = "ADMIN01"
confirmacion = True

def crear_equipo():

    ventana_crear = tk.Toplevel()
    ventana_crear.geometry("550x400")
    ventana_crear.resizable(False, False)
    ventana_crear.title("Crear Equipo")
    ventana_crear.transient(ventana_principal)
    ventana_crear.grab_set()

    try:
        icono_crear = tk.PhotoImage(file="icono_crear.png")
        ventana_crear.iconphoto(False, icono_crear)
        ventana_crear.icono = icono_crear
    except tk.TclError:
        pass  # si no existe el icono, sigue sin él


    label_titulo = tk.Label(ventana_crear,
                            text="Crear Equipo",
                            font=("Times New Roman", 20, "bold"),)
    label_titulo.place(x=190, y=30)

    label_titulo_codigo = tk.Label(ventana_crear,
                            text="Codigo: ",
                            font=("Times New Roman", 15, "bold" ),)
    label_titulo_codigo.place(x=50, y=100)

    #este label es para que se vaya mostrando el codigo de cada producto
    label_codigo = tk.Label(ventana_crear,
                            text="BN101",
                            font=("Times New Roman", 15, "bold"),
                            fg="#113EF0")
    label_codigo.place(x=135, y=100)

    label_nombre_equipo = tk.Label(ventana_crear,
                                   text="Nombre: ",
                                   font=("Times New Roman", 15, "bold"),)
    label_nombre_equipo.place(x=50, y=160)

    entrada_nombre_equipo = tk.Entry(ventana_crear,
                                     font=("Times New Roman", 13, ""))
    entrada_nombre_equipo.place(x=135, y=161, width=200, height=30)

    label_titulo_tipo = tk.Label(ventana_crear,
                                 text="Tipo: ",
                                 font=("Times New Roman", 15, "bold"),)
    label_titulo_tipo.place(x=50, y=220)

    listbox_tipo = ttk.Combobox(ventana_crear,
                                values=[],
                                font=("Times New Roman", 13),
                                state="readonly")
    listbox_tipo.place(x=135, y=221, width=200, height=30)

    boton_guardar = tk.Button(ventana_crear,
                              text="Guardar",
                              font=("Times New Roman", 15, "bold"),)
    boton_guardar.place(x=90, y=300,width=125, height=50)

    boton_cancelar = tk.Button(ventana_crear,
                               text="Cancelar",
                               font=("Times New Roman", 15, "bold"),)
    boton_cancelar.place(x=320, y=300,width=125, height=50)

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


#login()

if confirmacion:
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("1000x600")
    ventana_principal.resizable(False, False)
    icono_ventana_principal = tk.PhotoImage(file="icono_ventana_principal.png")
    ventana_principal.iconphoto(False, icono_ventana_principal)

    #apartado barra de menu

    barra_principal = tk.Menu(ventana_principal)
    ventana_principal.config(menu=barra_principal)

    menu_opciones_equipo = tk.Menu(barra_principal)
    barra_principal.add_cascade(label="Equipo", menu=menu_opciones_equipo)
    menu_opciones_equipo.add_command(label="Crear", command=crear_equipo)
    menu_opciones_equipo.add_command(label="Editar")
    menu_opciones_equipo.add_command(label="Eliminar")

    menu_opciones_inventario = tk.Menu(barra_principal)
    barra_principal.add_cascade(label="Inventario", menu=menu_opciones_inventario)
    menu_opciones_inventario.add_command(label="Ver Inventario")
    menu_opciones_inventario.add_command(label="Historial Prestamos")

    menu_ayuda = tk.Menu(barra_principal)
    barra_principal.add_cascade(label="Ayuda", menu=menu_ayuda)




    label_bienvenido = tk.Label(ventana_principal,
                                text="!Bienvenido!",
                                font=("Times New Roman", 25, " bold"))
    label_bienvenido.place(x=400, y=30)

    label_nombre_prestamo = tk.Label(ventana_principal,
                                     text="Nombre de estudiante/docente:",
                                     font=("Times New Roman", 14))
    label_nombre_prestamo.place(x=30, y=125)

    entrada_nombre_prestamo = tk.Entry(ventana_principal,
                                       font=("Times New Roman", 13),
                                       relief="solid", bd=1)
    entrada_nombre_prestamo.place(x=270, y=120, width=250, height=32)

    label_carnet = tk.Label(ventana_principal, text="Carnet:",
                            font=("Times New Roman", 14))
    label_carnet.place(x=560, y=125)

    entrada_carnet = tk.Entry(ventana_principal, font=("Times New Roman", 13),
                              relief="solid", bd=1)
    entrada_carnet.place(x=625, y=120, width=250, height=32)

    label_coordinador = tk.Label(ventana_principal, text="Coordinador:",
                                 font=("Times New Roman", 14))
    label_coordinador.place(x=30, y=180)

    entrada_coordinador = tk.Entry(ventana_principal, font=("Times New Roman", 13),
                                   relief="solid", bd=1)
    entrada_coordinador.insert(0, "Lucas Tebalan")
    entrada_coordinador.config(state="readonly") # esto es para que no se pueda modificar el nombre del coordinador
    entrada_coordinador.place(x=165, y=175, width=255, height=32)

    label_tipo = tk.Label(ventana_principal, text="Tipo:",
                          font=("Times New Roman", 14))
    label_tipo.place(x=470, y=180)

    combo_tipo = ttk.Combobox(ventana_principal, values=["Estudiante", "Docente"],
                              state="readonly", font=("Times New Roman", 13))
    combo_tipo.current(0) # esto sirve para que se inicie/vea la primera opcion
    combo_tipo.place(x=520, y=175, width=200, height=32)

    tk.Label(ventana_principal,
             text="Selecciona que desea Prestar: ",
             font=("Times New Roman", 17, "bold"),).place(x=30, y=230)

    opciones_bocina = ttk.Combobox(ventana_principal, values=["bocina"], state="readonly",
                         font=("Times New Roman", 14),
                         )
    opciones_bocina.set("BOCINAS")
    opciones_bocina.place(x=30, y=300, width=300, height=40)

    opciones_portatil = ttk.Combobox(ventana_principal,
                                     values=["portatil"], state="readonly",
                                     font=("Times New Roman", 14),)
    opciones_portatil.set("PORTATIL")
    opciones_portatil.place(x=30, y=380, width=300, height=40)

    opciones_camara = ttk.Combobox(ventana_principal,
                                   values=["camara"], state="readonly",
                                   font=("Times New Roman", 14),)
    opciones_camara.set("CAMARA")
    opciones_camara.place(x=400, y=300, width=300, height=40)

    opciones_proyector = ttk.Combobox(ventana_principal,
                                      values=["proyector"], state="readonly",
                                      font=("Times New Roman", 14),)
    opciones_proyector.set("PROYECTO")
    opciones_proyector.place(x=400, y=380, width=300, height=40)

    #Cuadro del carrito de prestamos y botones de prestamos

    carrito = tk.Canvas(ventana_principal, width=235, height=335,  # canvas sirve para crear formas
                        bg="#DB9927", highlightthickness=5,
                        highlightbackground="black")

    tk.Label(carrito, text="🛒", font=("Segoe UI Emoji", 22),
             bg="#DB9927").place(x=8, y=8)
    tk.Label(carrito, text="Carrito de\nPrestamo:", font=("#DB9927", 11, "bold"),
             bg="#DB9927", justify="left").place(x=62, y=12)
    carrito.place(x=745, y=170)

    boton_prestamo = tk.Button(ventana_principal,
                              text="Guardar \nPrestamo",
                              font=("Times New Roman", 14),
                              bg="#10B251",)
    boton_prestamo.place(x=745, y=525, width=110, height=50)

    boton_limpiar = tk.Button(ventana_principal,
                              text="Limpiar \nCarrito",
                              font=("Times New Roman", 14),
                              bg="#1066B2",)
    boton_limpiar.place(x=875, y=525, width=110, height=50)

    #Apartado de fechas prestamos y devolucion

    label_fecha_prestamo = tk.Label(ventana_principal,
                                    text="Fecha de prestamo",
                                    font=("Times New Roman", 14, " bold"),
                                    )
    label_fecha_prestamo.place(x=80, y=460)

    entrada_fecha_prestamo = tk.Entry(ventana_principal,
                                      font=("Times New Roman", 13))
    entrada_fecha_prestamo.place(x=65, y=490, width=200, height=35)

    label_fecha_devolucion = tk.Label(ventana_principal,
                                      text="Fecha de Devolucion",
                                      font=("Times New Roman", 14, " bold"),
                                    )
    label_fecha_devolucion.place(x=450, y=460)

    entrada_fecha_devolucion = tk.Entry(ventana_principal,
                                        font=("Times New Roman", 13))
    entrada_fecha_devolucion.place(x=435, y=490, width=200, height=35)




    ventana_principal.mainloop()