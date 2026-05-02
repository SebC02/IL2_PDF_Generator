# =============================================================================
# components.py
# Funciones que devuelven Flowables de ReportLab listos para agregar al story.
# Cada función tiene una única responsabilidad visual.
# =============================================================================

from reportlab.platypus import Paragraph, Image, HRFlowable, Spacer
from reportlab.lib.units import cm
from PIL import Image as PILImage
from typing import Optional, List

from Styles.styles import RULE_COLOR


# ── Regla horizontal ──────────────────────────────────────────────────────────
def make_rule() -> HRFlowable:
    """
    Crea una línea separadora decorativa horizontal.
    
    Equivalente a un componente UI reutilizable en C#. Devuelve un objeto
    HRFlowable de ReportLab que dibuja una línea con estilo consistente.
    
    Retorna:
    - HRFlowable configurado con color y grosor
    
    Arquitectura: Encapsula la creación de elementos visuales comunes,
    promoviendo reutilización y consistencia visual.
    """
    return HRFlowable(
        width='100%',
        thickness=1,
        color=RULE_COLOR,
        spaceAfter=6,
        spaceBefore=6,
    )


# ── Encabezado de sección (banda oscura) ──────────────────────────────────────
def make_section_header(text: str, styles: dict) -> Paragraph:
    """
    Crea un encabezado de sección con fondo oscuro.
    
    Similar a un método de fábrica en C#. Combina texto con estilo predefinido
    para crear encabezados visualmente distintivos.
    
    Parámetros:
    - text: Texto del encabezado
    - styles: Diccionario de estilos (debe contener 'section')
    
    Retorna:
    - Paragraph con estilo de sección aplicado
    
    Arquitectura: Abstrae la creación de elementos complejos, ocultando
    detalles de implementación y facilitando cambios globales.
    """
    return Paragraph(f'&nbsp;&nbsp;{text}', styles['section'])


# ── Párrafo de cuerpo ─────────────────────────────────────────────────────────
def make_body(text: str, styles: dict) -> Paragraph:
    """
    Crea un párrafo de texto normal del cuerpo.
    
    Función de fábrica simple. Aplica el estilo 'body' al texto proporcionado.
    
    Parámetros:
    - text: Contenido del párrafo
    - styles: Diccionario de estilos
    
    Retorna:
    - Paragraph con estilo de cuerpo
    
    Arquitectura: Simplifica la creación de elementos comunes, reduciendo
    código repetitivo.
    """
    return Paragraph(text, styles['body'])


# ── Viñeta ────────────────────────────────────────────────────────────────────
def make_bullet(text: str, styles: dict) -> Paragraph:
    """
    Crea un elemento de lista con viñeta.
    
    Añade el símbolo de viñeta (•) al texto y aplica estilo correspondiente.
    
    Parámetros:
    - text: Texto de la viñeta
    - styles: Diccionario de estilos
    
    Retorna:
    - Paragraph con viñeta formateada
    
    Arquitectura: Maneja la presentación de listas de manera consistente.
    """
    return Paragraph(f'•  {text}', styles['bullet'])


# ── Nota / Apunte (fondo claro, cursiva) ─────────────────────────────────────
def make_note(text: str, styles: dict) -> Paragraph:
    """
    Crea una nota con fondo claro y texto en cursiva.
    
    Para apuntes informativos o secundarios.
    
    Parámetros:
    - text: Contenido de la nota
    - styles: Diccionario de estilos
    
    Retorna:
    - Paragraph con estilo de nota
    
    Arquitectura: Diferencia visualmente tipos de contenido.
    """
    return Paragraph(f'<i>APUNTES: {text}</i>', styles['note'])


def make_apunte_usuario(text: str, styles: dict) -> Paragraph:
    """
    Crea una nota personal del usuario con símbolo especial.
    
    Similar a make_note pero con indicador de experiencia personal.
    
    Parámetros:
    - text: Contenido del apunte
    - styles: Diccionario de estilos
    
    Retorna:
    - Paragraph con estilo de apunte usuario
    
    Arquitectura: Proporciona variantes especializadas de componentes base.
    """
    return Paragraph(f'<i>★ APUNTES: {text}</i>', styles['note'])


# ── Advertencia crítica (borde rojo) ─────────────────────────────────────────
def make_warning(text: str, styles: dict) -> Paragraph:
    """
    Crea una advertencia crítica con borde rojo.
    
    Para información importante de seguridad o procedimientos críticos.
    
    Parámetros:
    - text: Contenido de la advertencia
    - styles: Diccionario de estilos
    
    Retorna:
    - Paragraph con estilo de advertencia
    
    Arquitectura: Enfatiza visualmente contenido crítico.
    """
    return Paragraph(f'<b>⚠ ATENCIÓN:</b> {text}', styles['warning'])


# ── Subsección ────────────────────────────────────────────────────────────────
def make_subsection(text: str, styles: dict) -> Paragraph:
    """
    Crea un título de subsección.
    
    Para divisiones menores dentro de secciones.
    
    Parámetros:
    - text: Título de la subsección
    - styles: Diccionario de estilos
    
    Retorna:
    - Paragraph con estilo de subsección
    
    Arquitectura: Jerarquía visual de contenido.
    """
    return Paragraph(text, styles['subsection'])


# ── Imagen con caption opcional ───────────────────────────────────────────────
def make_image(
    path: str,
    styles: dict,
    width: float = 13 * cm,
    caption: Optional[str] = None,
    max_height: float = 9 * cm,
) -> List:
    """
    Crea un elemento de imagen con caption opcional.
    
    Equivalente a un componente Image con texto alternativo en UI. Carga la imagen,
    ajusta proporciones, añade caption si se proporciona. Maneja errores gracefully.
    
    Parámetros:
    - path: Ruta al archivo de imagen
    - styles: Diccionario de estilos
    - width: Ancho deseado (default: 13cm)
    - caption: Texto descriptivo opcional
    - max_height: Altura máxima permitida
    
    Retorna:
    - Lista con [Image] o [Image, Paragraph(caption)]
    
    Arquitectura: Encapsula manejo de imágenes y errores, proporcionando
    interfaz consistente para contenido multimedia.
    """
    try:
        pil = PILImage.open(path)
        pw, ph = pil.size
        ratio  = ph / pw
        height = width * ratio

        if height > max_height:
            height = max_height
            width  = height / ratio

        items = [Image(path, width=width, height=height)]

        if caption:
            items.append(Paragraph(caption, styles['caption']))

        return items

    except Exception as exc:
        return [Paragraph(f'[Imagen no disponible: {exc}]', styles['body'])]


# ── Espaciado estándar ────────────────────────────────────────────────────────
def space(height_cm: float = 0.2) -> Spacer:
    """
    Crea un elemento de espaciado vertical.
    
    Similar a Margin o Padding en UI. Añade espacio blanco entre elementos.
    
    Parámetros:
    - height_cm: Altura del espacio en centímetros (default: 0.2)
    
    Retorna:
    - Spacer configurado
    
    Arquitectura: Controla el layout y separación visual entre componentes.
    """
    return Spacer(1, height_cm * cm)
