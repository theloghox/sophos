# Sophos Firewall Remote Shutdown
Este repositorio contiene 2 scripts para el apagado remoto de tu Sophos Firewall

- shutdownsf.py (inseguro - contraseñas en texto plano)
- secureshutdownsf.py (+seguro - utiliza)

## Requisitos

- Python 3.6 o superior
- Bibliotecas `pexpect` y `pywinpty` (esta última solo es necesaria para Windows)

## Instalación

### Windows

1. **Instalar Python**:
    - Descarga e instala Python desde [python.org](https://www.python.org/downloads/windows/).
    - Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

2. **Instalar `pexpect` y `pywinpty`**:
    - Abre PowerShell o la terminal de comandos y ejecuta:
    ```sh
    pip install pexpect
    pip install pywinpty
    ```

### Linux

1. **Instalar Python**:
    - La mayoría de las distribuciones de Linux ya tienen Python instalado. Verifica si está instalado ejecutando:
    ```sh
    python3 --version
    ```
    - Si no está instalado, usa el gestor de paquetes de tu distribución. Por ejemplo, en Debian/Ubuntu:
    ```sh
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. **Instalar `pexpect`**:
    - Abre una terminal y ejecuta:
    ```sh
    pip3 install pexpect
    ```

## Uso

1. Clona este repositorio:
    ```sh
    git clone https://github.com/theloghox/sophos.git
    cd sophos
    ```

2. Modifica el script con los valores correctos para `hostname`, `username` y `password`.

3. Ejecuta el script:

    - **Windows**:
    ```sh
    python shutdownsf.py
    ```

    - **Linux**:
    ```sh
    python3 shutdownsf.py
    ```

### Si vas a utilizar secureshutdownsf 

### Generar e Importar una Clave SSH

1. **Generar una Clave SSH**:
    - En Windows (PowerShell) o Linux/MacOS (Terminal):
    ```sh
    ssh-keygen -t rsa -b 2048 -f ~/.ssh/id_rsa
    ```

2. **Copiar la Clave Pública al Firewall**:
    - Obtener la clave pública:
    ```sh
    cat ~/.ssh/id_rsa.pub
    ```
    - Acceder al firewall y agregar la clave pública:
    ```sh
    Administración > Acceso al dispositivo > Autenticación de clave pública para el administrador
    Pega el contenido del archivo id_rsa.pub
    ![image](https://github.com/user-attachments/assets/387eeaed-cfcd-421a-8a84-efe9d851ae0f)
    No olvides Aplicar los cambios
    ```

3. **Modificar el archivo **:
    - Obtener la clave pública:
    ```sh
    cat ~/.ssh/id_rsa.pub
    ```
    - Acceder al firewall y agregar la clave pública:
    ```sh
    echo "tu_clave_publica" >> ~/.ssh/authorized_keys
    ```



