import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date

usuario_default = "ADMIN"
password_default = "ADMIN01"
confirmacion = True

class Equipo:
    def __init__(self, codigo, tipo, marca, estado):
        self.__codigo = codigo
        self.__tipo = tipo
        self.__marca = marca
        self.__estado = estado
    @property
    def codigo(self):
        return self.__codigo
    @property
    def tipo(self):
        return self.__tipo
    @property
    def marca(self):
        return self.__marca
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
class Historial:
    def __init__(self, equipo, usuario,tipo_usuario, fecha):
        self.__equipo = equipo
        self.__usuario = usuario
        self.__tipo_usuario = tipo_usuario
        self.__fecha = fecha
    @property
    def equipo(self):
        return self.__equipo
    @property
    def usuario(self):
        return self.__usuario
    @property
    def tipo_usuario(self):
        return self.__tipo_usuario
    @property
    def fecha(self):
        return self.__fecha
inventario_equipos = []
codigo_equipo = "BC"
rentas_carrito= []
historial_rentas=[]
actualmente_rentados=[]
texto_carrito = ""
numero_bocinas = 99
numero_camaras = 99
numero_proyectores = 99
numero_portatiles=99

def crear_equipo(ventana, comboCamara, comboProyec, comboBocina, comboCompu):
    global codigo_equipo
    codigo_equipo = "BC"
    valores_marcas = ["JBL", "Bose", "Sony"]
    def al_seleccionar(event):
        global valores_marcas, codigo_equipo
        seleccion = listbox_tipo.get()
        if seleccion == "Bocina":
            valores_marcas = ["JBL", "Bose", "Sony"]
            codigo_equipo = "BC"
        elif seleccion == "Computador portatil":
            valores_marcas = ["DELL", "Lenovo", "HP"]
            codigo_equipo = "CP"
        elif seleccion == "Cámara":
            valores_marcas = ["Canon", "Sony", "Nikon"]
            codigo_equipo = "CM"
        elif seleccion == "Proyector":
            valores_marcas = ["Optoma", "BenQ", "Epson"]
            codigo_equipo = "PY"
        listbox_marca_equipo['values'] = valores_marcas
        listbox_marca_equipo.set('')
        verificar_codigo(seleccion)

    def verificar_codigo(tipo):
        global codigo_equipo
        if tipo == "Bocina":
            codigo_equipo = codigo_equipo + str(numero_bocinas+1)
        elif tipo == "Cámara":
            codigo_equipo = codigo_equipo + str(numero_camaras+1)
        elif tipo == "Computador portatil":
            codigo_equipo = codigo_equipo + str(numero_portatiles+1)
        elif tipo == "Proyector":
            codigo_equipo = codigo_equipo + str(numero_proyectores+1)
        label_codigo.config(text=codigo_equipo)
    def guardar_eqipo():
        global codigo_equipo, numero_bocinas,numero_camaras,numero_proyectores,numero_portatiles
        if listbox_marca_equipo.get() != "":
            equip = Equipo(codigo_equipo, listbox_tipo.get(),listbox_marca_equipo.get(), True)
            inventario_equipos.append(equip)
            if listbox_tipo.get() == "Cámara":
                valores_actuales = list(comboCamara['values'])
                valores_actuales.append(f"{codigo_equipo} | {listbox_marca_equipo.get()} | Disponible")
                comboCamara['values'] = valores_actuales
                numero_camaras+=1
            elif listbox_tipo.get() == "Computador portatil":
                valores_actuales = list(comboCompu['values'])
                valores_actuales.append(f"{codigo_equipo} | {listbox_marca_equipo.get()} | Disponible")
                comboCompu['values'] = valores_actuales
                numero_portatiles+=1
            elif listbox_tipo.get() == "Proyector":
                valores_actuales = list(comboProyec['values'])
                valores_actuales.append(f"{codigo_equipo} | {listbox_marca_equipo.get()} | Disponible")
                comboProyec['values'] = valores_actuales
                numero_proyectores+=1
            elif listbox_tipo.get() == "Bocina":
                valores_actuales = list(comboBocina['values'])
                valores_actuales.append(f"{codigo_equipo} | {listbox_marca_equipo.get()} | Disponible")
                comboBocina['values'] = valores_actuales
                numero_bocinas+=1
            messagebox.showinfo("Registro exitoso",f"El equipo se ha registrado correctamente.\nCódigo: {codigo_equipo}", parent = ventana_crear)
            ventana_crear.destroy()
        else:
            messagebox.showwarning("Error de registro",f"Asegurese de seleccionar la marca.", parent = ventana_crear)

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
                            font=("Times New Roman", 20, "bold"),
                            fg="white",
                            bg="#30A318",
                            relief="flat"
                            )
    label_titulo.place(x=190, y=30)

    label_titulo_codigo = tk.Label(ventana_crear,
                            text="Codigo: ",
                            font=("Times New Roman", 15, "bold" ),)
    label_titulo_codigo.place(x=50, y=100)

    #este label es para que se vaya mostrando el codigo de cada producto
    label_codigo = tk.Label(ventana_crear,
                            text="BC100",
                            font=("Times New Roman", 15, "bold"),
                            fg="#113EF0")
    label_codigo.place(x=135, y=100)

    label_titulo_tipo = tk.Label(ventana_crear,
                                 text="Tipo: ",
                                 font=("Times New Roman", 15, "bold"),)
    label_titulo_tipo.place(x=50, y=160)

    listbox_tipo = ttk.Combobox(ventana_crear,
                                values=["Bocina", "Computador portatil", "Cámara", "Proyector"],
                                font=("Times New Roman", 13),
                                state="readonly")
    listbox_tipo.bind("<<ComboboxSelected>>", al_seleccionar)
    listbox_tipo.place(x=135, y=161, width=200, height=30)
    listbox_tipo.current(0)


    label_marca_equipo = tk.Label(ventana_crear,
                                   text="Marca: ",
                                   font=("Times New Roman", 15, "bold"),)
    label_marca_equipo.place(x=50, y=220)

    listbox_marca_equipo = ttk.Combobox(ventana_crear,
                                values = valores_marcas,
                                font=("Times New Roman", 13, ""),
                                state="readonly")
    listbox_marca_equipo.place(x=135, y=221, width=200, height=30)

    boton_guardar = tk.Button(ventana_crear,
                              text="Guardar",
                              font=("Times New Roman", 15, "bold"),
                              command = guardar_eqipo)
    boton_guardar.place(x=90, y=300,width=125, height=50)

    boton_cancelar = tk.Button(ventana_crear,
                               text="Cancelar",
                               font=("Times New Roman", 15, "bold"),
                               command=ventana_crear.destroy)
    boton_cancelar.place(x=320, y=300,width=125, height=50)

    verificar_codigo(listbox_tipo.get())

