# =============================================================================
# config.py
# Configuración de entorno: rutas, tamaños de página y márgenes.
# ES EL ÚNICO ARCHIVO QUE DEBE MODIFICARSE AL CAMBIAR DE ENTORNO.
# =============================================================================

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

# ── Página ────────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN         = 2.2 * cm
TOP_MARGIN     = 2.4 * cm
BOTTOM_MARGIN  = 1.8 * cm

import sys

# ── Rutas ─────────────────────────────────────────────────────────────────────
# Detectar si estamos ejecutando como ejecutable o script
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGES_DIR = os.path.join(base_dir, "GeneralConfig", "assets", "images")
OUTPUT_PDF = os.path.join(base_dir, "Academia_Combate_250H_1.pdf")

# ── Metadatos del documento ───────────────────────────────────────────────────
DOC_TITLE  = "Academia de Combate 250H #1"
DOC_AUTHOR = "COMANDO AEREO"

# ── Imágenes (nombre de archivo → ruta completa) ──────────────────────────────
# Renombrar los archivos en assets/images/ para que coincidan con estas claves,
# o modificar los valores directamente.
def img_path(filename: str) -> str:
    """
    Construye la ruta absoluta a una imagen dentro de assets/images/.
    
    Equivalente a Path.Combine() en C#. Asegura que las rutas sean correctas
    independientemente del directorio de ejecución.
    
    Parámetros:
    - filename: Nombre del archivo de imagen (ej: "portada.png")
    
    Retorna:
    - Ruta completa al archivo
    
    Arquitectura: Centraliza la gestión de rutas de recursos, facilitando
    cambios en la estructura de directorios sin modificar múltiples lugares.
    """
    return os.path.join(IMAGES_DIR, filename)

IMAGES = {
    "portada"           : img_path("portada.png"),
    "portada_new"       : img_path("PortadaBaseline.png"),
    "tacometro"         : img_path("Tacometro a 1200-1300RPM.jpg"),
    "bombas_flaps"      : img_path("Cazas con Bombas si requieren flaps.jpg"),
    "modo_combate"      : img_path("Utilizamos el MODO COMBATE al despegue, no el modo emergencia.jpg"),
    "rueda_cola"        : img_path("Rueda de cola levantandose del piso.jpg"),
    "despegue_suave"    : img_path("El despegue debe ser suave, no abrupto con los comandos.jpg"),
    "posicion_exterior" : img_path("Maniobra de aterrizaje, posicion con respecto a la psita desde fuera del avion.jpg"),
    "posicion_cabina"   : img_path("Maniobra de aterriza,e posicion respecto a la pista al inicio de la misma desde la vision del piloto.jpg"),
    "corte_potencia"    : img_path("Se corta la potencia para el descenso abrupto.jpg"),
    "descenso_cabina"   : img_path("El descenso es abrupto hacia la cabecera, vista de cabina.jpg"),
    "descenso_externo"  : img_path("Descenso abrupto, externo.jpg"),
    "altura_minima"     : img_path("La altura minima para la pasada es baja, pero no demasiado, hay margende maniobra.jpg"),
    "giro_180"          : img_path("El giro en la otra cabecera es lo suficientemente abrupto como para perder energia.jpg"),
    "bajar_flaps"       : img_path("De camino a la segunda cabecera, bajamos los flaps.jpg"),
    "encarar_pista"     : img_path("Empezamos a encarar la pista, bajamos el tren.jpg"),
    "aproximacion"      : img_path("Aproximacion final, a baja velocidad encarando la pista para el aterrizaje.jpg"),
    "potencia_stall"    : img_path("Y subimos la potencia para no entrar en stall en la aproximacion final.jpg"),
    "toque_3puntos"     : img_path("Al llegar a la cabecera cortamos la potencia y levantamos el morro para aterrizar en 3 puntos.jpg"),
    "flaps_20"          : img_path("20 grados de flaps.jpg"),
}
