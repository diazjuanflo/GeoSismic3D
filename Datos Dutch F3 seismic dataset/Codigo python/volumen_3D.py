import segyio
import numpy as np

archivo = "C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"

# Abrimos el archivo con geometría
with segyio.open(archivo, "r") as f:

    # Tomamos un rango pequeño (subvolumen)
    inlines = list(f.ilines)[10:30]      # 20 inlines
    crosslines = list(f.xlines)[10:30]   # 20 crosslines
    n_samples = f.samples.size

    # Creamos el cubo 3D vacío
    volumen = np.zeros((len(inlines), len(crosslines), n_samples))

    # Llenamos el volumen
    for i, il in enumerate(inlines):
        for j, xl in enumerate(crosslines):
            volumen[i, j, :] = f.trace[il, xl]

print("Volumen creado con forma:", volumen.shape)