def devolver_equipo():
    valores_inventario=[]
    def al_seleccionar(event):
        seleccion = listbox_tipo.get()
        valores_inventario.clear()
        for act in actualmente_rentados:
            if act.tipo == seleccion and act.estado is False:
                valores_inventario.append(f"{act.codigo} | {act.marca} | En uso")
        listbox_equipo['values'] = valores_inventario
        listbox_equipo.set("")
    def confirmar_devolucion():
        codigo = ""
        contador = 0
        equipo_seleccionado = listbox_equipo.get()
        if listbox_equipo.get() != "":
            while contador < 5:
                codigo = codigo + equipo_seleccionado[contador]
                contador += 1
            encontrado = False
            for act in actualmente_rentados:
                if codigo == act.codigo:
                    encontrado = True
                    actualmente_rentados.remove(act)
                    break
            if encontrado:
                for inven in inventario_equipos:
                    if codigo == inven.codigo:
                        inven.estado = True
                resetear_combos_principales()
                messagebox.showinfo("Devolución registrada", "Se ha registrado la devolución del equipo.", parent = ventana_devolver)
                ventana_devolver.destroy()
        else:
            messagebox.showwarning("Error al devolver", "No se ha seleccionado ningún equipo para devolver.", parent = ventana_devolver)

    ventana_devolver = tk.Toplevel()
    ventana_devolver.geometry("550x400")
    ventana_devolver.resizable(False, False)
    ventana_devolver.title("Devolver Equipo")
    ventana_devolver.transient(ventana_principal)
    ventana_devolver.grab_set()

    try:
        icono_devolver = tk.PhotoImage(file="icono_devolver.png")
        ventana_devolver.iconphoto(False, icono_devolver)
        ventana_devolver.icono = icono_devolver
    except tk.TclError:
        pass  # si no existe el icono, sigue sin él


    label_titulo = tk.Label(ventana_devolver,
                            text="Devolver Equipo",
                            font=("Times New Roman", 20, "bold"),
                            fg="white",
                            bg="#CC2B2B",
                            relief="flat"
                            )
    label_titulo.place(x=190, y=30)

    label_titulo_codigo = tk.Label(ventana_devolver,
                            text="Tipo: ",
                            font=("Times New Roman", 15, "bold" ),)
    label_titulo_codigo.place(x=50, y=125)

    listbox_tipo = ttk.Combobox(ventana_devolver,
                                values=["Bocina", "Cámara", "Computador portatil", "Proyector"],
                                font=("Times New Roman", 13),
                                state="readonly")
    listbox_tipo.place(x=135, y=125, width=200, height=30)
    listbox_tipo.bind("<<ComboboxSelected>>", al_seleccionar)

    label_equipo = tk.Label(ventana_devolver,
                            text="Equipo: ",
                            font=("Times New Roman", 15, "bold"),)
    label_equipo.place(x=50, y=205)

    listbox_equipo = ttk.Combobox(ventana_devolver,
                                values=[],
                                font=("Times New Roman", 13),
                                state="readonly")
    listbox_equipo.place(x=135, y=205, width=200, height=30)

    boton_devolver = tk.Button(ventana_devolver,
                              text="Devolver",
                              font=("Times New Roman", 15, "bold"),
                               command= confirmar_devolucion)
    boton_devolver.place(x=115, y=290,width=100, height=50)

    boton_cancelar = tk.Button(ventana_devolver,
                               text="Cancelar",
                               font=("Times New Roman", 15, "bold"),
                               command = ventana_devolver.destroy)
    boton_cancelar.place(x=300, y=290,width=100, height=50)

