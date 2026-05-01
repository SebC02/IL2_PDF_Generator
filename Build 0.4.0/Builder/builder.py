# =============================================================================
# builder.py
# Ensambla el story[] del documento sección por sección.
# No contiene texto inline ni lógica visual: delega en components y content.
# =============================================================================

from reportlab.platypus import Paragraph, Spacer, Image, PageBreak
from reportlab.lib.units import cm
from PIL import Image as PILImage

from GeneralConfig.config import PAGE_W, MARGIN, IMAGES
from Styles.styles import RULE_COLOR, PARCHMENT, HEADER_BG, HEADER_FG
from Models.Const.content import Intro, Taxi, Despegue, Aterrizaje, NotasFinales
from Models.Const.content import DOC_SERIES, DOC_SUBTITLE, DOC_SUBJECT, DOC_END, DOC_EPILOGUE, DOC_CLOSING
from Flows.components import (
    make_rule, make_section_header, make_body, make_bullet,
    make_note, make_apunte_usuario, make_warning, make_subsection,
    make_image, space,
)


def _add_bullets(story: list, bullets: list, styles: dict) -> None:
    """
    Helper: añade una lista de viñetas al story.
    
    Itera sobre la lista de textos y crea elementos de viñeta
    usando make_bullet().
    
    Parámetros:
    - story: Lista donde añadir elementos
    - bullets: Lista de strings para viñetas
    - styles: Diccionario de estilos
    
    Arquitectura: Función auxiliar para reducir código repetitivo.
    """
    for text in bullets:
        story.append(make_bullet(text, styles))


def build_story(styles: dict) -> list:
    """
    Construye y devuelve el story[] completo del documento.
    
    Equivalente al método Build() en un patrón Builder de C#. Orquesta la
    construcción del documento completo llamando a funciones especializadas
    para cada sección.
    
    Parámetros:
    - styles: Diccionario de estilos generado por make_styles()
    
    Retorna:
    - Lista de Flowables (story) lista para ReportLab
    
    Arquitectura: Centraliza la lógica de ensamblaje, delegando detalles
    a funciones especializadas. Facilita cambios en la estructura del documento.
    """
    story = []

    # ── PORTADA ──────────────────────────────────────────────────────────────
    _build_cover(story, styles)

    # ── INTRODUCCIÓN ─────────────────────────────────────────────────────────
    _build_intro(story, styles)
    story.append(PageBreak())

    # ── SECCIÓN I — RODAJE ───────────────────────────────────────────────────
    _build_taxi(story, styles)
    story.append(PageBreak())

    # ── SECCIÓN II — DESPEGUE ────────────────────────────────────────────────
    _build_despegue(story, styles)
    story.append(PageBreak())

    # ── SECCIÓN III — ATERRIZAJE ─────────────────────────────────────────────
    _build_aterrizaje(story, styles)
    story.append(PageBreak())

    # ── NOTAS FINALES ────────────────────────────────────────────────────────
    _build_notas_finales(story, styles)

    return story


# ── Portada ───────────────────────────────────────────────────────────────────
def _build_cover(story: list, styles: dict) -> None:
    """
    Construye la sección de portada del documento.
    
    Carga la imagen de portada, calcula proporciones para ajustarla al ancho
    de página disponible, y la añade al story con un salto de página.
    
    Parámetros:
    - story: Lista donde añadir los elementos
    - styles: Diccionario de estilos (no usado en portada)
    
    Arquitectura: Maneja la presentación inicial del documento, separada
    del contenido textual.
    """
    pil = PILImage.open(IMAGES['portada'])
    pw, ph = pil.size
    cw = PAGE_W - 2 * MARGIN
    ch = cw * (ph / pw)
    story.append(Image(IMAGES['portada'], width=cw, height=ch))
    story.append(PageBreak())


# ── Introducción ──────────────────────────────────────────────────────────────
def _build_intro(story: list, styles: dict) -> None:
    """
    Construye la sección de Introducción del documento.
    
    Añade títulos, reglas decorativas, párrafos y listas usando componentes
    reutilizables. Utiliza datos de la clase Intro para el contenido.
    
    Parámetros:
    - story: Lista donde añadir los elementos
    - styles: Diccionario de estilos para formatear
    
    Arquitectura: Combina componentes visuales con datos de contenido,
    manteniendo separación entre presentación y datos.
    """
    story.append(space(0.6))
    story.append(Paragraph(DOC_SERIES,    styles['title_main']))
    story.append(make_rule())
    story.append(make_subsection(DOC_SUBTITLE, styles))
    story.append(Paragraph(DOC_SUBJECT,   styles['title_main']))
    story.append(make_rule())
    story.append(space(0.4))

    story.append(make_subsection(Intro.TITLE, styles))
    story.append(make_body(Intro.PARRAFO_1, styles))
    story.append(space(0.2))
    story.append(make_body(Intro.PARRAFO_2, styles))
    story.append(space(0.2))
    story.append(make_body(Intro.PARRAFO_3, styles))

    story.append(space(0.3))
    story.append(make_subsection(Intro.AVIONES_TITULO, styles))
    _add_bullets(story, Intro.AVIONES, styles)


