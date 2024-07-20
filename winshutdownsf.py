import paramiko

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

    # Enviar comandos a través de la sesión
    channel.send("7\n")
    while not channel.recv_ready():
        pass
    output = channel.recv(1024).decode('utf-8')
    print(output)

    channel.send("S\n")
    while not channel.recv_ready():
        pass
    output = channel.recv(1024).decode('utf-8')
    print(output)

    # Cerrar la conexión SSH
    client.close()
except Exception as e:
    print(f"Error: {e}")