def eliminar_equipo():
    valores_inventario = []
    def al_seleccionar(event):
        seleccion = listbox_tipo.get()
        valores_inventario.clear()
        for i in inventario_equipos:
            if i.tipo == seleccion:
                if i.estado is False:
                    valores_inventario.append(f"{i.codigo} | {i.marca} | En uso")
                else:
                    valores_inventario.append(f"{i.codigo} | {i.marca} | Disponible")
        listbox_equipo['values'] = valores_inventario
        listbox_equipo.set("")
    def eliminar_del_inventario():
        if listbox_equipo.get() != "":
            codigo = ""
            contador = 0
            equipo_seleccionado = listbox_equipo.get()
            while contador < 5:
                codigo = codigo + equipo_seleccionado[contador]
                contador += 1
            for inv in inventario_equipos:
                if codigo == inv.codigo:
                    inventario_equipos.remove(inv)
                    messagebox.showinfo("Equipo eliminado","El equipo se ha eliminado del inventario correctamente.", parent = ventana_eliminar)
                    ventana_eliminar.destroy()
                    break
        else:
            messagebox.showwarning("Error al eliminar", "No se ha seleccionado el equipo que se desea eliminar.", parent = ventana_eliminar)
        resetear_combos_principales()
        limpiar_prestamo()
    def buscar_para_eliminar():
        if entrada_busqueda.get() != "":
            encontrado = False
            for inv in inventario_equipos:
                if entrada_busqueda.get().upper() == inv.codigo:
                    encontrado = True
                    listbox_tipo.set(inv.tipo)
                    if inv.estado is False:
                        listbox_equipo.set(f"{inv.codigo} | {inv.marca} | En uso")
                    else:
                        listbox_equipo.set(f"{inv.codigo} | {inv.marca} | Disponible")
                    break
            if encontrado is False:
                messagebox.showerror("Error al buscar código", "No se ha encontrado ningún equipo con ese código.",parent=ventana_eliminar)
        else:
            messagebox.showwarning("Error al buscar", "No se ha ingresado ningún código para buscar.", parent = ventana_eliminar)
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.geometry("550x400")
    ventana_eliminar.resizable(False, False)
    ventana_eliminar.title("Eliminar Equipo")
    ventana_eliminar.transient(ventana_principal)
    ventana_eliminar.grab_set()
    try:
        icono_eliminar = tk.PhotoImage(file="icono_eliminar.png")
        ventana_eliminar.iconphoto(False, icono_eliminar)
        ventana_eliminar.icono = icono_eliminar
    except tk.TclError:
        pass  # si no existe el icono, sigue sin él

    label_titulo = tk.Label(ventana_eliminar,
                            text="Eliminar Equipo",
                            font=("Times New Roman", 20, "bold"),
                            fg="white",
                            bg="#F07D28",
                            relief="flat")
    label_titulo.place(x=190, y=30)

    label_titulo_codigo = tk.Label(ventana_eliminar,
                                   text="Tipo: ",
                                   font=("Times New Roman", 15, "bold"), )
    label_titulo_codigo.place(x=50, y=100, )


    listbox_tipo = ttk.Combobox(ventana_eliminar,
                                values=["Bocina", "Cámara", "Computador portatil", "Proyector"],
                                font=("Times New Roman", 13),
                                state="readonly")
    listbox_tipo.place(x=115, y=100, width=235, height=30)
    listbox_tipo.bind("<<ComboboxSelected>>", al_seleccionar)

    label_equipo = tk.Label(ventana_eliminar,
                            text="Seleccione \nEquipo: ",
                            font=("Times New Roman", 12, "bold"),
                            )
    label_equipo.place(x=35,  y=185)

    listbox_equipo = ttk.Combobox(ventana_eliminar,
                                  values=[],
                                  font=("Times New Roman", 13),
                                  state="readonly")
    listbox_equipo.place(x=115, y=190, width=235, height=30)

    boton_filtrar = tk.Button(ventana_eliminar,
                              text="Filtrar",
                              font=("Times New Roman", 15, "bold"), )
    boton_filtrar.place(x=410, y=95, width=85, height=35)

    boton_eliminar = tk.Button(ventana_eliminar,
                               text="Eliminar",
                               font=("Times New Roman", 15, "bold"),
                               command = eliminar_del_inventario)
    boton_eliminar.place(x=410, y=200, width=85, height=35)

    boton_buscar = tk.Button(ventana_eliminar,
                             text="Buscar",
                             font=("Times New Roman", 15, "bold"),
                             command = buscar_para_eliminar)
    boton_buscar.place(x=410, y=315, width=85, height=35)

    label_busqueda = tk.Label(ventana_eliminar,
                              text="Buscar por Codigo: ",
                              font=("Times New Roman", 10, "bold"))
    label_busqueda.place(x=50, y=325 )

    entrada_busqueda = tk.Entry(ventana_eliminar,
                                font=("Times New Roman", 10))
    entrada_busqueda.place(x=165, y=325, width=150)

