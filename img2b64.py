import base64
import os

def imagen_a_base64(nombre_archivo):
    ruta = os.path.join("img", nombre_archivo)
    try:
        with open(ruta, "rb") as imagen:
            imagen_codificada = base64.b64encode(imagen.read())
            return imagen_codificada.decode("utf-8")
    except FileNotFoundError:
        return f"❌ No se encontró la imagen en la ruta: {ruta}"

# Solicita solo el nombre del archivo
nombre = input("🖼️ Ingresá el nombre del archivo (ej: foto.jpg): ")
base64_string = imagen_a_base64(nombre)

print("\n📄 Resultado en Base64:\n")
print(base64_string)

# Pausa al final
input("\nPresioná cualquier tecla para salir...")
