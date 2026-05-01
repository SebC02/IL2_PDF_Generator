# =============================================================================
# yaml_builder.py
# Nuevo Builder capaz de interpretar content.yaml.
# Delegado al renderizado de componentes basado en la estructura YAML.
# =============================================================================

import yaml
import sys
import os
from reportlab.platypus import PageBreak
from reportlab.lib.units import cm
from GeneralConfig.config import IMAGES
from Flows.components import (
    make_rule, make_section_header, make_body, make_bullet,
    make_note, make_apunte_usuario, make_warning, make_subsection,
    make_image, space
)

def get_resource_path(relative_path):
    """ Obtiene la ruta al recurso buscando en el directorio del ejecutable o en la ruta de desarrollo """
    if getattr(sys, 'frozen', False):
        # Cuando es un ejecutable, buscamos en la carpeta donde reside el .exe
        return os.path.join(os.path.dirname(sys.executable), relative_path)
    # En desarrollo, busca relativo al archivo actual
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', relative_path)

def load_yaml(filepath="content.yaml"):
    """
    Summary: Carga y parsea el archivo de configuración YAML de contenido.
    """
    path = get_resource_path(filepath)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def _render_block(block, styles, assets):
    """
    Summary: Despacha la renderización de un bloque basado en su tipo, delegando a los componentes de flujo.
    """
    b_type = block.get("type")

    if b_type == "paragraph":
        return [make_body(block["content"], styles)]

    elif b_type == "subsection":
        return [make_subsection(block["content"], styles)]

    elif b_type == "bullet_list":
        return [make_bullet(item, styles) for item in block["items"]]

    elif b_type == "note":
        return [make_note(block["content"], styles)]

    elif b_type == "warning":
        return [make_warning(block["content"], styles)]

    elif b_type == "image":
        img_key = block["key"]
        path = assets.get(img_key)
        # Extraer valores y asegurar que sean números antes de multiplicar por cm
        raw_width = block.get("width", 13.0)
        raw_height = block.get("max_height", 9.0)
        
        # Convertir a float explícitamente para evitar problemas de tipos
        width_val = float(raw_width) * cm
        height_val = float(raw_height) * cm
        
        return make_image(path, styles, width=width_val, max_height=height_val, caption=block.get("caption"))

    return [space(0.2)]

def build_story_from_yaml(styles: dict, content_data: dict, assets: dict) -> list:
    """
    Summary: Construye el story del PDF iterando sobre todas las secciones, utilizando el diccionario de assets resueltos.
    """
    story = []

    for section in content_data.get("sections", []):
        # La portada no requiere el encabezado de sección estándar
        if section["id"] != "portada":
            story.append(make_section_header(section["title"], styles))
            story.append(space(0.2))

        for block in section.get("blocks", []):
            story.extend(_render_block(block, styles, assets))

        story.append(PageBreak())

    return story
