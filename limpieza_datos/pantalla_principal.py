import tkinter as tk # Libreria para crear las interfaces
from PIL import ImageTk, Image # Libreria para mostrar imagenes
import os # segunda libreria para llamar las imagenes sin utilizar ruta completa
from tkinter import messagebox, filedialog
import Clases.bd_conection as bd
import Clases.validaciones_campos as valid
import Clases.validaciones_sensibles as sensitivy
import pandas as pd

#
#
#
#************ VENTANA LOGIN *********************************************************************************************************************************
#
#
#
def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario != "" and contrasena != "":
        mysql = bd.MySQLConnector()
        resultado_validacion = mysql.validate_login(usuario, contrasena)

        if resultado_validacion == 1:
            abrir_ventana_principal() #entramos a el sistema
        elif resultado_validacion == 0:
            messagebox.showwarning("Error", "Contraseña incorrecta.")
        elif resultado_validacion == -1:
            messagebox.showwarning("Error", "Usuario inexistente.")
    else:
        messagebox.showwarning("Error", "¡Llene ambos campos antes de iniciar sesion!")

def abrir_ventana_principal():
    # Código para mostrar la ventana principal existente
    ventana_login.destroy()

#cerrar el login
def cerrar_login():
    exit()

#
#
#
#************ LOGIN *********************************************************************************************************************************
#
#
#

# Crear la ventana de inicio de sesión
ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.protocol("WM_DELETE_WINDOW", cerrar_login)
ventana_login.resizable(False, False)

# Configurar tamaño fijo para la ventana
ventana_login.geometry("500x450")

# Cambiar el fondo de la ventana
ventana_login.configure(bg="#a2d2ff")

# Título
titulo_label = tk.Label(ventana_login, text="Iniciar Sesión", font=("Arial", 18), bg="#a2d2ff", fg="black")
titulo_label.pack(pady=10)

# Imagen
# Obtener la ruta del script y el directorio
script_dir = os.path.dirname(os.path.abspath(__file__))
image_filename = "login.png"

# Construir la ruta completa a la imagen
image_path = os.path.join(script_dir, image_filename)
imagen = Image.open(image_path).convert("RGBA")
imagen = imagen.resize((200, 200))  # Ajusta el tamaño de la imagen según tus necesidades
imagen_tk = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(ventana_login, image=imagen_tk, bg="#a2d2ff")
imagen_label.image = imagen_tk  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
imagen_label.pack()

# Crear el marco principal
main_frame = tk.Frame(ventana_login, bg="#a2d2ff")
main_frame.pack(pady=10)

# Etiqueta de usuario
label_usuario = tk.Label(main_frame, text="Usuario:", bg="#a2d2ff", font=("Arial", 12), fg="black")
label_usuario.pack(anchor="center")

# Campo de entrada de usuario
entry_usuario = tk.Entry(main_frame, width=20)
entry_usuario.pack()

# Etiqueta de contraseña
label_contrasena = tk.Label(main_frame, text="Contraseña:", bg="#a2d2ff", font=("Arial", 12), fg="black")
label_contrasena.pack(anchor="center")

# Campo de entrada de contraseña
entry_contrasena = tk.Entry(main_frame, show="*", width=20)
entry_contrasena.pack()

# Botón de inicio de sesión
boton_iniciar_sesion = tk.Button(ventana_login, text="Iniciar Sesión", command=verificar_credenciales, font=("Arial", 11), bg="#0096c7", fg="black")
boton_iniciar_sesion.pack()

# Ejecutar la ventana de inicio de sesión
ventana_login.mainloop()

#
#----------------------------------------------------------------------------------------------------------------------------------
#VENTANA PRINCIPAL
#----------------------------------------------------------------------------------------------------------------------------------
#

# creación de la ventana del menú principal
principal = tk.Tk()
principal.title("Pantalla Principal")
principal.geometry("500x500")  # Ajuste del tamaño de la ventana
principal.resizable(False, False)
principal.protocol("WM_DELETE_WINDOW", lambda: cerrar_pantalla(principal))


