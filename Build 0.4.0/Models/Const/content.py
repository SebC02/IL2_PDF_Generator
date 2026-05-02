# =============================================================================
# content.py
# Textos del manual como constantes organizadas por sección.
# Para editar el contenido textual, modificar SOLO este archivo.
# Los textos admiten etiquetas HTML básicas de ReportLab: <b>, <i>, <br/>.
# =============================================================================


# ── Encabezado y pie de página ────────────────────────────────────────────────
HEADER_TEXT  = "ACADEMIA DE COMBATE 250H  —  N.º 1  —  TAXI, DESPEGUE Y ATERRIZAJE: CAZAS"
FOOTER_TEXT  = "DOCUMENTO DE USO INTERNO — Unidad Aerea - 250 Hispana"
DOC_SUBTITLE = "MANUAL DE INSTRUCCIÓN N.º 1"
DOC_SERIES   = "ACADEMIA DE COMBATE 250H"
DOC_SUBJECT  = "Taxi, Despegue y Aterrizaje: Cazas"
DOC_CLOSING  = "Academia de Combate 250H  ·  Manual N.º 1  ·  IL-2 Great Battles"
DOC_END      = "— FIN DEL DOCUMENTO —"
DOC_EPILOGUE = "Este documento es el primero de la serie Academia de Combate 250H.<br/>"


# ── Introducción ──────────────────────────────────────────────────────────────
class Intro:
    """
    Contiene el contenido textual de la sección de Introducción del manual.
    
    Similar a una clase estática en C# con constantes. Agrupa todos los textos
    relacionados con la introducción para mantenerlos organizados y facilitar
    modificaciones.
    
    Atributos:
    - TITLE: Título de la sección
    - PARRAFO_1, PARRAFO_2, PARRAFO_3: Contenido de párrafos
    - AVIONES_TITULO: Título de la lista de aviones
    - AVIONES: Lista de aviones recomendados
    
    Arquitectura: Separa el contenido del formato, permitiendo traducciones
    o cambios de texto sin afectar la lógica de presentación.
    """
    TITLE = "I. PROPÓSITO DEL DOCUMENTO"

    PARRAFO_1 = (
        "El presente manual constituye el primer documento de instrucción formal de la "
        "Academia de Combate 250H, destinado a pilotos en formación que operan aeronaves "
        "de caza en el entorno del simulador <b>IL-2 Great Battles</b>. Su contenido cubre "
        "los procedimientos fundamentales de rodaje (taxi), despegue y aterrizaje aplicables "
        "a los aviones caza"
    )

    PARRAFO_2 = (
        "Este documento ha sido redactado sobre la base de <b>experiencia práctica acumulada</b>, "
        "Toda instrucción contenida en estas páginas ha sido verificada sesiones de practica "
        "con diversos modelos de caza"
    )

    PARRAFO_3 = (
        "El avión de referencia principal es el <b>Spitfire Mk XIV</b>, seleccionado por su "
        "marcada sensibilidad al torque, al prop-wash y a su tendencia a los trompos. Lo "
        "aprendido en esta aeronave es transferible a cualquier caza del período."
    )

    AVIONES_TITULO = "AVIONES RECOMENDADOS PARA ENTRENAMIENTO:"

    AVIONES = [
        "<b>Primario:</b> Spitfire (cualquier variante disponible, preferentemente Mk XIV).",
        "<b>Alternativo:</b> Bf-109 (sin bloquear rueda de cola), Fw-190 (ídem).",
        "<b>Otros válidos:</b> MiG-3, Yak-1B.",
    ]


