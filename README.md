# Introducción
La Fórmula 1 es la máxima categoría del automovilismo mundial, donde la diferencia entre la victoria y la derrota suele medirse en milésimas de segundo. Si bien el rendimiento del vehículo y la habilidad del piloto son fundamentales, el trabajo en equipo durante las paradas en boxes (*pit stops*) representa un factor crítico en la estrategia de carrera. Entre los años 1994 y 2010, la Fórmula 1 atravesó una de sus épocas más dinámicas, caracterizada por la reintroducción y posterior prohibición del repostaje de combustible durante las carreras. Este trabajo de investigación tiene como propósito realizar un análisis estadístico exhaustivo sobre el conjunto de datos de paradas en boxes de la F1 en dicho periodo. A través del uso de herramientas computacionales en R, se busca descomponer la varianza de los tiempos de parada en función de factores como la escudería, el año y las estrategias de carrera.
## Estructura del Informe

Este documento técnico se encuentra estructurado en cinco capítulos fundamentales:

**Capítulo I**, se plantea la problemática de la eficiencia operativa en los boxes, formulando las preguntas de investigación y delimitando el alcance temporal y de variables del estudio.

**Capítulo II** establece el Marco Teórico, definiendo los conceptos estadísticos clave necesarios para la interpretación de los datos.

**Capítulo III** describe el Marco Metódico, detallando el proceso de limpieza de datos (ETL) y las pruebas utilizadas.

**Capítulo IV** presenta el Análisis de Resultados, donde se exhiben las tablas y gráficos generados dinámicamente.

**Capítulo V**, se exponen las Conclusiones y Recomendaciones del estudio.

Este reporte no solo pretende ofrecer una radiografía del pasado de la competencia, sino también establecer una metodología reproducible para el análisis descriptivo de grandes volúmenes de datos deportivos.
# Planteamiento del Problema
  En la Fórmula 1, el tiempo de permanencia en el *pit lane* es una variable de alto impacto que condiciona el resultado deportivo. Durante el ciclo 1994-2010, las reglas respecto a las operaciones permitidas en los boxes cambiaron drásticamente, siendo el más crítico la reintroducción y posterior prohibición del repostaje de combustible. El problema central de esta investigación consiste en evaluar, desde una perspectiva estadística, cómo evolucionaron los tiempos de estas paradas a lo largo de los años y determinar si existen diferencias significativas en la eficiencia operativa de las distintas escuderías. La ausencia de un modelo claro que cuantifique cómo estas variables categóricas impactan en el tiempo esperado de parada genera la necesidad de responder a las siguientes preguntas de investigación: 
1. ¿Cuál fue el tiempo promedio de las paradas en boxes durante el periodo de adaptación a las nuevas reglas (1994-1996)?
2. ¿Qué escudería (equipo) registró los tiempos de pit stop más rápidos en promedio durante ese trienio?
3. ¿Cuáles son las estrategias de paradas (1, 2 o 3 paradas) más predominantes a lo largo del periodo evaluado?

## Justificación 
La justificación de este trabajo de investigación reside en la necesidad de aplicar técnicas estadísticas rigurosas para comprender la eficiencia operativa en entornos de alta presión. Desde el punto de vista académico, este estudio aporta una metodología replicable utilizando R y LaTeX para el análisis exploratorio y descriptivo de bases de datos deportivas, sirviendo como material de referencia.

##Objetivos 

##Objetivo General: Analizar los patrones históricos y los factores determinantes en los tiempos de las paradas en boxes de la Fórmula 1 (1994-2010) para caracterizar el comportamiento de la eficiencia mecánica de las escuderías.

##Objetivos Específicos 
1. Calcular las medidas de tendencia central y dispersión (media, mediana y desviación estándar) de los tiempos de parada para los años 1994, 1995 y 1996. 
2. Identificar las escuderías con los menores tiempos promedio de parada mediante tablas de frecuencias y gráficos de barras. 
3. Analizar la distribución de frecuencias del número de paradas por piloto para identificar estrategias.