# ── Sección I — Rodaje ────────────────────────────────────────────────────────
def _build_taxi(story: list, styles: dict) -> None:
    """
    Construye la Sección I: Rodaje (Taxi).
    
    Añade encabezado de sección, subsecciones, texto explicativo,
    apuntes y elementos visuales (imágenes) usando datos de Taxi.
    """
    story.append(make_section_header(Taxi.SECTION_TITLE, styles))
    story.append(space(0.2))

    # 1.1
    story.append(make_subsection(Taxi.SUB_CABECERA, styles))
    story.append(make_body(Taxi.CABECERA_BODY, styles))
    story.append(make_apunte_usuario(Taxi.CABECERA_APUNTE, styles))

    # 1.2
    story.append(space(0.3))
    story.append(make_subsection(Taxi.SUB_PROCEDIMIENTO, styles))
    story.append(make_body(Taxi.PROCEDIMIENTO_BODY, styles))
    _add_bullets(story, Taxi.PROCEDIMIENTO_BULLETS, styles)

    story.append(space(0.3))
    story.extend(make_image(IMAGES['tacometro'], styles, caption=Taxi.FIG_1_CAPTION))

    # 1.3
    story.append(space(0.3))
    story.append(make_subsection(Taxi.SUB_RIESGOS, styles))
    _add_bullets(story, Taxi.RIESGOS_BULLETS, styles)
    story.append(space(0.2))
    story.append(make_note(Taxi.RIESGOS_APUNTE, styles))


# ── Sección II — Despegue ─────────────────────────────────────────────────────
def _build_despegue(story: list, styles: dict) -> None:
    """
    Construye la Sección II: Despegue.
    
    Incluye texto, imágenes ilustrativas y elementos interactivos
    basados en datos de Despegue.
    """
    story.append(make_section_header(Despegue.SECTION_TITLE, styles))
    story.append(space(0.2))

    # 2.1
    story.append(make_subsection(Despegue.SUB_PREP, styles))
    story.append(make_body(Despegue.PREP_BODY, styles))
    _add_bullets(story, Despegue.PREP_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['bombas_flaps'], styles, caption=Despegue.FIG_2_CAPTION))

    # 2.2
    story.append(space(0.3))
    story.append(make_subsection(Despegue.SUB_PROC, styles))
    story.append(make_body(Despegue.PROC_BODY, styles))
    _add_bullets(story, Despegue.PROC_BULLETS, styles)

    story.append(space(0.3))
    story.extend(make_image(IMAGES['modo_combate'], styles, caption=Despegue.FIG_3_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['rueda_cola'],   styles, caption=Despegue.FIG_4_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['despegue_suave'], styles, caption=Despegue.FIG_5_CAPTION))

    story.append(PageBreak())

    # 2.3
    story.append(make_subsection(Despegue.SUB_ERRORES, styles))
    story.append(make_body(Despegue.ERRORES_BODY, styles))
    story.append(space(0.1))

    story.append(make_subsection(Despegue.ERROR_A_TITLE, styles))
    story.append(make_apunte_usuario(Despegue.ERROR_A_APUNTE, styles))
    _add_bullets(story, Despegue.ERROR_A_BULLETS, styles)

    story.append(space(0.2))
    story.append(make_subsection(Despegue.ERROR_B_TITLE, styles))
    _add_bullets(story, Despegue.ERROR_B_BULLETS, styles)

    story.append(space(0.2))
    story.append(make_subsection(Despegue.ERROR_C_TITLE, styles))
    story.append(make_warning(Despegue.ERROR_C_WARNING, styles))


