
# Metadata Filter Files

Este script de Python permite extraer metadatos de archivos DOCX, XLSX y PDF en un directorio dado

## Requisitos

- Python 3.x
- Bibliotecas: docx, openpyxl, PyPDF2

## Uso
- Instalar los requerimientos del archivo 
- Ejecutar el script con el python o python3 en su defecto
- Darle como parametro el directorio absoluto donde se encuentran sus archivos

## Ejemplo

Creamos un entorno virtual para el encapsulamiento de paquetes
```bash
  python3 -m venv .venv
```

Instalamos los requerimientos solicitados anteriormente

```bash
  pip install -r requirements.txt 
```

El directorio absoluto puede ser similar a esto -> /home/user/data

Ejecutamos el script de la siguiente forma

```bash
  python3 main.py <Directorio absoluto>
```

Obteniendo el siguiente resultado por cada archivo en consola

```bash
  Metadata for test1xlsx.xlsx:
  title: None
  author: Ikari Vargas
  created: 2024-03-22 15:56:32
  modified: 2024-03-22 15:57:30
```


## Autor

- [@PitaroDark](https://www.github.com/PitaroDark)
