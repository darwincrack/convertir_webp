# img2webp

Herramienta en Python para convertir imágenes a formato WEBP de manera masiva, con soporte para subcarpetas, control de calidad, exclusión de archivos, logs y más.

## Requisitos

- Python 3.7 o superior
- [Pillow](https://python-pillow.org/) (instalable con pip)

Instala las dependencias ejecutando:

```sh
pip install Pillow
```

## Uso

El script principal es `img2webp.py`. Puedes ejecutarlo desde la línea de comandos con diferentes opciones:

### Argumentos principales

- `--input` o `-i`: Carpeta de entrada donde están las imágenes a convertir (**obligatorio**)
- `--output` o `-o`: Carpeta de salida donde se guardarán las imágenes `.webp` (**obligatorio**)
- `--recursive` o `-r`: Procesa subcarpetas de manera recursiva (opcional)
- `--overwrite`: Sobrescribe archivos `.webp` existentes en la carpeta de salida (opcional)
- `--quality`: Calidad de compresión WEBP (1-100, por defecto 85) (opcional)
- `--log`: Ruta de archivo donde guardar el log de la conversión (opcional)
- `--exclude`: Uno o varios patrones para excluir archivos (puedes usar comodines tipo `*` y `?`) (opcional)

### Ejemplos de uso

#### Conversión básica

```sh
python img2webp.py -i img/redes/ -o img/redes/webp/
```

#### Conversión recursiva (incluye subcarpetas)

```sh
python img2webp.py -i img/redes/ -o img/redes/webp/ -r
```

#### Sobrescribir archivos existentes y ajustar calidad

```sh
python img2webp.py -i img/redes/ -o img/redes/webp/ --overwrite --quality 90
```

#### Excluir archivos por patrón

```sh
python img2webp.py -i img/redes/ -o img/redes/webp/ --exclude "*_old.png" "test*.jpg"
```

#### Guardar log de la conversión

```sh
python img2webp.py -i img/redes/ -o img/redes/webp/ --log conversion_log.txt
```

#### Combinando varias opciones

```sh
python img2webp.py -i img/redes/ -o img/redes/webp/ -r --overwrite --quality 80 --log conversion_log.txt --exclude "*_old.png" "test*.jpg"
```

## Notas

- El script solo convierte imágenes con extensiones `.jpg`, `.jpeg` y `.png`.
- Si usas la opción `--recursive`, la estructura de subcarpetas se mantiene en la carpeta de salida.
- Si no usas `--overwrite`, los archivos `.webp` ya existentes no se modificarán.
- Los patrones de exclusión usan la sintaxis de [fnmatch](https://docs.python.org/3/library/fnmatch.html) (comodines tipo shell).
- El log, si se especifica, se agrega al final del archivo indicado.

## Licencia

MIT 