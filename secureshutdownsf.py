# Autor: Jorge Mario Vélez Rincón [TheLoghox]
# Labs: Digital User SAS
# Contacto: jvelez@digital-user.com

import pexpect

# Reemplaza estos valores con los correctos
hostname = "172.16.16.16"
username = "admin"
ssh_key = "~/.ssh/id_rsa"

# Construir el comando SSH
ssh_command = f"ssh -i {ssh_key} {username}@{hostname}"

# Iniciar la sesión SSH
child = pexpect.spawn(ssh_command)

#Interactuamos con la lista de Sophos
child.expect("Select Menu Number \[0-7\]:")

#Seleccionamos la opción 7 para apagar/reiniciar el firewall
child.sendline("7")

# Esperar la solicitud de apagado o reinicio
child.expect("Shutdown\(S/s\) or Reboot\(R/r\) Device  \(S/s/R/r\):")

# Enviar la respuesta deseada, 'S' para Shutdown
child.sendline("S")

#Interactuar con la CLI - Ejecuta la acción
child.interact()

#Cerrar sesión SSH
child.close()
