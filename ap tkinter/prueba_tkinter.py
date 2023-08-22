import tkinter as tk

def verificar_login():
    # Obtiene el texto ingresado en el campo de entrada
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    # Realiza la verificación del inicio de sesión aquí
    # Puedes agregar la lógica de verificación que necesites
    
    # Ejemplo básico de verificación
    if usuario == "admin":
        if contraseña == "12345":
            mensaje_resultado.config(text="Inicio de sesión exitoso", fg="green")
            boton_login.config(state="disabled")
            boton_reset.config(state="normal")
        else:
            mensaje_resultado.config(text="Contrasena incorrecta", fg="red")
    else:
        mensaje_resultado.config(text="Usuario Incorrecto", fg="red")
        
    '''if usuario == "admin" and contraseña == "12345":
        mensaje_resultado.config(text="Inicio de sesión exitoso", fg="green")
    else:
        mensaje_resultado.config(text="Inicio de sesión fallido", fg="red")'''

def reset():
    entry_usuario.delete(0,tk.END)
    entry_contraseña.delete(0,tk.END)
    boton_login.config(state="normal")
    boton_reset.config(state="disabled")
        
# Crear la ventana
ventana = tk.Tk()
ventana.geometry("350x200")
ventana.title("Ventana de inicio de sesión")

# Crear y posicionar los elementos en la ventana
mensaje = tk.Label(ventana, text="Ingrese su usuario y contraseña")
mensaje.pack()

label_usuario = tk.Label(ventana, text="Usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack()
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

boton_login = tk.Button(ventana, text="Iniciar sesión", command=verificar_login, state="normal")
boton_login.pack()

boton_reset = tk.Button(ventana, text="Reset", command=reset, state="disabled")
boton_reset.pack()

boton_salir = tk.Button(ventana, text="Salir", command=exit)
boton_salir.pack()

mensaje_resultado = tk.Label(ventana, text="")
mensaje_resultado.pack()