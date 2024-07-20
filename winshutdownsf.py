import pexpect
import pywinpty

# Reemplaza estos valores con los correctos
hostname = "172.16.16.16"
username = "admin"
password = "Digitaluser98*"

# Construir el comando SSH
ssh_command = f"ssh {username}@{hostname}"

# Iniciar la sesión SSH utilizando pywinpty para manejar el pseudoterminal
winpty = pywinpty.PTY()
winpty.spawn(ssh_command)
child = pexpect.fdpexpect.fdspawn(winpty.fd)

# Manejar la autenticidad del host
# child.expect espera 0:para la pregunta 1:si solicita password, 2: si la conexión se cierra y 3: tiempo de espera agotado
i = child.expect([r"Are you sure you want to continue connecting \(yes/no/\[fingerprint\]\)?", "password:", pexpect.EOF, pexpect.TIMEOUT])

if i == 0:
    # Si se pregunta sobre la autenticidad del host, responde 'yes'
    child.sendline("yes")
    # Esperar la siguiente solicitud de contraseña
    child.expect("password:")
elif i == 1:
    # pass no hace nada, solo deja fluir el código.
    pass
elif i in [2, 3]:
    print("Error: no se pudo conectar.")
    print(child.before.decode('utf-8'))
    child.close()
    exit(1)

# Ingresar la contraseña
child.sendline(password)

# Interactuamos con la lista de Sophos
child.expect(r"Select Menu Number \[0-7\]:")

# Seleccionamos la opción 7 para apagar/reiniciar el firewall
child.sendline("7")

# Esperar la solicitud de apagado o reinicio
child.expect(r"Shutdown\(S/s\) or Reboot\(R/r\) Device  \(S/s/R/r\):")

# Enviar la respuesta deseada, por ejemplo, 'S' para Shutdown
child.sendline("S")

# Interactuar con la CLI
child.interact()

# Cerrar sesión SSH
child.close()
