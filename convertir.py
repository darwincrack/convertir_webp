from PIL import Image
import os

# Carpeta de entrada y salida
input_folder = "img/redes/"
output_folder = "img/redes/webp/"
os.makedirs(output_folder, exist_ok=True)

extensiones = (".jpg", ".jpeg", ".png")

procesadas = 0
fallidas = []

for filename in os.listdir(input_folder):
    if filename.lower().endswith(extensiones):
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                webp_name = os.path.splitext(filename)[0] + ".webp"
                webp_path = os.path.join(output_folder, webp_name)
                img.save(webp_path, "WEBP", quality=85)
                print(f"✅ Convertido: {filename} → {webp_name}")
                procesadas += 1
        except UnidentifiedImageError:
            print(f"❌ ERROR: No se pudo abrir como imagen → {filename}")
            fallidas.append(filename)
        except Exception as e:
            print(f"❌ ERROR inesperado con {filename}: {e}")
            fallidas.append(filename)

# Resumen final
print("\n--- RESUMEN ---")
print(f"Imágenes convertidas correctamente: {procesadas}")
print(f"Imágenes con error: {len(fallidas)}")

if fallidas:
    print("Lista de imágenes con error:")
    for f in fallidas:
        print(f" - {f}")