import yaml
import os
from Builder.yaml_builder import get_resource_path
from GeneralConfig.config import IMAGES_DIR

def load_assets(filepath="assets.yaml"):
    """
    Carga el registro de imágenes y resuelve las rutas completas.
    """
    path = get_resource_path(filepath)
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    resolved_assets = {}
    for key, filename in data.get("images", {}).items():
        # Aquí resolvemos contra la ruta base de assets. 
        # En ejecutable, asumimos que assets están en la carpeta raíz relativa al ejecutable.
        resolved_assets[key] = os.path.join(IMAGES_DIR, filename)
        
    return resolved_assets