# ── Sección I — Rodaje ────────────────────────────────────────────────────────
class Taxi:
    SECTION_TITLE = "SECCIÓN I — RODAJE (TAXI)"

    # 1.1
    SUB_CABECERA  = "1.1  ELECCIÓN DE CABECERA"
    CABECERA_BODY = (
        "Antes de iniciar el rodaje, el piloto determinará la cabecera a utilizar. "
        "La regla general es simple: seleccionar la cabecera más cercana a la posición "
        "actual de la aeronave."
    )
    CABECERA_APUNTE = (
        "En la vida real, el despegue se realiza siempre contra el viento. En el simulador "
        "este factor es irrelevante para la instrucción básica, ya que en el simulador no "
        "sentimos con fuerza; nos permitimos esta licencia."
    )

    # 1.2
    SUB_PROCEDIMIENTO  = "1.2  PROCEDIMIENTO DE RODAJE"
    PROCEDIMIENTO_BODY = (
        "El procedimiento de taxi exige control permanente y movimientos suaves. "
        "El principal accidente en tierra es el trompo descontrolado. Para evitarlo:"
    )
    PROCEDIMIENTO_BULLETS = [
        "Aplicar potencia de manera <b>gradual y suave</b>. Nunca de golpe.",
        (
            "Mantener las RPM entre <b>1.200 y 1.300 RPM</b> durante todo el rodaje. "
            "Este rango garantiza autoridad de timón sin exceso de velocidad."
        ),
        (
            "Conocer la ubicación del <b>TACÓMETRO</b> en el tablero del avión que nos "
            "encontramos es INDISPENSABLE para esto, NO CONFIAR EN EL TECNOCHAT. "
            "Si no se conoce la ubicacion del mismo, tomarse el tiempo de estudiar la cabina."
        ),
        (
            "Utilizar <b>frenos y timón de dirección</b> para guiar la aeronave. "
            "Bloquear la rueda de cola cuando se ruede en línea recta; desbloquear para girar."
        ),
        (
            "<b>No cortar la potencia completamente</b> durante el taxi. Esto provocara una "
            "reduccion del prop-wash en el timón reduciendo la capacidad de respuesta a un "
            "trompo, en aviones como el Spitfire, el efecto es tan fuerte que puede resultar "
            "en trompos sin control."
        ),
    ]
    FIG_1_CAPTION = "FIG. 1 — Tacómetro indicando el rango operativo de rodaje: 1.200–1.300 RPM."

    # 1.3
    SUB_RIESGOS  = "1.3  RIESGOS COMUNES EN RODAJE"
    RIESGOS_BULLETS = [
        "Exceso de velocidad por potencia elevada sin uso de frenos.",
        "Pérdida de autoridad de timón al cortar totalmente el motor.",
        "Trompo al girar con rueda de cola bloqueada.",
        "Mala aplicacion de frenos para dirigir el avion, resultando en trompo.",
    ]
    RIESGOS_APUNTE = (
        "El Spitfire Mk XIV es el avión que con mayor fidelidad reproduce los efectos del "
        "torque y el prop-wash durante el taxi. Su dominio en tierra garantiza la transferencia "
        "de habilidades a cualquier otra aeronave de caza del período."
    )


