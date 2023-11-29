# convert_itrf

## Convertir Coordenadas y Velocidades a ITRF
Este script en Python toma datos de estaciones y transforma las coordenadas y velocidades de un sistema de referencia a otro, en este caso, de un sistema de referencia local a ITRF (International Terrestrial Reference Frame).

# Requisitos
Asegúrate de tener instaladas las siguientes bibliotecas de Python:

bash
Copy code
pip install matplotlib numpy
# Uso
Coloca los datos de las estaciones en el archivo stations.txt.
Asegúrate de tener el archivo Transfo-ITRF2014_ITRFs.txt en la carpeta docs.
Ejecuta el script.
bash
Copy code
python nombre_del_script.py
# Descripción
El script lee datos de estaciones desde stations.txt y realiza transformaciones de coordenadas y velocidades del sistema local a ITRF utilizando información del archivo Transfo-ITRF2014_ITRFs.txt. Los resultados se imprimen en la consola.

Nota: Asegúrate de tener los datos de entrada correctamente formateados en stations.txt.

Para más detalles sobre la implementación y los resultados, revisa el código fuente.

¡Espero que encuentres útil este script!
