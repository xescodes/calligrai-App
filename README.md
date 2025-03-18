# Challigrai

Challigrai es una aplicación web de escritura asistida por IA que inspira a los usuarios en su proceso creativo. La aplicación ofrece una interfaz limpia y moderna con capacidades de generación de texto impulsadas por la IA de Qwen 2.5 Max.

## Características

- Interfaz web moderna y responsive
- Barra de herramientas con:
  - Menú de archivo (Nuevo, Abrir, Guardar)
  - Selector de tono de escritura
- Editor de texto principal
- Área para mostrar el texto generado por la IA
- Atajo de teclado Ctrl+Enter para generar texto
- Soporte para cargar y guardar archivos de texto
- Diseño responsive que funciona en dispositivos móviles

## Requisitos

- Python 3.8 o superior
- Conexión a Internet (para la API de Qwen)

## Instalación

1. Clona el repositorio o descarga los archivos
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Inicia el servidor Flask:
```bash
python app.py
```

2. Abre tu navegador y visita:
```
http://localhost:5000
```

3. Comienza a escribir en el editor principal
4. Selecciona un tono del menú desplegable para generar texto inspirado
5. Usa los botones de la barra de herramientas para:
   - Crear un nuevo documento
   - Abrir un archivo de texto existente
   - Guardar tu trabajo

## Tecnologías Utilizadas

- Backend: Flask (Python)
- Frontend: HTML5, CSS3, JavaScript
- IA: Qwen 2.5 Max API
- Estilos: CSS personalizado con variables CSS
- Fuentes: Roboto de Google Fonts

## Notas

- La aplicación requiere una conexión a Internet para funcionar con la API de Qwen
- Los archivos se guardan en formato .txt
- El texto generado por la IA se muestra en un área separada debajo del editor principal 