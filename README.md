# img2webp

Herramienta en Python para convertir imágenes a formato WEBP de manera masiva, con soporte para subcarpetas, control de calidad, exclusión de archivos, logs y más.

## Requisitos

- Python 3.7 o superior (solo si usas el script Python)
- [Pillow](https://python-pillow.org/) (instalable con pip)

## ¡Ejecutable listo para usar!

En este repositorio encontrarás el archivo **`img2webp.exe`** dentro de la carpeta `dist/`.

- Puedes usar este ejecutable directamente en Windows **sin necesidad de instalar Python** ni dependencias.
- Solo necesitas copiar `img2webp.exe` a la carpeta donde tengas tus imágenes o a cualquier ubicación de tu preferencia.

---

## Uso del ejecutable

Abre una terminal (cmd o PowerShell), navega a la carpeta donde está `img2webp.exe` y ejecuta los siguientes comandos según tu caso:

### 1. Convertir todas las imágenes de la carpeta actual y guardar en una subcarpeta

```sh
img2webp.exe -i . -o salida
```

Esto convierte todas las imágenes compatibles de la carpeta actual y guarda los `.webp` en la subcarpeta `salida`.

### 2. Convertir imágenes de una carpeta específica a otra carpeta

```sh
img2webp.exe -i C:\ruta\a\mis_imagenes -o C:\ruta\a\salida
```

### 3. Procesar subcarpetas recursivamente

```sh
img2webp.exe -i . -o salida -r
```

### 4. Sobrescribir archivos existentes y ajustar calidad

```sh
img2webp.exe -i . -o salida --overwrite --quality 90
```

### 5. Excluir archivos por patrón

```sh
img2webp.exe -i . -o salida --exclude "*_old.png" "test*.jpg"
```

### 6. Guardar log de la conversión

```sh
img2webp.exe -i . -o salida --log conversion_log.txt
```

### 7. Convertir imágenes de una subcarpeta específica y guardar en otra

```sh
img2webp.exe -i imagenes_originales -o webp_convertidas
```

---

## Uso del script Python (opcional)

Si prefieres usar el script Python, instala las dependencias ejecutando:

```sh
pip install Pillow
```

Y luego ejecuta:

```sh
python img2webp.py -i carpeta/entrada -o carpeta/salida
```

---

## Argumentos principales

- `--input` o `-i`: Carpeta de entrada donde están las imágenes a convertir (**obligatorio**)
- `--output` o `-o`: Carpeta de salida donde se guardarán las imágenes `.webp` (**obligatorio**)
- `--recursive` o `-r`: Procesa subcarpetas de manera recursiva (opcional)
- `--overwrite`: Sobrescribe archivos `.webp` existentes en la carpeta de salida (opcional)
- `--quality`: Calidad de compresión WEBP (1-100, por defecto 85) (opcional)
- `--log`: Ruta de archivo donde guardar el log de la conversión (opcional)
- `--exclude`: Uno o varios patrones para excluir archivos (puedes usar comodines tipo `*` y `?`) (opcional)

---

## Notas

- El script y el ejecutable solo convierten imágenes con extensiones `.jpg`, `.jpeg` y `.png`.
- Si usas la opción `--recursive`, la estructura de subcarpetas se mantiene en la carpeta de salida.
- Si no usas `--overwrite`, los archivos `.webp` ya existentes no se modificarán.
- Los patrones de exclusión usan la sintaxis de [fnmatch](https://docs.python.org/3/library/fnmatch.html) (comodines tipo shell).
- El log, si se especifica, se agrega al final del archivo indicado.

## Licencia

MIT 