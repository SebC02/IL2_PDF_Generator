# Guía de Solución v0.4.0

Esta guía describe el estado actual de la solución tras la consolidación de la versión 0.4.0.

## Componentes Clave
- **`main.py`**: Punto de entrada único. Gestiona la validación visual y la orquestación del proceso.
- **`Builder/yaml_builder.py`**: Motor de renderizado dinámico. Interpreta `content.yaml` y resuelve rutas de forma agnóstica al entorno (desarrollo vs. ejecutable).
- **`GeneralConfig/asset_loader.py`**: Gestor de activos. Resuelve rutas de imágenes desde `assets.yaml`.
- **`GeneralConfig/ui_utils.py`**: Utilidades visuales (Tkinter) para feedback de usuario sin necesidad de consola.
- **`content.yaml`**: Definición jerárquica del manual, incluyendo metadatos globales (cabecera/pie).
- **`assets.yaml`**: Registro central de imágenes.

## Cómo operar en v0.4.0
1. **Añadir contenido**: Editar `content.yaml`.
2. **Añadir imágenes**:
    - Copiar el archivo a `GeneralConfig/assets/images/`.
    - Registrar la clave en `assets.yaml`.
    - Referenciar la clave en `content.yaml` dentro de un bloque tipo `image`.
3. **Generar PDF**: Ejecutar `generate_document.exe` (en modo producción) o `python main.py` (en modo desarrollo).
4. **Errores**: Consultar `error.log` en el directorio de ejecución para diagnósticos detallados.
