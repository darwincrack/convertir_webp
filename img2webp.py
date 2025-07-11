from PIL import Image, UnidentifiedImageError
import os
import argparse
import fnmatch
from datetime import datetime

# Argumentos CLI
parser = argparse.ArgumentParser(description="Convierte imágenes a formato WEBP.")
parser.add_argument('--input', '-i', type=str, required=True, help='Carpeta de entrada')
parser.add_argument('--output', '-o', type=str, required=True, help='Carpeta de salida')
parser.add_argument('--recursive', '-r', action='store_true', help='Procesar subcarpetas recursivamente')
parser.add_argument('--overwrite', action='store_true', help='Sobrescribir archivos .webp existentes')
parser.add_argument('--quality', type=int, default=85, help='Calidad de compresión WEBP (1-100, por defecto 85)')
parser.add_argument('--log', type=str, help='Archivo donde guardar el log de la conversión')
parser.add_argument('--exclude', type=str, nargs='*', default=[], help='Patrones de archivos a excluir (ej: "*_old.png" "test*.jpg")')
args = parser.parse_args()

input_folder = args.input
output_folder = args.output
os.makedirs(output_folder, exist_ok=True)

extensiones = (".jpg", ".jpeg", ".png")
procesadas = 0
fallidas = []
log_lines = []

# Función para saber si un archivo debe excluirse
def esta_excluido(filename, patrones):
    for patron in patrones:
        if fnmatch.fnmatch(filename, patron):
            return True
    return False

# Función para procesar archivos
def procesar_archivos():
    global procesadas, fallidas
    if args.recursive:
        for root, _, files in os.walk(input_folder):
            for filename in files:
                if filename.lower().endswith(extensiones) and not esta_excluido(filename, args.exclude):
                    ruta_rel = os.path.relpath(root, input_folder)
                    carpeta_salida = os.path.join(output_folder, ruta_rel)
                    os.makedirs(carpeta_salida, exist_ok=True)
                    convertir_imagen(os.path.join(root, filename), carpeta_salida, filename)
    else:
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(extensiones) and not esta_excluido(filename, args.exclude):
                convertir_imagen(os.path.join(input_folder, filename), output_folder, filename)

def convertir_imagen(img_path, carpeta_salida, filename):
    global procesadas, fallidas
    webp_name = os.path.splitext(filename)[0] + ".webp"
    webp_path = os.path.join(carpeta_salida, webp_name)
    if os.path.exists(webp_path) and not args.overwrite:
        mensaje = f"⚠️ Ya existe (omitido): {webp_name}"
        print(mensaje)
        log_lines.append(mensaje)
        return
    try:
        with Image.open(img_path) as img:
            img.save(webp_path, "WEBP", quality=args.quality)
            mensaje = f"✅ Convertido: {filename} → {webp_name}"
            print(mensaje)
            log_lines.append(mensaje)
            procesadas += 1
    except UnidentifiedImageError:
        mensaje = f"❌ ERROR: No se pudo abrir como imagen → {filename}"
        print(mensaje)
        log_lines.append(mensaje)
        fallidas.append(filename)
    except Exception as e:
        mensaje = f"❌ ERROR inesperado con {filename}: {e}"
        print(mensaje)
        log_lines.append(mensaje)
        fallidas.append(filename)

procesar_archivos()

# Resumen final
resumen = [
    "\n--- RESUMEN ---",
    f"Imágenes convertidas correctamente: {procesadas}",
    f"Imágenes con error: {len(fallidas)}"
]
print("\n".join(resumen))
log_lines.extend(resumen)

if fallidas:
    log_lines.append("Lista de imágenes con error:")
    for f in fallidas:
        log_lines.append(f" - {f}")
        print(f" - {f}")

# Guardar log si se pidió
if args.log:
    try:
        with open(args.log, 'a', encoding='utf-8') as logf:
            logf.write(f"\n--- LOG {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            for line in log_lines:
                logf.write(line + '\n')
        print(f"\n📝 Log guardado en: {args.log}")
    except Exception as e:
        print(f"❌ No se pudo guardar el log: {e}") 