def ver_inventario():
    posy = 70
    def desplegar(tipo):
        nonlocal posy
        texto_margen = "╔════════════════════════════════════════════╗\n"
        for proy in inventario_equipos:
            if proy.tipo == tipo:
                texto_margen += "║                                                                                                       ║\n"
        texto_margen += "╚════════════════════════════════════════════╝\n"
        label_margen = tk.Label(ventana_inventario, text=texto_margen, font=("arial", 15))
        label_margen.place(x=35, y=posy)
        posy += 25
        for proy in inventario_equipos:
            if proy.tipo == tipo:
                if proy.estado is True:
                    label_info = tk.Label(ventana_inventario,
                                          text=f"{proy.codigo}       | {proy.tipo} {proy.marca}      | Disponible",
                                          font=("arial", 12))
                    label_info.place(x=150, y=posy)
                else:
                    label_info = tk.Label(ventana_inventario,
                                          text=f"{proy.codigo}       | {proy.tipo} {proy.marca}      | En uso",
                                          font=("arial", 12))
                    label_info.place(x=150, y=posy)
                posy += 23
        posy += 30
    ventana_inventario = tk.Toplevel()
    ventana_inventario.geometry("750x750")
    ventana_inventario.resizable(False, False)
    ventana_inventario.title("Inventario")
    ventana_inventario.transient(ventana_principal)
    ventana_inventario.grab_set()

    label_inventario = tk.Label(ventana_inventario,text="Inventario",font=("Times New Roman", 25))
    label_inventario.place(x=300, y=30)
    contador = 0
    desplegado = False
    for inven in inventario_equipos:
        if inven.tipo == "Proyector":
            contador += 1
    if contador>0:
        desplegar("Proyector")
        desplegado = True
    contador = 0
    for inven in inventario_equipos:
        if inven.tipo == "Bocina":
            contador += 1
    if contador>0:
        desplegar("Bocina")
        desplegado = True
    contador = 0
    for inven in inventario_equipos:
        if inven.tipo == "Cámara":
            contador += 1
    if contador>0:
        desplegar("Cámara")
        desplegado = True
    contador = 0
    for inven in inventario_equipos:
        if inven.tipo == "Computador portatil":
            contador += 1
    if contador>0:
        desplegar("Computador portatil")
        desplegado = True
    if desplegado is False:
        messagebox.showwarning("No hay información", "Aún no se ha registrado ningún equipo de ningún tipo.", parent = ventana_inventario)
        ventana_inventario.destroy()

