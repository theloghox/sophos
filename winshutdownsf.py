# Autor: [TheLoghox]
# Labs: Digital User SAS
# Contacto: jvelez@digital-user.com

import paramiko
import time

# Reemplaza estos valores con los correctos
hostname = "172.16.16.16"
username = "admin"
password = "Digitaluser98*"

try:
    # Crear un cliente SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Conectar al servidor SSH
    client.connect(hostname, username=username, password=password)

    # Crear una sesión de canal
    channel = client.invoke_shell()
    
    # Esperar a que el canal esté listo para enviar datos
    time.sleep(1)
    output = channel.recv(1024).decode('utf-8')
    print(output)

    # Enviar comandos a través de la sesión
    channel.send("7\n")
    time.sleep(1)
    output = channel.recv(1024).decode('utf-8')
    print(output)

    channel.send("S\n")
    time.sleep(1)
    output = channel.recv(1024).decode('utf-8')
    print(output)

    # Interactuar con la CLI
    while True:
        if channel.recv_ready():
            output = channel.recv(1024).decode('utf-8')
            print(output)
        time.sleep(1)
except Exception as e:
    print(f"Error: {e}")
finally:
    # Cerrar la conexión SSH
    client.close()
