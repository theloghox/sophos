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
    python script.py
    ```

    - **Linux**:
    ```sh
    python3 script.py
    ```