# ── Sección III — Aterrizaje ──────────────────────────────────────────────────
def _build_aterrizaje(story: list, styles: dict) -> None:
    """
    Construye la Sección III: Aterrizaje.
    
    La sección más compleja con múltiples subsecciones, imágenes
    y procedimientos detallados usando datos de Aterrizaje.
    """
    story.append(make_section_header(Aterrizaje.SECTION_TITLE, styles))
    story.append(space(0.2))

    # 3.1
    story.append(make_subsection(Aterrizaje.SUB_GENERAL, styles))
    story.append(make_body(Aterrizaje.GENERAL_BODY, styles))
    story.append(make_apunte_usuario(Aterrizaje.GENERAL_APUNTE, styles))
    story.append(make_warning(Aterrizaje.GENERAL_WARNING, styles))

    # 3.2
    story.append(space(0.3))
    story.append(make_subsection(Aterrizaje.SUB_MANIOBRA, styles))
    story.append(make_body(Aterrizaje.MANIOBRA_BODY, styles))
    story.append(space(0.1))

    # Fase 1
    story.append(make_subsection(Aterrizaje.FASE1_TITLE, styles))
    _add_bullets(story, Aterrizaje.FASE1_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['posicion_exterior'], styles, caption=Aterrizaje.FIG_6_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['posicion_cabina'],   styles, caption=Aterrizaje.FIG_7_CAPTION))

    story.append(PageBreak())

    # Fase 2
    story.append(make_subsection(Aterrizaje.FASE2_TITLE, styles))
    _add_bullets(story, Aterrizaje.FASE2_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['corte_potencia'],  styles, caption=Aterrizaje.FIG_8_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['descenso_cabina'], styles, caption=Aterrizaje.FIG_9_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['descenso_externo'], styles, caption=Aterrizaje.FIG_10_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['altura_minima'],   styles, caption=Aterrizaje.FIG_11_CAPTION))

    story.append(PageBreak())

    # Fase 3
    story.append(make_subsection(Aterrizaje.FASE3_TITLE, styles))
    _add_bullets(story, Aterrizaje.FASE3_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['giro_180'], styles, caption=Aterrizaje.FIG_12_CAPTION))

    # Fase 4
    story.append(space(0.3))
    story.append(make_subsection(Aterrizaje.FASE4_TITLE, styles))
    _add_bullets(story, Aterrizaje.FASE4_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['bajar_flaps'], styles, caption=Aterrizaje.FIG_13_CAPTION))

    story.append(PageBreak())

    # Fase 5
    story.append(make_subsection(Aterrizaje.FASE5_TITLE, styles))
    _add_bullets(story, Aterrizaje.FASE5_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['encarar_pista'],  styles, caption=Aterrizaje.FIG_14_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['aproximacion'],   styles, caption=Aterrizaje.FIG_15_CAPTION))
    story.append(space(0.2))
    story.extend(make_image(IMAGES['potencia_stall'], styles, caption=Aterrizaje.FIG_16_CAPTION))

    story.append(PageBreak())

    # Fase 6
    story.append(make_subsection(Aterrizaje.FASE6_TITLE, styles))
    _add_bullets(story, Aterrizaje.FASE6_BULLETS, styles)
    story.append(space(0.2))
    story.extend(make_image(IMAGES['toque_3puntos'], styles, caption=Aterrizaje.FIG_17_CAPTION))

    story.append(PageBreak())

    # 3.3
    story.append(make_subsection(Aterrizaje.SUB_FALLOS, styles))
    _add_bullets(story, Aterrizaje.FALLOS_BULLETS, styles)
    story.append(space(0.2))
    story.append(make_warning(Aterrizaje.FALLOS_WARNING, styles))


# ── Notas finales ─────────────────────────────────────────────────────────────
def _build_notas_finales(story: list, styles: dict) -> None:
    """
    Construye la sección final con notas, epílogo y cierres.
    
    Añade elementos de conclusión usando constantes globales
    y datos de NotasFinales.
    """
    story.append(make_section_header(NotasFinales.SECTION_TITLE, styles))
    story.append(space(0.3))

    story.append(make_body(NotasFinales.PARRAFO_1, styles))
    story.append(space(0.2))
    story.append(make_body(NotasFinales.PARRAFO_2, styles))

    story.append(space(0.3))
    story.append(make_subsection(NotasFinales.PRINCIPIOS_TITULO, styles))
    _add_bullets(story, NotasFinales.PRINCIPIOS, styles)

    story.append(space(0.5))
    story.append(make_rule())
    story.append(space(0.2))
    story.append(Paragraph(DOC_EPILOGUE, styles['intro']))

    story.append(space(0.3))
    story.append(Paragraph(DOC_END, styles['title_main']))
    story.append(make_rule())
    story.append(space(0.2))
    story.append(Paragraph(DOC_CLOSING, styles['caption']))
