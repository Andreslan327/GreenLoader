# GreenLoader V7.0

GreenLoader es una interfaz gráfica de alto rendimiento diseñada para la gestión y descarga de contenido multimedia desde diversas plataformas. Esta herramienta actúa como un puente visual optimizado para **yt-dlp**, permitiendo a los usuarios de Windows procesar videos y audios sin interactuar con líneas de comandos complejas.

En esta nueva versión, se ha migrado la arquitectura interna de Electron hacia un motor basado en **Python**, lo que garantiza una aplicación mucho más ligera, un consumo de recursos mínimo y una ejecución más fluida.

---

### Características Principales

* Descarga de contenido de video en formato MP4 con soporte para altas resoluciones.
* Conversión avanzada de audio a formato MP3 con bitrate de hasta 320kbps.
* Sistema de post-procesamiento para la inclusión automática de carátulas (miniaturas) en los archivos descargados.
* Organización inteligente de archivos en subcarpetas dedicadas para Audio y Video.
* Interfaz minimalista construida sobre tecnologías web, libre de publicidad y elementos distractores.
* Procesamiento interno mediante FFmpeg integrado para garantizar compatibilidad total.

---

### Detalles Técnicos de la Versión 7.0

* **Motor de Interfaz:** Python PyWebView (sustituyendo a Electron para mayor eficiencia).
* **Motor de Descarga:** yt-dlp.
* **Procesamiento Multimedia:** FFmpeg y FFprobe (integrados internamente).
* **Compatibilidad de Metadatos:** Inserción de miniaturas y etiquetas ID3 automática.

---

### Gestión de Archivos

Para evitar la pérdida de archivos en carpetas temporales, GreenLoader utiliza ahora la ruta estándar de usuario. Todas las descargas se almacenarán en la siguiente ubicación:

* **Ruta:** `C:\Usuarios\[TuUsuario]\Downloads\GreenLoader`

Dentro de este directorio, el sistema clasificará automáticamente los archivos en las carpetas **Audio** y **Video**.

---

### Requisitos del Sistema

* Sistema Operativo: Windows 10 o Windows 11 (recomendados).
* Espacio en disco: Mínimo 100MB para el ejecutable y componentes internos.
* Conexión a Internet estable.

---

### Instrucciones de Uso

1. Descargar el archivo ejecutable `GreenLoader_V7.exe`.
2. Ejecutar la aplicación (No requiere instalación previa).
3. Pegar los enlaces deseados en el área de texto.
4. Seleccionar el formato y la calidad preferida.
5. Iniciar el procesamiento y esperar la confirmación en pantalla.

---

### Créditos y Licencias

El funcionamiento de GreenLoader se basa en el poder de **yt-dlp**, un proyecto de código abierto mantenido por una comunidad global. 

* GreenLoader es únicamente una interfaz gráfica (GUI). No se modifica el código base de yt-dlp ni se reclama propiedad sobre su tecnología.
* Este software se distribuye de forma gratuita como un proyecto personal sin fines de lucro.
* Repositorio oficial de yt-dlp: https://github.com/yt-dlp/yt-dlp

---

### Desarrollador

* **Autor:** Andrés.
* **Propósito:** Proyecto personal enfocado en la optimización de descargas multimedia.