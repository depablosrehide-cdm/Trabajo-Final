# Introducción
La Fórmula 1 es la máxima categoría del automovilismo mundial, donde la diferencia entre la victoria y la derrota suele medirse en milésimas de segundo. Si bien el rendimiento del vehículo y la habilidad del piloto son fundamentales, el trabajo en equipo durante las paradas en boxes (*pit stops*) representa un factor crítico en la estrategia de carrera. Entre los años 1994 y 2010, la Fórmula 1 atravesó una de sus épocas más dinámicas, caracterizada por la reintroducción y posterior prohibición del repostaje de combustible durante las carreras. Este trabajo de investigación tiene como propósito realizar un análisis estadístico exhaustivo sobre el conjunto de datos de paradas en boxes de la F1 en dicho periodo. A través del uso de herramientas computacionales en R y Python, se busca descomponer la varianza de los tiempos de parada en función de factores como la escudería, el año y las estrategias de carrera.
## Estructura del Informe

Este documento técnico se encuentra estructurado en cinco capítulos fundamentales:

**Capítulo I**, se plantea la problemática de la eficiencia operativa en los boxes, formulando las preguntas de investigación y delimitando el alcance temporal y de variables del estudio.

**Capítulo II** establece el Marco Teórico, definiendo los conceptos estadísticos clave necesarios para la interpretación de los datos.

**Capítulo III** describe el Marco Metódico, detallando el proceso de limpieza de datos (ETL) y las pruebas utilizadas.

**Capítulo IV** presenta el Análisis de Resultados, donde se exhiben las tablas y gráficos generados dinámicamente.

**Capítulo V**, se exponen las Conclusiones y Recomendaciones del estudio.

Este reporte no solo pretende ofrecer una radiografía del pasado de la competencia, sino también establecer una metodología reproducible para el análisis descriptivo de grandes volúmenes de datos deportivos.
# Planteamiento del Problema
  En la Fórmula 1, el tiempo de permanencia en el pit lane es una variable de alto impacto que condiciona el resultado deportivo. Durante el ciclo 1994-2010, las reglas respecto a las operaciones permitidas en los boxes cambiaron drásticamente, siendo el más crítico la reintroducción y posterior prohibición del repostaje de combustible. El problema central de esta investigación consiste en evaluar, desde una perspectiva estadística, la eficiencia operativa de las distintas escuderías durante el periodo de adaptación a estas normativas de repostaje (1994-1996). La ausencia de un modelo claro que cuantifique cómo estas variables categóricas impactan en el tiempo esperado de parada genera la necesidad de responder a las siguientes preguntas de investigación: 
1. ¿Existen diferencias significativas en los tiempos de parada al comparar el primer *pit stop* de un vehículo con su segunda parada en boxes?
2. ¿Qué escudería demostró ser la más eficiente y registró los tiempos promedio de parada más rápidos durante este periodo?
3. ¿Cuáles son las estrategias de paradas (1, 2 o 3 paradas) más predominantes a lo largo del periodo evaluado?

## Justificación 
El análisis temporal de las paradas en boxes trasciende el ámbito puramente deportivo; representa un caso de estudio ideal sobre cómo los equipos de alto rendimiento optimizan procesos bajo condiciones de extrema presión y variabilidad. Se justifica esta investigación en la oportunidad de aplicar modelos de estadística descriptiva (medidas de tendencia central y dispersión) y análisis de distribuciones de frecuencias para cuantificar el impacto real que tienen los cambios de normativas externas (como la reintroducción del repostaje de combustible) sobre los tiempos de ejecución mecánica. Desde la perspectiva académica, este trabajo permite demostrar la utilidad de lenguajes como R, Python y LaTeX para depurar, transformar y extraer conclusiones significativas a partir de registros cronométricos crudos, consolidando habilidades prácticas en la ejecución de un riguroso Análisis Exploratorio de Datos (EDA), el manejo de distribuciones asimétricas y la interpretación de diagramas de caja y barras.

## Objetivos 

## Objetivo General: 
Analizar los patrones históricos y los factores determinantes en los tiempos de las paradas en boxes de la Fórmula 1 (1994-2010) para caracterizar el comportamiento de la eficiencia mecánica de las escuderías.

## Objetivos Específicos 
1. Comparar los tiempos registrados según el orden de la parada (primera parada vs. segunda parada) para analizar las razones estadísticas por las cuales una de las dos paradas tiende a tener menor tiempo.
2. Describir la influencia de la variable escudería en la distribución de los tiempos de los pit stops.
3. Analizar la distribución de frecuencias del número de paradas por piloto para identificar estrategias.
