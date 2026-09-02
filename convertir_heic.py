from PIL import Image
from pillow_heif import register_heif_opener
import os

# Registrar el soporte para HEIC
register_heif_opener()

# Carpeta de fotos
carpeta = r"C:\Users\lucas\OneDrive\Documentos\CUMPLE\fotos"

# Archivos HEIC a convertir
archivos_heic = ['foto2.heic', 'foto4.heic', 'foto6.HEIC']

print("Convirtiendo fotos HEIC a JPG...")

for archivo in archivos_heic:
    ruta_heic = os.path.join(carpeta, archivo)

    if os.path.exists(ruta_heic):
        # Nombre del archivo JPG (mismo nombre pero con extensión .jpg)
        nombre_base = os.path.splitext(archivo)[0]
        ruta_jpg = os.path.join(carpeta, f"{nombre_base}.jpg")

        try:
            # Abrir y convertir
            imagen = Image.open(ruta_heic)

            # Convertir a RGB si es necesario
            if imagen.mode != 'RGB':
                imagen = imagen.convert('RGB')

            # Guardar como JPG
            imagen.save(ruta_jpg, 'JPEG', quality=95)
            print(f"OK - Convertido: {archivo} -> {nombre_base}.jpg")

        except Exception as e:
            print(f"ERROR al convertir {archivo}: {e}")
    else:
        print(f"ERROR - No se encontro: {archivo}")

print("\nConversion completada!")
