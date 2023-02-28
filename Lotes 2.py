import os
import shutil
import random

# Función para cambiar letras y dígitos
def modificar_archivo(ruta_archivo):
    with open(ruta_archivo, "r") as rt_arch:
        contenido = rt_arch.read()
        # Reemplazar letras y dígitos
        nuevos_caracteres = []
        for c in contenido:
            if c.isalpha():
                # Generar dígito aleatorio
                nuevos_c = random.choice("0123456789")
                nuevos_caracteres.append(nuevos_c)
            elif c.isdigit():
                # Generar letra aleatoria
                nuevos_c = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                nuevos_caracteres.append(nuevos_c)
            else:
                nuevos_caracteres.append(c)
        nuevo_contenido = "".join(nuevos_caracteres)  
    with open(ruta_archivo, "w") as rt_arch:
        rt_arch.write(nuevo_contenido)

# Función para procesar archivo
def proceso(ruta_archivo):
    # Generar una nueva ruta para la copia del archivo
    nombre_direccion, nombre_archivo = os.path.split(ruta_archivo)
    nuevo_nombre_direccion = f"{nombre_direccion}_copy"
    nueva_ruta_archivo = os.path.join(nuevo_nombre_direccion, nombre_archivo)

    # Crear la carpeta para la copia si no existe
    if not os.path.exists(nuevo_nombre_direccion):
        os.makedirs(nuevo_nombre_direccion)

    # Copiar archivo a nueva ruta
    shutil.copy(ruta_archivo, nueva_ruta_archivo)

    # Modificar archivo copiado
    modificar_archivo(nueva_ruta_archivo)

    print(f"Archivo procesado: {nueva_ruta_archivo}")

ruta_carpeta = "E:/SSPSO/Sistemas"
for raiz, direcciones, archivos in os.walk(ruta_carpeta):
    for archivo in archivos:
        ruta_archivo = os.path.join(raiz, archivo)
        proceso(ruta_archivo)

