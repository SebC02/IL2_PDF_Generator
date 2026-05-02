# =============================================================================
# styles.py
# Definición visual del documento: paleta de colores y estilos de párrafo.
# Para cambiar la apariencia del manual, modificar SOLO este archivo.
# =============================================================================

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.units import cm

# ── Paleta de colores ─────────────────────────────────────────────────────────
PARCHMENT   = colors.HexColor('#e8dcc8')   # Fondo general (pergamino)
INK         = colors.HexColor('#1a1208')   # Texto principal
INK_LIGHT   = colors.HexColor('#2e2010')   # Texto secundario / notas
RULE_COLOR  = colors.HexColor('#5c4a28')   # Líneas decorativas y bordes
WARN_BG     = colors.HexColor('#c8b89a')   # Fondo de notas/apuntes
WARN_BORDER = colors.HexColor('#7a5c28')   # Borde de notas/apuntes
HEADER_BG   = colors.HexColor('#3a2e1a')   # Fondo de encabezado de sección
HEADER_FG   = colors.HexColor('#e8dcc8')   # Texto sobre encabezado de sección
DANGER_TEXT = colors.HexColor('#6b0000')   # Texto de advertencias críticas
DANGER_BG   = colors.HexColor('#ddc8a0')   # Fondo de advertencias críticas


# ── Estilos de párrafo ────────────────────────────────────────────────────────
def make_styles() -> dict:
    """
    Construye y devuelve un diccionario con todos los ParagraphStyle del manual.
    
    Similar a definir estilos CSS en web o recursos de UI en C#. Crea objetos
    ParagraphStyle de ReportLab que definen apariencia de texto (fuente, tamaño,
    color, alineación, etc.).
    
    Claves disponibles:
        title_main | title_sub | section | subsection | body | body_indent |
        bullet | note | warning | caption | intro | rec
    
    Retorna:
    - Diccionario con estilos listos para usar
    
    Arquitectura: Separa la definición visual del contenido, permitiendo
    cambios de apariencia sin modificar lógica de negocio o datos.
    """
    s = {}

    # Atributos base reutilizados en varios estilos
    _base = dict(
        fontName  = 'Courier',
        fontSize  = 9,
        leading   = 14,
        textColor = INK,
        alignment = TA_JUSTIFY,
    )
    s = {}

    # Atributos base reutilizados en varios estilos
    _base = dict(
        fontName  = 'Courier',
        fontSize  = 9,
        leading   = 14,
        textColor = INK,
        alignment = TA_JUSTIFY,
    )

    s['title_main'] = ParagraphStyle(
        'title_main',
        fontName  = 'Courier-Bold',
        fontSize  = 20,
        leading   = 24,
        textColor = INK,
        alignment = TA_CENTER,
        spaceAfter = 6,
    )

    s['title_sub'] = ParagraphStyle(
        'title_sub',
        fontName  = 'Courier-Bold',
        fontSize  = 28,
        leading   = 32,
        textColor = INK,
        alignment = TA_CENTER,
        spaceAfter = 4,
    )

    s['section'] = ParagraphStyle(
        'section',
        fontName    = 'Courier-Bold',
        fontSize    = 13,
        leading     = 16,
        textColor   = HEADER_FG,
        alignment   = TA_LEFT,
        spaceBefore = 14,
        spaceAfter  = 6,
        backColor   = HEADER_BG,
        leftIndent  = -0.3 * cm,
        rightIndent = -0.3 * cm,
        borderPad   = 5,
    )

    s['subsection'] = ParagraphStyle(
        'subsection',
        fontName      = 'Courier-Bold',
        fontSize      = 10,
        leading       = 13,
        textColor     = INK,
        alignment     = TA_LEFT,
        spaceBefore   = 10,
        spaceAfter    = 4,
        borderPadding = (0, 0, 2, 0),
    )

    s['body'] = ParagraphStyle(
        'body',
        **_base,
        spaceBefore = 3,
        spaceAfter  = 3,
    )

    s['body_indent'] = ParagraphStyle(
        'body_indent',
        **_base,
        leftIndent  = 1 * cm,
        spaceBefore = 2,
        spaceAfter  = 2,
    )

    s['bullet'] = ParagraphStyle(
        'bullet',
        **_base,
        leftIndent      = 1.2 * cm,
        firstLineIndent = -0.6 * cm,
        spaceBefore     = 2,
        spaceAfter      = 2,
    )

    s['note'] = ParagraphStyle(
        'note',
        fontName    = 'Courier-Oblique',
        fontSize    = 8,
        leading     = 11,
        textColor   = INK_LIGHT,
        alignment   = TA_LEFT,
        leftIndent  = 0.5 * cm,
        rightIndent = 0.5 * cm,
        spaceBefore = 4,
        spaceAfter  = 4,
        backColor   = WARN_BG,
        borderPad   = 6,
        borderColor = WARN_BORDER,
        borderWidth = 0.5,
    )

    s['warning'] = ParagraphStyle(
        'warning',
        fontName    = 'Courier-Bold',
        fontSize    = 9,
        leading     = 12,
        textColor   = DANGER_TEXT,
        alignment   = TA_LEFT,
        leftIndent  = 0.5 * cm,
        rightIndent = 0.5 * cm,
        spaceBefore = 6,
        spaceAfter  = 6,
        backColor   = DANGER_BG,
        borderPad   = 6,
        borderColor = DANGER_TEXT,
        borderWidth = 1,
    )

    s['caption'] = ParagraphStyle(
        'caption',
        fontName    = 'Courier-Oblique',
        fontSize    = 7.5,
        leading     = 10,
        textColor   = INK_LIGHT,
        alignment   = TA_CENTER,
        spaceBefore = 2,
        spaceAfter  = 8,
    )

    s['intro'] = ParagraphStyle(
        'intro',
        fontName    = 'Courier-Oblique',
        fontSize    = 9,
        leading     = 14,
        textColor   = INK,
        alignment   = TA_JUSTIFY,
        spaceBefore = 4,
        spaceAfter  = 4,
    )

    s['rec'] = ParagraphStyle(
        'rec',
        fontName    = 'Courier-Bold',
        fontSize    = 9,
        leading     = 13,
        textColor   = INK,
        alignment   = TA_LEFT,
        leftIndent  = 0.8 * cm,
        spaceBefore = 2,
        spaceAfter  = 2,
    )

    return s