# ── Sección II — Despegue ─────────────────────────────────────────────────────
class Despegue:
    SECTION_TITLE = "SECCIÓN II — DESPEGUE"

    # 2.1
    SUB_PREP  = "2.1  PREPARACIÓN PREVIA AL DESPEGUE"
    PREP_BODY = (
        "Antes de solicitar permiso de despegue y aplicar potencia, el piloto verificará "
        "los siguientes puntos:"
    )
    PREP_BULLETS = [
        (
            "Verificar que las <b>RPM estén correctamente ajustadas</b> para el despegue, "
            "si el avión no posee control automático de hélice. En el caso contrario, no hay "
            "que preocuparse, esto aplica principalmente a aeronaves alemanas y al "
            "<b>Spitfire Mk XIV \"Teardrop\" como el utilizado en este ejemplo, aunque se lo "
            "colocó en control manual para la documentacion del manual</b>."
        ),
        (
            "<b>Flaps:</b> No son necesarios para el despegue en condiciones normales. "
            "Los Spitfire y Yak no disponen de posiciones intermedias de flap; sus flaps "
            "son de despliegue total y están reservados para el aterrizaje."
        ),
        (
            "Excepción de flaps en despegue: pista muy corta con obstáculo inmediato "
            "(bosque, edificación). En ese caso, <b>20° de flap</b> son ideales y aplicables "
            "a cualquier despegue con pista comprometida."
        ),
    ]
    FIG_2_CAPTION = (
        "FIG. 2 — Caza con carga de bombas: única condición que justifica el uso de flaps "
        "en despegue."
    )

    # 2.2
    SUB_PROC  = "2.2  PROCEDIMIENTO DE DESPEGUE"
    PROC_BODY = (
        "Una vez alineado en cabecera y con todos los parámetros verificados, se procederá "
        "del siguiente modo:"
    )
    PROC_BULLETS = [
        (
            "<b>Paso 1 — Potencia:</b> Utilizar como maximo el <b>MODO COMBATE</b>. No utilizar "
            "WEP (Emergencia) para el despegue. La única justificación para WEP sería una carga "
            "máxima de bombas en pista corta."
        ),
        (
            "<b>Paso 2 — Aplicación de potencia:</b> Avanzar el acelerador de manera "
            "<b>progresiva y firme</b>. Ni lenta ni de golpe. Una aplicación repentina al "
            "máximo puede sobrerevolucionar el motor si las RPM están al tope."
        ),
        (
            "<b>Paso 3 — Control de torque:</b> Simultáneamente, contrarrestar con timón de "
            "dirección la tendencia natural del avión a desviarse. La dirección varía según "
            "el tipo de aeronave."
        ),
        (
            "<b>Paso 4 — Rueda de cola:</b> A medida que se gana velocidad, la rueda de cola "
            "se levantará del suelo <b>sin necesidad de empujar la palanca</b>. Este momento "
            "indica que el avión está próximo a la velocidad de despegue."
        ),
        (
            "<b>Paso 5 — Rotación:</b> De forma <b>suave</b>, tirar de la palanca para entrar "
            "en vuelo. Sin movimientos abruptos."
        ),
    ]
    FIG_3_CAPTION = (
        "FIG. 3 — Modo Combate seleccionado para el despegue. El modo Emergencia (WEP) "
        "no se emplea."
    )
    FIG_4_CAPTION = (
        "FIG. 4 — La rueda de cola se levanta naturalmente al alcanzar velocidad suficiente, "
        "sin intervención del piloto."
    )
    FIG_5_CAPTION = (
        "FIG. 5 — El despegue debe ser suave en los comandos. La rotación brusca es uno de "
        "los errores más frecuentes."
    )

    # 2.3
    SUB_ERRORES  = "2.3  ERRORES COMUNES EN DESPEGUE"
    ERRORES_BODY = "Los errores en el despegue se agrupan en tres perfiles de piloto:"

    ERROR_A_TITLE  = "<b>A. Inseguridad con el avion. </b>"
    ERROR_A_APUNTE = (
        "Es frecuente observar pilotos novatos que suben la potencia muy despacio y se "
        "desconcentran con el torque. Al enfocarse en el torque, olvidan continuar aumentando "
        "potencia para ganar velocidad y autoridad de timón. El resultado es la pérdida de "
        "control antes de despegar."
    )
    ERROR_A_BULLETS = [
        "Sube la palanca de potencia demasiado lento.",
        "Se distraen con el torque y olvidan aumentar la potencia.",
        "No alcanzan velocidad suficiente para tener autoridad de timón.",
        "Pierden el control antes de levantar vuelo.",
    ]

    ERROR_B_TITLE   = "<b>B. Impulsividad (Potencia Excesiva / Brusca)</b>"
    ERROR_B_BULLETS = [
        "Aplica potencia máxima de golpe.",
        (
            "Con las RPM ajustadas al máximo, un avance súbito puede "
            "<b>sobrerevolucionar el motor</b> y dañarlo irreparablemente. Y aunque esto no "
            "esta reflejado, en la realidad esto podria terminar en que el avion se da vuelta."
        ),
        "El mayor riesgo en este error, es romper el motor, o dañarlo gravemente.",
    ]

    ERROR_C_TITLE   = "<b>C. Uso Incorrecto del WEP (Emergencia)</b>"
    ERROR_C_WARNING = (
        "NO utilizar WEP (Modo Emergencia) para el despegue en condiciones normales. "
        "Esta potencia no es necesaria y puede comprometer la vida útil del motor. "
        "Su uso sólo se justifica con carga máxima de bombas en pista corta."
    )


