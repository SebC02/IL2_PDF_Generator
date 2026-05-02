# =============================================================================
# main.py
# Entry point del proyecto que usa el Builder interno
# =============================================================================

import traceback
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from GeneralConfig.config import PAGE_W, PAGE_H, MARGIN, TOP_MARGIN, BOTTOM_MARGIN, OUTPUT_PDF, DOC_TITLE, DOC_AUTHOR
from Styles.styles import make_styles, PARCHMENT, RULE_COLOR, HEADER_BG, HEADER_FG
from Builder.yaml_builder import build_story_from_yaml, load_yaml
from GeneralConfig.asset_loader import load_assets
from GeneralConfig.ui_utils import check_dependencies, show_error, show_success

# Variable global para los metadatos (inyectada en main)
doc_metadata = {}

def draw_page(c, doc):
    """
    Callback que dibuja el encabezado, pie de página y bordes en cada página del PDF,
    usando metadatos dinámicos.
    """
    c.saveState()
    
    # Fondo de pergamino
    c.setFillColor(PARCHMENT)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    
    # Bordes
    c.setStrokeColor(RULE_COLOR)
    c.setLineWidth(3)
    c.rect(0.8*cm, 0.8*cm, PAGE_W - 1.6*cm, PAGE_H - 1.6*cm, fill=0, stroke=1)
    c.setLineWidth(0.8)
    c.rect(1.05*cm, 1.05*cm, PAGE_W - 2.1*cm, PAGE_H - 2.1*cm, fill=0, stroke=1)
    
    # Encabezado (solo en páginas internas)
    if doc.page > 1:
        c.setFillColor(HEADER_BG)
        c.rect(0.8*cm, PAGE_H - 1.8*cm, PAGE_W - 1.6*cm, 0.9*cm, fill=1, stroke=0)
        c.setFillColor(HEADER_FG)
        c.setFont('Courier-Bold', 7)
        c.drawString(1.4*cm, PAGE_H - 1.35*cm, doc_metadata.get("header", ""))
        c.setFont('Courier', 7)
        c.drawRightString(PAGE_W - 1.4*cm, PAGE_H - 1.35*cm, f'PÁG. {doc.page - 1}')
    
    # Pie de página
    c.setFillColor(RULE_COLOR)
    c.setFont('Courier', 6)
    c.drawCentredString(PAGE_W / 2, 1.15*cm, doc_metadata.get("footer", ""))
    
    c.restoreState()


def main():
    """
    Función principal que orquesta la generación del PDF usando configuración YAML.
    """
    global doc_metadata
    
    if not check_dependencies(["content.yaml", "assets.yaml"]):
        return

    try:
        # Cargar contenido YAML
        content_data = load_yaml("content.yaml")
        assets_data = load_assets("assets.yaml")
        
        # Inyectar metadatos para el callback
        doc_metadata = content_data.get("metadata", {})
        
        # Crear documento
        doc = SimpleDocTemplate(
            OUTPUT_PDF,
            pagesize=A4,
            leftMargin=MARGIN,
            rightMargin=MARGIN,
            topMargin=TOP_MARGIN,
            bottomMargin=BOTTOM_MARGIN,
            title=DOC_TITLE,
            author=DOC_AUTHOR,
        )
        
        # Generar estilos
        styles = make_styles()
        
        # Construir story usando el YAMLBuilder
        story = build_story_from_yaml(styles, content_data, assets_data)
        
        # Generar PDF
        doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
        
        show_success(f"PDF generado exitosamente:\n{OUTPUT_PDF}")
        
    except Exception as e:
        # Registrar el error en un log persistente
        with open("error.log", "w", encoding="utf-8") as f:
            traceback.print_exc(file=f)
        show_error(f"Error crítico detectado:\n{str(e)}\n\nDetalles guardados en error.log")


if __name__ == '__main__':
    main()
