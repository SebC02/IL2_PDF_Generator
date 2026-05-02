import os
import subprocess
import sys

def build():
    print("Iniciando compilación de generate_document.exe...")
    
    # Comando para PyInstaller usando el ejecutable actual para evitar problemas de PATH
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconsole",
        "--onefile",
        "--name=generate_document",
        "main.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("\n✓ Ejecutable generado con éxito en la carpeta /dist")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error durante la compilación: {e}")

if __name__ == "__main__":
    # Asegurar que pyinstaller esté instalado
    try:
        import PyInstaller
    except ImportError:
        print("Instalando PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    build()