# Cambiar el fondo de la ventana principal
principal.configure(bg="#bde0fe")

# Tamaño deseado para las imágenes de los botones (en píxeles)
tamaño_deseado = (60, 60)


# Cargar las imágenes de los botones y redimensionarlas

imagen_registro_medico = Image.open("registros.png")
imagen_registro_medico = imagen_registro_medico.resize(tamaño_deseado)
registro_medico_img = ImageTk.PhotoImage(imagen_registro_medico)

imagen_datos_generales = Image.open("generales.png")
imagen_datos_generales = imagen_datos_generales.resize(tamaño_deseado)
datos_generales_img = ImageTk.PhotoImage(imagen_datos_generales)


imagen_datos_privados = Image.open("privados.png")
imagen_datos_privados = imagen_datos_privados.resize(tamaño_deseado)
datos_privados_img = ImageTk.PhotoImage(imagen_datos_privados)


imagen_compras = Image.open("tarjeta.png")
imagen_compras = imagen_compras.resize(tamaño_deseado)
compras_img = ImageTk.PhotoImage(imagen_compras)


#
#
#
#************ VENTANA REGISTRO MEDICO *********************************************************************************************************************************
#
#
#


# Función para la pantalla de regristro medico
def ventana_pantalla_principal():
    # Lógica para abrir la pantalla principal
    print("Abrir pantalla de registro médico")
    registro_medico_window = tk.Toplevel()
    registro_medico_window.title("Registro Médico")
    registro_medico_window.geometry("500x600")  # Ajusta el tamaño de la ventana
    registro_medico_window.resizable(False, False)  # Establecer tamaño fijo
    registro_medico_window.protocol("WM_DELETE_WINDOW", lambda: cerrar_pantalla(registro_medico_window))

    # Cambiar el fondo de la ventana
    registro_medico_window.configure(bg="#caf0f8")

    # Título
    titulo_label = tk.Label(registro_medico_window, text="Sistema de Registro Médico", font=("Arial", 18), bg="#caf0f8", fg="black")
    titulo_label.pack(pady=10)

    # Imagen
    # Obtener la ruta del script y el directorio
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_filename = "med.jpg"

    # Construir la ruta completa a la imagen
    image_path = os.path.join(script_dir, image_filename)
    imagen = Image.open(image_path)
    imagen = imagen.resize((200, 200))  # Ajusta el tamaño de la imagen según tus necesidades
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(registro_medico_window, image=imagen_tk)
    imagen_label.image = imagen_tk  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
    imagen_label.pack()

    # Crear el marco principal
    main_frame = tk.Frame(registro_medico_window, bg="#caf0f8")
    main_frame.pack(pady=10)

    # Crear los campos de entrada
    campos = [
        ("Nombre:", "nombre_entry"),
        ("Edad:", "edad_entry"),
        ("Sexo:", "sexo_entry"),
        ("Diagnóstico:", "diagnostico_entry"),
    ]

    # Diccionario para almacenar las referencias a los campos de entrada
    entries = {}

    def show_warning(message):
        messagebox.showerror("Error", message)
        registro_medico_window.lift()  # Mantener la ventana de registro médico en primer plano

    for i, (texto, entry_variable) in enumerate(campos):
        label = tk.Label(main_frame, text=texto, bg="#caf0f8", fg="black", font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
        entry = tk.Entry(main_frame, font=("Arial", 12))
        entry.grid(row=i, column=1, padx=10, pady=10)

        entries[entry_variable] = entry

   # Función para guardar los datos de registro médico
    def guardar_datos_registro_medico():
        # Objeto de la clase de validacioens
        s = sensitivy.VerificadorSensibilidad()

        # Obtener los valores de los campos de entrada
        nombre_valor = entries["nombre_entry"].get()
        edad_valor = entries["edad_entry"].get()
        sexo_valor = entries["sexo_entry"].get()
        diagnostico_valor = entries["diagnostico_entry"].get()

        vl = valid.validacionesCampos()

        if vl.validar_registro_medico(nombre_valor, edad_valor, sexo_valor, diagnostico_valor):
            # Insertar los datos en la tabla
            objetomysql = bd.MySQLConnector()
            objetomysql.insercion_registromedico(s.es_sensible(nombre_valor),
                                                 s.es_sensible(edad_valor),
                                                 s.es_sensible(sexo_valor),
                                                 s.es_sensible(diagnostico_valor))

            # Limpiar los campos de entrada
            for e in entries.values():
                e.delete(0, tk.END)

            messagebox.showinfo("Guardar", "Datos guardados exitosamente.")
            registro_medico_window.lift()
        else:
            show_warning(vl.mensaje_error)


    # Asignar la función de guardar_datos_registro_medico al botón de guardar

    guardar_button = tk.Button(registro_medico_window, text="Guardar", command=guardar_datos_registro_medico,
                               font=("Arial", 12), bg="#4C72B0", fg="white")
    guardar_button.pack(pady=10)

    excel_button = tk.Button(registro_medico_window, text="Excel", command=lambda: generar_excel('medico', registro_medico_window),
                               font=("Arial", 12), bg="#4C72B0", fg="white")
    excel_button.pack(pady=10)


#
#
#
#************ VENTANA DATOS GENERALES *********************************************************************************************************************************
#
#
#

# Función para la pantalla de datos generales

def pantalla_principal_datos():
    datos_generales_window = tk.Toplevel()
    datos_generales_window.title("Datos Generales")
    datos_generales_window.geometry("500x650")
    datos_generales_window.resizable(False, False)  # Establecer tamaño fijo
    datos_generales_window.protocol("WM_DELETE_WINDOW", lambda: cerrar_pantalla(datos_generales_window))

    # Cambiar el fondo de la ventana
    datos_generales_window.configure(bg="#003554")

    # Crear el marco principal
    main_frame = tk.Frame(datos_generales_window, bg="#003554")
    main_frame.pack(pady=10)

    # Crear el título "Datos Generales" con tamaño de fuente más grande
    titulo_label = tk.Label(main_frame, text="Datos Generales", bg="#003554", fg="white",
                            font=("Arial", 18, "bold"))
    titulo_label.pack(pady=10)

    # Crear el marco para la imagen
    imagen_frame = tk.Frame(datos_generales_window, bg="#003554")
    imagen_frame.pack(pady=10)

    # Cargar la imagen
    # Obtener la ruta del script y el directorio
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_filename = "gene.jpg"

    # Construir la ruta completa a la imagen
    image_path = os.path.join(script_dir, image_filename)
    imagen = Image.open(image_path)
    imagen = imagen.resize((150, 150))  # Ajusta el tamaño según tus necesidades
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Mostrar la imagen en un widget Label dentro del marco de la imagen
    imagen_label = tk.Label(imagen_frame, image=imagen_tk, bg="#003554")
    imagen_label.image = imagen_tk  # Guardar una referencia para evitar que la imagen se elimine de la memoria
    imagen_label.pack()

    # Crear los campos de entrada con tamaño de fuente más grande y validaciones
    campos_frame = tk.Frame(datos_generales_window, bg="#003554")
    campos_frame.pack(pady=10)

    campos = [
        ("Nombre:", "nombre_entry"),
        ("Apellido:", "apellido_entry"),
        ("Edad:", "edad_entry"),
        ("Teléfono:", "telefono_entry"),
        ("Email:", "email_entry"),
        ("Dirección:", "direccion_entry")
    ]

    def show_warning(message):
        messagebox.showwarning("Advertencia", message)
        datos_generales_window.lift()  # Mantener la ventana de datos generales en primer plano

    entries = {}  # Diccionario para almacenar las referencias a los campos de entrada

    for i, (texto, entry_variable) in enumerate(campos):
        label = tk.Label(campos_frame, text=texto, bg="#003554", fg="white",
                         font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
        entry = tk.Entry(campos_frame, font=("Arial", 12))
        entry.grid(row=i, column=1, padx=10, pady=10)
        # Guardar la referencia a la variable de entrada en el diccionario entries
        entries[entry_variable] = entry


    # Función para guardar los datos de datos generales
    def guardar_datos_datos_generales():
        #Objeto de la clase de validacioens
        s = sensitivy.VerificadorSensibilidad()

        # Obtener los valores de los campos de entrada
        nombre_valor = entries["nombre_entry"].get()
        apellido_valor = entries["apellido_entry"].get()
        edad_valor = entries["edad_entry"].get()
        telefono_valor = entries["telefono_entry"].get()
        email_valor = entries["email_entry"].get()
        direccion_valor = entries["direccion_entry"].get()

        vl = valid.validacionesCampos()

        if vl.validar_datos_generales(nombre_valor, apellido_valor, edad_valor, telefono_valor, email_valor, direccion_valor):
            # Insertar los datos en la tabla
            objetomysql = bd.MySQLConnector()
            objetomysql.insercion_datosgenerales(s.es_sensible(nombre_valor),
                                                 s.es_sensible(apellido_valor),
                                                 s.es_sensible(direccion_valor),
                                                 s.es_sensible(edad_valor),
                                                 s.es_sensible(telefono_valor),
                                                 s.es_sensible(email_valor))

            messagebox.showinfo("Guardar", "Datos guardados exitosamente.")

            # Limpiar los campos de entrada
            for entry in entries.values():
                entry.delete(0, tk.END)

            datos_generales_window.lift()
        else:
            show_warning(vl.mensaje_error)

    def es_dato_sensible(dato):
        # Aquí puedes implementar la lógica para determinar si el dato es sensible o no
        # Por ejemplo, puedes tener una lista de palabras clave sensibles y verificar si alguna de ellas está presente en el dato
        return "*"


    # Asignar la función de guardar_datos_datos_generales al botón de guardar
    guardar_button = tk.Button(datos_generales_window, text="Guardar", command=guardar_datos_datos_generales,
                               font=("Arial", 12), bg="#219ebc", fg="white")
    guardar_button.pack(pady=10)

    excel_button = tk.Button(datos_generales_window, text="Excel",
                             command=lambda: generar_excel('datosgenerales', datos_generales_window),
                             font=("Arial", 12), bg="#4C72B0", fg="white")
    excel_button.pack(pady=10)

#
#
#
#************ VENTANA DATOS PRIVADOS *********************************************************************************************************************************
#
#
#

# Función para la pantalla de datos privados
def pantalla_principal_privados():
    datos_privados_window = tk.Toplevel()
    datos_privados_window.title("Datos Privados")
    datos_privados_window.geometry("500x650")  # Ajusta el tamaño de la ventana
    datos_privados_window.resizable(False, False)  # Establecer tamaño fijo
    datos_privados_window.protocol("WM_DELETE_WINDOW", lambda: cerrar_pantalla(datos_privados_window))

    # Cambiar el fondo de la ventana
    datos_privados_window.configure(bg="#00a6fb")

    # Crear el marco principal
    main_frame = tk.Frame(datos_privados_window, bg="#00a6fb")
    main_frame.pack(pady=10)

    # Crear el título "Datos Privados" con tamaño de fuente más grande
    titulo_label = tk.Label(main_frame, text="Datos Privados", bg="#00a6fb", fg="white",
                            font=("Arial", 18, "bold"))
    titulo_label.pack(pady=10)

    # Crear el marco para los campos de entrada y la imagen
    campos_imagen_frame = tk.Frame(datos_privados_window, bg="#00a6fb")
    campos_imagen_frame.pack(pady=10)

    # Cargar la imagen
    # Obtener la ruta del script y el directorio
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_filename = "dat.jpg"

    # Construir la ruta completa a la imagen
    image_path = os.path.join(script_dir, image_filename)
    imagen = Image.open(image_path)
    imagen = imagen.resize((200, 150))  # Ajusta el tamaño según tus necesidades
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Mostrar la imagen en un widget Label dentro del marco de la imagen
    imagen_label = tk.Label(campos_imagen_frame, image=imagen_tk, bg="#00a6fb")
    imagen_label.image = imagen_tk  # Guardar una referencia para evitar que la imagen se elimine de la memoria
    imagen_label.pack()

    # Crear el marco para los campos de entrada
    campos_frame = tk.Frame(campos_imagen_frame, bg="#00a6fb")
    campos_frame.pack(pady=10)

    # Crear los campos de entrada
    campos = [
        ("Nombre:", "nombre_entry"),
        ("Apellido:", "apellido_entry"),
        ("DNI:", "dni_entry"),
        ("Dirección:", "direccion_entry"),
        ("Teléfono:", "telefono_entry"),
        ("Email:", "email_entry"),
    ]

    # Diccionario para almacenar las referencias a los campos de entrada
    entries = {}

    def show_warning(message):
        messagebox.showwarning("Advertencia", message)
        datos_privados_window.lift()  # Mantener la ventana de datos privados en primer plano

    for i, (texto, entry_variable) in enumerate(campos):
        label = tk.Label(campos_frame, text=texto, bg="#00a6fb", fg="white",
                         font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
        entry = tk.Entry(campos_frame, font=("Arial", 12))
        entry.grid(row=i, column=1, padx=10, pady=10)
        # Guardar la referencia a la variable de entrada en el diccionario entries
        entries[entry_variable] = entry

    # Establecer un estilo para el botón
    boton_privados = {"font": ("Arial", 10), "bg": "#00a6fb", "fg": "Black", "width": 90}

    # Función para guardar los datos
    def guardar_datos():
        # Objeto de la clase de validacioens
        s = sensitivy.VerificadorSensibilidad()

        # Obtener los valores de los campos de entrada
        nombre_valor = entries["nombre_entry"].get()
        apellido_valor = entries["apellido_entry"].get()
        dni_valor = entries["dni_entry"].get()
        direccion_valor = entries["direccion_entry"].get()
        telefono_valor = entries["telefono_entry"].get()
        email_valor = entries["email_entry"].get()

        vl = valid.validacionesCampos()

        if vl.validar_registro_datos_privados(nombre_valor, apellido_valor, dni_valor, direccion_valor, telefono_valor, email_valor):
            # Insertar los datos en la tabla
            objetomysql=bd.MySQLConnector()
            objetomysql.insercion_datosprivados(s.es_sensible(nombre_valor),
                                                s.es_sensible(apellido_valor),
                                                s.es_sensible(f"{dni_valor}"),
                                                s.es_sensible(direccion_valor),
                                                s.es_sensible(telefono_valor),
                                                s.es_sensible(email_valor))

            # Limpiar los campos de entrada
            for e in entries.values():
                e.delete(0, tk.END)

            messagebox.showinfo("Guardar", "Datos guardados exitosamente.")
            datos_privados_window.lift()
        else:
            show_warning(vl.mensaje_error)


    # Asignar la función de guardar_datos al botón de guardar
    guardar_button = tk.Button(datos_privados_window, text="Guardar", command=guardar_datos,
                               font=("Arial", 12), bg="#ffafcc", fg="black")
    guardar_button.pack(pady=10)

    excel_button = tk.Button(datos_privados_window, text="Excel",
                             command=lambda: generar_excel('datosprivados', datos_privados_window),
                             font=("Arial", 12), bg="#4C72B0", fg="white")
    excel_button.pack(pady=10)

#
#
#
#************ VENTANA COMPRAS *********************************************************************************************************************************
#
#
#
def pantalla_principal_compras():
    compras_window = tk.Toplevel()
    compras_window.title("Compras")
    compras_window.geometry("500x650")  # Ajusta el tamaño de la ventana
    compras_window.resizable(False, False)  # Establecer tamaño fijo
    compras_window.protocol("WM_DELETE_WINDOW", lambda: cerrar_pantalla(compras_window))

    # Cambiar el fondo de la ventana
    compras_window.configure(bg="#006494")

    # Crear el marco principal
    main_frame = tk.Frame(compras_window, bg="#006494")
    main_frame.pack(pady=10)

    # Título
    titulo_label = tk.Label(main_frame, text="Sistema de Compras", font=("Arial", 18), bg="#006494", fg="white")
    titulo_label.pack()

    # Cargar la imagen
    # Obtener la ruta del script y el directorio
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_filename = "compras.png"

    # Construir la ruta completa a la imagen
    image_path = os.path.join(script_dir, image_filename)
    imagen = Image.open(image_path)
    imagen = imagen.resize((150, 150))  # Ajusta el tamaño según tus necesidades
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Mostrar la imagen en un widget Label
    imagen_label = tk.Label(main_frame, image=imagen_tk, bg="#006494")
    imagen_label.image = imagen_tk  # Guardar una referencia para evitar que la imagen se elimine de la memoria
    imagen_label.pack()

    # Crear el marco para los campos de entrada
    campos_frame = tk.Frame(main_frame, bg="#006494")
    campos_frame.pack(pady=10)

    # Crear los campos de entrada
    campos = [
        ("Nombre:", "nombre_entry"),
        ("Apellido:", "apellido_entry"),
        ("Dirección:", "direccion_entry"),
        ("Ciudad:", "ciudad_entry"),
        ("Teléfono:", "telefono_entry"),
        ("Email:", "email_entry"),
        ("Tarjeta de Crédito:", "tarjeta_entry"),
    ]

    # Diccionario para almacenar las referencias a los campos de entrada
    entries = {}

    def show_warning(message):
        messagebox.showwarning("Advertencia", message)
        compras_window.lift()  # Mantener la ventana de compras en primer plano

    for i, (texto, entry_variable) in enumerate(campos):
        label = tk.Label(campos_frame, text=texto, bg="#006494", fg="white",
                         font=("Arial", 12))
        label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
        entry = tk.Entry(campos_frame, font=("Arial", 12))
        entry.grid(row=i, column=1, padx=10, pady=10)
        # Guardar la referencia a la variable de entrada en el diccionario entries
        entries[entry_variable] = entry

    # Establecer un estilo para el botón
    boton_compras = {"font": ("Arial", 10), "bg": "#cbf3f0", "fg": "Black", "width": 90}

    # Función para guardar los datos
    def guardar_datos():
        # Objeto de la clase de validacioens
        s = sensitivy.VerificadorSensibilidad()

        # Obtener los valores de los campos de entrada
        nombre_valor = entries["nombre_entry"].get()
        apellido_valor = entries["apellido_entry"].get()
        direccion_valor = entries["direccion_entry"].get()
        ciudad_valor = entries["ciudad_entry"].get()
        telefono_valor = entries["telefono_entry"].get()
        email_valor = entries["email_entry"].get()
        tarjeta_valor = entries["tarjeta_entry"].get()

        vl = valid.validacionesCampos()

        if vl.validar_registro_datos_compra(nombre_valor, apellido_valor, direccion_valor, ciudad_valor, telefono_valor, email_valor, tarjeta_valor):
           # Insertar los datos en la tabla
           objetomysql = bd.MySQLConnector()
           objetomysql.insercion_datoscompras(s.es_sensible(nombre_valor),
                                              s.es_sensible(apellido_valor),
                                              s.es_sensible(direccion_valor),
                                              s.es_sensible(ciudad_valor),
                                              s.es_sensible(telefono_valor),
                                              s.es_sensible(email_valor),
                                              s.es_sensible(tarjeta_valor))

           # Limpiar los campos de entrada
           for entry in entries.values():
               entry.delete(0, tk.END)

           messagebox.showinfo("Guardar", "Datos guardados exitosamente.")
           compras_window.lift()

        else:
            show_warning(vl.mensaje_error)

    # Asignar la función de guardar_datos al botón de guardar
    guardar_button = tk.Button(compras_window, text="Guardar", command=guardar_datos, font=("Arial", 12),
                                   bg="#a2d2ff", fg="black")
    guardar_button.pack(pady=10)

    excel_button = tk.Button(compras_window, text="Excel",
                             command=lambda: generar_excel('compras', compras_window),
                             font=("Arial", 12), bg="#4C72B0", fg="white")
    excel_button.pack(pady=10)


#--------------------------------------------------------------------
#------------- funcion para cerrar las pantallas secundarias
def cerrar_pantalla(pantalla):
    resp = messagebox.askyesno("Advertencia", "¿Seguro que desea cerrar esta pantalla?, si lo hace cualquier progreso se perdera")

    if resp:
        pantalla.destroy()
    else:
        pantalla.lift()

#--------------------------------------------------------------------
#------------- funcion para generar los excels
def generar_excel(tabla, pantalla):
    c = bd.MySQLConnector()
    nombres_columnas, registros = c.obtener_registros_por_tabla(tabla)

    if registros:
        # Crear un DataFrame de Pandas con los registros
        df = pd.DataFrame(registros, columns=nombres_columnas)

        # Pedir al usuario la ubicación y el nombre del archivo Excel
        nombre_archivo_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])

        # Verificar si el usuario canceló la selección
        if not nombre_archivo_excel:
            messagebox.showerror("Error al guardar", "No se seleciono una ruta valida de guardado")
        else:
            # Guardar el DataFrame en el archivo Excel seleccionado con los nombres de las columnas
            try:
                df.to_excel(nombre_archivo_excel, index=False)
                messagebox.showinfo("Exito al guardar", f"Los registros se han guardado exitosamente en '{nombre_archivo_excel}'.")
            except Exception as e:
                messagebox.showerror("Error al guardar", f"Error al guardar en Excel: {e}")
    else:
        messagebox.showerror("No se encontraron registros en la tabla.")

    pantalla.lift()

#stop

# Establecer un estilo para los botones
estilo_botones = {"font": ("Arial", 12), "bg": "#4C72B0", "fg": "white", "width": 140}


# Crear un marco para contener los botones
marco_botones = tk.Frame(principal, bg="#bde0fe")
marco_botones.pack(pady=120)


# Botones para las diferentes pantallas
registro_medico_button = tk.Button(marco_botones, image=registro_medico_img, command=ventana_pantalla_principal, **estilo_botones, compound=tk.TOP)
registro_medico_button.grid(row=0, column=0, padx=10, pady=10)
registro_medico_button.config(text="Registro Médico")

datos_generales_button = tk.Button(marco_botones, image=datos_generales_img, command=pantalla_principal_datos, **estilo_botones, compound=tk.TOP)
datos_generales_button.grid(row=0, column=1, padx=10, pady=10)
datos_generales_button.config(text="Datos Generales")

datos_privados_button = tk.Button(marco_botones, image=datos_privados_img, command=pantalla_principal_privados, **estilo_botones, compound=tk.TOP)
datos_privados_button.grid(row=1, column=0, padx=10, pady=10)
datos_privados_button.config(text="Datos Privados")

compras_button = tk.Button(marco_botones, image=compras_img, command=pantalla_principal_compras, **estilo_botones, compound=tk.TOP)
compras_button.grid(row=1, column=1, padx=10, pady=10)
compras_button.config(text="Compras")


# Centrar el marco de los botones verticalmente en la ventana
principal.grid_rowconfigure(0, weight=1)
principal.grid_columnconfigure(0, weight=1)

# Ejecutar la ventana principal
principal.mainloop()