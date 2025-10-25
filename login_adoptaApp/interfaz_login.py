# Importamos las librerías necesarias
import tkinter as tk
from tkinter import messagebox
from login import iniciar_sesion

# Función que valida las credenciales ingresadas
def verificar_credenciales():
    correo = entry_correo.get().strip()
    contraseña = entry_contraseña.get().strip()

    # Validamos que los campos no estén vacíos
    if not correo or not contraseña:
        messagebox.showwarning("Campos vacíos", "Por favor, ingrese su correo y contraseña.")
        return

    # Verificamos las credenciales con la función del archivo login.py
    acceso_valido = iniciar_sesion(correo, contraseña)

    if acceso_valido:
        messagebox.showinfo("Inicio de sesión", f"Bienvenido/a a AdoptaApp, {correo} 🐾")
    else:
        messagebox.showerror("Error de acceso", "Correo o contraseña incorrectos.\n\n"
                             "Ejemplos válidos:\n"
                             "fundacion@adoptaapp.com → admin123\n"
                             "usuario@adoptaapp.com → user456")

# ---- Construcción de la interfaz gráfica ----

ventana = tk.Tk()
ventana.title("🐾 AdoptaApp - Inicio de Sesión")
ventana.geometry("500x350")
ventana.config(bg="#F7F7F7")

# Título
titulo = tk.Label(
    ventana,
    text="Bienvenido a AdoptaApp 🐶🐱",
    font=("Arial", 16, "bold"),
    bg="#F7F7F7",
    fg="#333"
)
titulo.pack(pady=10)

# Subtítulo
subtitulo = tk.Label(
    ventana,
    text="Inicia sesión para acceder a la plataforma de adopciones.",
    font=("Arial", 10),
    bg="#F7F7F7"
)
subtitulo.pack()

# Campo correo
tk.Label(ventana, text="Correo electrónico:", bg="#F7F7F7", font=("Arial", 11)).pack(pady=5)
entry_correo = tk.Entry(ventana, width=35, font=("Arial", 10))
entry_correo.pack(ipady=3)

# Campo contraseña
tk.Label(ventana, text="Contraseña:", bg="#F7F7F7", font=("Arial", 11)).pack(pady=5)
entry_contraseña = tk.Entry(ventana, width=35, show="*", font=("Arial", 10))
entry_contraseña.pack(ipady=3)

# Botón de inicio de sesión
btn_iniciar = tk.Button(
    ventana,
    text="Iniciar sesión",
    command=verificar_credenciales,
    bg="#3B82F6",
    fg="white",
    font=("Arial", 11, "bold"),
    relief="raised",
    width=20
)
btn_iniciar.pack(pady=15)

# Área informativa con ejemplos
info = tk.Label(
    ventana,
    text="💡 Ejemplos de acceso:\n"
         "• fundacion@adoptaapp.com  →  admin123\n"
         "• usuario@adoptaapp.com  →  user456",
    bg="#E0F2FE",
    fg="#000",
    font=("Arial", 10),
    relief="solid",
    bd=1,
    padx=10,
    pady=5
)
info.pack(pady=10)

# Pie de página
pie = tk.Label(
    ventana,
    text="© 2025 AdoptaApp - Proyecto de adopción responsable 🐾",
    bg="#F7F7F7",
    fg="#555",
    font=("Arial", 8)
)
pie.pack(side="bottom", pady=5)

# Iniciar la ventana
ventana.mainloop()