def ver_historial_prestamos():
    posy = 70

    ventana_prestamos = tk.Toplevel()
    ventana_prestamos.geometry("850x750")
    ventana_prestamos.resizable(False, False)
    ventana_prestamos.title("Historial de prestamos")
    ventana_prestamos.transient(ventana_principal)
    ventana_prestamos.grab_set()

    label_inventario = tk.Label(ventana_prestamos, text="Historial de prestamos", font=("Times New Roman", 25))
    label_inventario.place(x=250, y=30)

    if len(historial_rentas)>0:
        texto_margen = "╔═════════════════════════════════════════════════╗\n"
        for hist in historial_rentas:
            texto_margen += "║                                                                                                                   ║\n"
        texto_margen += "╚═════════════════════════════════════════════════╝\n"
        label_margen = tk.Label(ventana_prestamos, text=texto_margen, font=("arial", 15))
        label_margen.place(x=35, y=posy)
        posy += 25
        for hist in reversed(historial_rentas):
            label_info = tk.Label(ventana_prestamos,
                                  text=f"{hist.equipo.codigo}   |   {hist.equipo.tipo} {hist.equipo.marca}   |   {hist.usuario}   |   {hist.tipo_usuario}   |   {hist.fecha}",
                                  font=("arial", 12))
            label_info.place(x=80, y=posy)
            posy += 23
    else:
        messagebox.showwarning("Sin información", "Aún no se ha rentado ningún equipo de ningún tipo.", parent = ventana_prestamos)
        ventana_prestamos.destroy()

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

def agregar_carrito(event):
    global texto_carrito
    combo_activo = event.widget
    contador = 0
    codigo = ""
    seleccion = combo_activo.get()
    while contador < 5:
        codigo = codigo + seleccion[contador]
        contador += 1
    ya_agregado = False
    for ag in rentas_carrito:
        if codigo == ag.codigo:
            messagebox.showwarning("Error al agregar", "Ese equipo ya fué agregado al carrito.")
            ya_agregado = True
            break
    if ya_agregado is False:
        for b in inventario_equipos:
            if codigo == b.codigo and b.estado is True:
                if b.tipo == "Bocina":
                    texto_carrito += f"■ {b.codigo} | Bocina {b.marca}\n"
                elif b.tipo == "Cámara":
                    texto_carrito += f"■ {b.codigo} | Cámara {b.marca}\n"
                elif b.tipo == "Computador portatil":
                    texto_carrito += f"■ {b.codigo} | Portatil {b.marca}\n"
                elif b.tipo == "Proyector":
                    texto_carrito += f"■ {b.codigo} | Proyector {b.marca}\n"
                carrito.itemconfig(producto1, text=texto_carrito)
                rentas_carrito.append(b)
                break
            elif codigo == b.codigo and b.estado is False:
                messagebox.showwarning("Error al agregar al carrito", "El equipo que intenta agregar al carrito ya se encuentra prestado.")
                opciones_bocina.set('BOCINAS')
                opciones_camara.set('CAMARA')
                opciones_proyector.set('PROYECTOR')
                opciones_portatil.set('PORTATIL')
