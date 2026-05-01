# TODO

## v0.5.0 (Interfaz de Usuario)
- [ ] Implementar GUI (usando CustomTkinter) para edición visual del manual.
- [ ] Crear editor de estructura jerárquica para `content.yaml`.
- [ ] Crear editor de activos para `assets.yaml`.
- [ ] Implementar panel de ajuste visual para `styles.py` (colores, fuentes, márgenes).
- [ ] Integrar botón "Generar PDF" dentro de la propia interfaz.

## v1.0.0
- [ ] Implementar generación condicional de documentos basada en keys: "USA", "UK", "USSR", "GER".
- [ ] Aplicar estilos personalizados dinámicos según el tipo de documento seleccionado.
- [ ] Generación de partes específicas del manual según la aeronave/nación indicada.

## v0.4.0
- [x] Generar archivo ejecutable (distribuible) que permita generar el PDF sin necesidad de entorno Python local.

## v0.3.0
- [x] Implementar sistema de configuración externo para la carga de imágenes (assets/images).
- [x] Eliminar dependencia de `config.py` para el registro de rutas de imágenes.

## v0.2.1
- [x] Restauración completa de secciones integradas dinámicamente.
- [x] Corrección de bug en renderizado de imágenes (tipos y redimensionamiento).
- [x] Versionado del proyecto (Git inicial).

## v0.2.0
- [x] Implementación de configuración desacoplada (YAML).
- [x] Creación de YAMLBuilder.

