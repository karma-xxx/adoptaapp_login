usuarios = {
    "fundacion@adoptaapp.com": "admin123",
    "usuario@adoptaapp.com": "user456",
    "voluntario@adoptaapp.com": "help789"
}

def iniciar_sesion(correo, contraseña):
    if correo in usuarios and usuarios[correo] == contraseña:
        return True
    else:
        return False
