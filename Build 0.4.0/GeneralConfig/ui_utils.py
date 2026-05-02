import tkinter as tk
from tkinter import messagebox
import os

def show_error(msg):
    """Muestra una ventana de error en caso de fallo."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error de Ejecución", msg)
    root.destroy()

def show_success(msg):
    """Muestra una ventana de éxito al finalizar."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Proceso Finalizado", msg)
    root.destroy()

def check_dependencies(files):
    """Verifica si los archivos necesarios existen."""
    for file in files:
        if not os.path.exists(file):
            show_error(f"Archivo faltante necesario para la ejecución: {file}")
            return False
    return True