# ── Sección III — Aterrizaje ──────────────────────────────────────────────────
class Aterrizaje:
    SECTION_TITLE = "SECCIÓN III — ATERRIZAJE"

    # 3.1
    SUB_GENERAL  = "3.1  CONSIDERACIÓN GENERAL"
    GENERAL_BODY = (
        "Existen múltiples procedimientos de aterrizaje válidos. Este manual describe "
        "<b>uno específico</b>, diseñado para minimizar el tiempo de exposición en el circuito "
        "de aproximación, dado que toda aeronave en vuelo a baja velocidad y baja altura "
        "representa un blanco potencial para el enemigo."
    )
    GENERAL_APUNTE = (
        "En lugar de seguir un patrón de tránsito estándar, que consume tiempo y expone "
        "innecesariamente la aeronave, se describe aquí una maniobra de desaceleración rápida, "
        "y recordad, utilizamos esta maniobra para evitar riesgos de atacques. "
        "La probabilidad de ataque nunca es cero."
    )
    GENERAL_WARNING = (
        "Si la aeronave está dañada: ATERRIZA COMO PUEDAS. Sin importar la cabecera, sin "
        "importar la dirección. La prioridad es salvar la aeronave y al piloto."
    )

    # 3.2
    SUB_MANIOBRA  = "3.2  MANIOBRA DE ATERRIZAJE — PROCEDIMIENTO PASO A PASO"
    MANIOBRA_BODY = (
        "A continuación se detalla la secuencia completa, ordenada desde la fase inicial "
        "hasta el toque en pista:"
    )

    FASE1_TITLE   = "<b>FASE 1 — Localización y aproximación directa</b>"
    FASE1_BULLETS = [
        "Divisar la pista y determinar la cabecera de aterrizaje.",
        "Dirigirse hacia la pista de <b>forma directa</b>. No realizar patrón de aproximación estándar.",
    ]
    FIG_6_CAPTION = (
        "FIG. 6 — Posición de la aeronave respecto a la pista al inicio de la maniobra "
        "(vista exterior)."
    )
    FIG_7_CAPTION = "FIG. 7 — Misma posición desde la visión del piloto en cabina."

    FASE2_TITLE   = "<b>FASE 2 — Pasada sobre pista (descenso inicial)</b>"
    FASE2_BULLETS = [
        (
            "Al llegar sobre la pista o muy próximo a la cabecera elegida, "
            "<b>cortar la potencia del motor</b>, manteniendo las RPM al máximo."
        ),
        "En aeronaves con control automático de hélice, iniciar el control manual de RPM en este momento.",
        (
            "Iniciar un <b>descenso pronunciado</b> hacia la pista. El objetivo no es aterrizar "
            "en esta pasada, sino realizar un paso de baja altura de cabecera a cabecera, con "
            "margen suficiente para maniobrar."
        ),
        "La altura mínima de esta pasada es baja, pero no excesivamente. Debe existir margen de maniobra.",
    ]
    FIG_8_CAPTION  = "FIG. 8 — Corte de potencia para iniciar el descenso abrupto sobre la pista."
    FIG_9_CAPTION  = "FIG. 9 — El descenso es pronunciado. Vista desde cabina."
    FIG_10_CAPTION = "FIG. 10 — Vista exterior del descenso abrupto hacia la cabecera."
    FIG_11_CAPTION = "FIG. 11 — La altura mínima de la pasada es baja, pero con margen operativo."

    FASE3_TITLE   = "<b>FASE 3 — Giro de 180° en la segunda cabecera</b>"
    FASE3_BULLETS = [
        (
            "Al llegar al extremo opuesto de la pista, con el motor cortado, ejecutar un "
            "<b>giro de 180°</b> lo más abrupto posible."
        ),
        (
            "Este giro tiene por objeto <b>quemar la energía restante</b> y dejar la aeronave "
            "en condiciones de velocidad apropiadas para el aterrizaje."
        ),
    ]
    FIG_12_CAPTION = (
        "FIG. 12 — El giro en la segunda cabecera debe ser suficientemente abrupto para "
        "perder energía."
    )

    FASE4_TITLE   = "<b>FASE 4 — Configuración de flaps y gestión de potencia</b>"
    FASE4_BULLETS = [
        (
            "Una vez completado el giro, comenzar a <b>bajar los flaps a la posición de "
            "aterrizaje</b> (despliegue máximo en la mayoría de los aviones)."
        ),
        (
            "Para evitar entrar en pérdida (stall) con flaps desplegados, "
            "<b>aumentar suavemente la potencia</b> para mantener una velocidad muy baja "
            "pero controlada."
        ),
    ]
    FIG_13_CAPTION = (
        "FIG. 13 — Bajada de flaps de camino hacia la segunda cabecera, para configurar "
        "la aeronave para el aterrizaje."
    )

    FASE5_TITLE   = "<b>FASE 5 — Aproximación final</b>"
    FASE5_BULLETS = [
        "Sobrepasar la cabecera de destino y ejecutar el <b>giro final</b> para encarar la pista en aproximación.",
        (
            "Durante este giro, regular con cuidado la potencia. Un aumento brusco a baja "
            "velocidad puede hacer que el torque voltee la aeronave."
        ),
        "Una vez encarados con la pista, bajar el <b>tren de aterrizaje</b>.",
        (
            "Descender gradualmente hacia pista, <b>reduciendo potencia de forma progresiva</b> "
            "mientras se aproxima a la cabecera."
        ),
    ]
    FIG_14_CAPTION = "FIG. 14 — Encarando la pista en aproximación final. Tren de aterrizaje bajando."
    FIG_15_CAPTION = "FIG. 15 — Aproximación final a baja velocidad, pista encuadrada."
    FIG_16_CAPTION = (
        "FIG. 16 — Ajuste suave de potencia en la aproximación final para sostener la "
        "velocidad y evitar la pérdida."
    )

    FASE6_TITLE   = "<b>FASE 6 — Toque y rodaje de parada</b>"
    FASE6_BULLETS = [
        (
            "Al llegar a la cabecera y estar muy próximo al suelo, <b>cortar la potencia</b> "
            "y realizar un <b>aterrizaje de tres puntos</b>: las dos ruedas principales y la "
            "rueda de cola tocan simultáneamente."
        ),
        (
            "Es normal no ver la pista en este momento: el morro levantado bloquea la visión "
            "frontal. Sin potencia, el avión descenderá por su propio peso."
        ),
        (
            "<b>Excepción Spitfire:</b> No cortar totalmente la potencia al tocar. Mantener "
            "un mínimo (aprox. 1.200 RPM) para evitar el trompo al contacto."
        ),
        (
            "Una vez en tierra, aplicar <b>frenos de forma progresiva</b>. No clavar de punta. "
            "Aeronaves propensas al vuelco: La-5, La-7, P-51, P-47."
        ),
    ]
    FIG_17_CAPTION = (
        "FIG. 17 — Al llegar a la cabecera, se corta la potencia y se levanta el morro "
        "para el aterrizaje de tres puntos."
    )

    # 3.3
    SUB_FALLOS  = "3.3  FALLOS FRECUENTES EN ATERRIZAJE"
    FALLOS_BULLETS = [
        "<b>Aterrizaje en cabecera incorrecta:</b> Salvo emergencia, siempre aterrizar en la cabecera activa.",
        (
            "<b>Descenso insuficientemente pronunciado:</b> Si la pasada inicial no es "
            "suficientemente baja, el avión llega con demasiada energía al giro final."
        ),
        (
            "<b>Giro en segunda cabecera demasiado suave:</b> El avión no pierde suficiente "
            "energía y llega rápido a la aproximación final."
        ),
        (
            "<b>Aumento brusco de potencia en el giro final:</b> El torque a baja velocidad "
            "puede hacer virar violentamente la aeronave hacia el suelo."
        ),
        (
            "<b>Pánico ante el rebote:</b> Si el avión rebota al tocar, NO actuar sobre los "
            "mandos. No empujar ni tirar la palanca. Dejar que el avión termine el rebote "
            "por sí solo."
        ),
        (
            "<b>Frenos excesivos:</b> En los aviones señalados (La-5, La-7, P-51, P-47), "
            "los frenos agresivos pueden volcar la aeronave sobre el morro."
        ),
    ]
    FALLOS_WARNING = (
        "GO-AROUND OBLIGATORIO: Si al finalizar la maniobra el piloto advierte que no "
        "dispondrá de pista suficiente para detenerse, aplicar INMEDIATAMENTE potencia "
        "de combate y ejecutar una nueva aproximación completa."
    )


# ── Apuntes finales ───────────────────────────────────────────────────────────
class NotasFinales:
    SECTION_TITLE = "APUNTES FINALES A CONSIDERAR."

    PARRAFO_1 = (
        "El dominio de los procedimientos descritos en este manual, de aplicarse bien "
        "lograra que cualquier persona iniciando en el simulador pueda sobrellevar los "
        "despegues y aterrizajes"
    )

    PARRAFO_2 = (
        "Consideracion final: Si doman el Spitfire, reaplicar los conceptos en otros "
        "cazas es sencillo."
    )

    PRINCIPIOS_TITULO = "RESUMEN DE PRINCIPIOS FUNDAMENTALES:"
    PRINCIPIOS = [
        "Suavidad en los mandos. Siempre.",
        "La potencia es progresiva, nunca de golpe.",
        "El torque se contrarresta, no se ignora.",
        "El tiempo en el aire durante el aterrizaje es riesgo. Minimizarlo.",
        "Si duda en el aterrizaje: Go-Around. Siempre hay otra oportunidad.",
        "Si el avión está dañado: aterrizar como sea, donde sea.",
        "Un rebote no es un accidente. Pánico sobre el rebote sí lo es.",
    ]