def confirmar_prestamo():
    if len(rentas_carrito) > 0:
        if entrada_nombre_prestamo.get() == "" or  entrada_carnet.get() == "":
            messagebox.showwarning("Falta información", "Asegurese de llenar todos los campos de información")
        else:
            if len(entrada_carnet.get()) == 8:
                for i in inventario_equipos:
                    for r in rentas_carrito:
                        if r.codigo == i.codigo:
                            i.estado = False
                resetear_combos_principales()
                messagebox.showinfo("Prestamo registrado", "Se realizó el registro del prestamo correctamente.")
                for r in rentas_carrito:
                    h = Historial(r,entrada_nombre_prestamo.get(), combo_tipo.get(), date.today().strftime("%d/%m/%Y"))
                    historial_rentas.append(h)
                    actualmente_rentados.append(r)
                limpiar_prestamo()
            else:
                messagebox.showwarning("Dato incompleto", "El carnet debe tener 8 caracteres.")
    else:
        messagebox.showwarning("Falta información", "No se ha agregado ningún elemento al carrito.")
def resetear_combos_principales():
    nuevos_valores = []
    nuevos_valores.clear()
    for i in inventario_equipos:
        if i.tipo == "Bocina" and i.estado is False:
            nuevos_valores.append(f"{i.codigo} | Bocina {i.marca} | En uso")
        elif i.tipo == "Bocina" and i.estado is True:
            nuevos_valores.append(f"{i.codigo} | Bocina {i.marca} | Disponible")
    opciones_bocina['values'] = nuevos_valores
    nuevos_valores.clear()
    for i in inventario_equipos:
        if i.tipo == "Cámara" and i.estado is False:
            nuevos_valores.append(f"{i.codigo} | Cámara {i.marca} | En uso")
        elif i.tipo == "Cámara" and i.estado is True:
            nuevos_valores.append(f"{i.codigo} | Cámara {i.marca} | Disponible")
    opciones_camara['values'] = nuevos_valores
    nuevos_valores.clear()
    for i in inventario_equipos:
        if i.tipo == "Proyector" and i.estado is False:
            nuevos_valores.append(f"{i.codigo} | Proyector {i.marca} | En uso")
        elif i.tipo == "Proyector" and i.estado is True:
            nuevos_valores.append(f"{i.codigo} | Proyector {i.marca} | Disponible")
    opciones_proyector['values'] = nuevos_valores
    nuevos_valores.clear()
    for i in inventario_equipos:
        if i.tipo == "Computador portatil" and i.estado is False:
            nuevos_valores.append(f"{i.codigo} | Portatil {i.marca} | En uso")
        elif i.tipo == "Computador portatil" and i.estado is True:
            nuevos_valores.append(f"{i.codigo} | Portatil {i.marca} | Disponible")
    opciones_portatil['values'] = nuevos_valores
def limpiar_prestamo():
    global texto_carrito
    texto_carrito=""
    carrito.itemconfig(producto1, text="Seleccione un equipo")
    opciones_bocina.set('BOCINAS')
    opciones_camara.set('CAMARA')
    opciones_proyector.set('PROYECTOR')
    opciones_portatil.set('PORTATIL')
    entrada_nombre_prestamo.delete(0, tk.END)
    entrada_carnet.delete(0, tk.END)
    rentas_carrito.clear()

def solo_numeros(texto_nuevo):
  return texto_nuevo == "" or texto_nuevo.isdigit()

if confirmacion:
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("1000x600")
    ventana_principal.resizable(False, False)
    icono_ventana_principal = tk.PhotoImage(file="icono_ventana_principal.png")
    ventana_principal.iconphoto(False, icono_ventana_principal)

    vcmd =ventana_principal.register(solo_numeros)

    #apartado barra de menu

    barra_principal = tk.Menu(ventana_principal)
    ventana_principal.config(menu=barra_principal)

    menu_opciones_equipo = tk.Menu(barra_principal)
    barra_principal.add_cascade(label="Equipo", menu=menu_opciones_equipo)
    menu_opciones_equipo.add_command(label="Crear", command=lambda:crear_equipo(ventana_principal, opciones_camara, opciones_proyector, opciones_bocina, opciones_portatil))
    menu_opciones_equipo.add_command(label="Devolver", command=devolver_equipo)
    menu_opciones_equipo.add_command(label="Eliminar", command=eliminar_equipo)

    menu_opciones_inventario = tk.Menu(barra_principal)
    barra_principal.add_cascade(label="Inventario", menu=menu_opciones_inventario)
    menu_opciones_inventario.add_command(label="Ver Inventario", command = ver_inventario)
    menu_opciones_inventario.add_command(label="Historial Prestamos", command = ver_historial_prestamos)

    menu_ayuda = tk.Menu(barra_principal)
    barra_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

    label_bienvenido = tk.Label(ventana_principal,
                                text="¡Bienvenido!",
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
                              relief="solid", bd=1,validate="key", validatecommand=(vcmd, "%P"))
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

    opciones_bocina = ttk.Combobox(ventana_principal, values=[], state="readonly",
                         font=("Times New Roman", 14),
                         )
    opciones_bocina.set("BOCINAS")
    opciones_bocina.place(x=30, y=300, width=300, height=40)

    opciones_portatil = ttk.Combobox(ventana_principal,
                                     values=[], state="readonly",
                                     font=("Times New Roman", 14),)
    opciones_portatil.set("PORTATIL")
    opciones_portatil.place(x=30, y=380, width=300, height=40)

    opciones_camara = ttk.Combobox(ventana_principal,
                                   values=[], state="readonly",
                                   font=("Times New Roman", 14),)
    opciones_camara.set("CAMARA")
    opciones_camara.place(x=400, y=300, width=300, height=40)

    opciones_proyector = ttk.Combobox(ventana_principal,
                                      values=[], state="readonly",
                                      font=("Times New Roman", 14),)
    opciones_proyector.set("PROYECTOR")
    opciones_proyector.place(x=400, y=380, width=300, height=40)

    opciones_bocina.bind("<<ComboboxSelected>>", agregar_carrito)
    opciones_proyector.bind("<<ComboboxSelected>>", agregar_carrito)
    opciones_camara.bind("<<ComboboxSelected>>", agregar_carrito)
    opciones_portatil.bind("<<ComboboxSelected>>", agregar_carrito)

    #Cuadro del carrito de prestamos y botones de prestamos

    carrito = tk.Canvas(ventana_principal, width=235, height=335,  # canvas sirve para crear formas
                        bg="#DB9927", highlightthickness=5,
                        highlightbackground="black")

    tk.Label(carrito, text="🛒", font=("Segoe UI Emoji", 22),
             bg="#DB9927").place(x=8, y=8)
    tk.Label(carrito, text="Carrito de\nPrestamo:", font=("#DB9927", 11, "bold"),
             bg="#DB9927", justify="left").place(x=62, y=12)
    producto1 = carrito.create_text(110,70,text="Seleccione un equipo",font=("#DB9927", 11, "bold"),anchor = 'n',justify="left")
    carrito.place(x=745, y=170)

    boton_prestamo = tk.Button(ventana_principal,
                              text="Guardar \nPrestamo",
                              font=("Times New Roman", 14),
                              bg="#10B251",
                               command = confirmar_prestamo)
    boton_prestamo.place(x=745, y=525, width=110, height=50)

    boton_limpiar = tk.Button(ventana_principal,
                              text="Limpiar \nCarrito",
                              font=("Times New Roman", 14),
                              bg="#1066B2",
                              command = limpiar_prestamo)
    boton_limpiar.place(x=875, y=525, width=110, height=50)

    #Apartado de fechas prestamos y devolucion

    label_fecha_prestamo = tk.Label(ventana_principal,
                                    text="Fecha de prestamo",
                                    font=("Times New Roman", 14, " bold"),
                                    )
    label_fecha_prestamo.place(x=80, y=460)

    label_fecha_hoy = tk.Label(ventana_principal,
                               text = date.today().strftime("%d/%m/%Y"),
                                      font=("Times New Roman", 13))
    label_fecha_hoy.place(x=65, y=490, width=200, height=35)

    label_fecha_devolucion = tk.Label(ventana_principal,
                                      text="Fecha de Devolucion",
                                      font=("Times New Roman", 14, " bold"),
                                    )
    label_fecha_devolucion.place(x=450, y=460)

    entrada_fecha_devolucion = tk.Entry(ventana_principal,
                                        font=("Times New Roman", 13))
    entrada_fecha_devolucion.place(x=435, y=490, width=200, height=35)

    ventana_principal.mainloop()