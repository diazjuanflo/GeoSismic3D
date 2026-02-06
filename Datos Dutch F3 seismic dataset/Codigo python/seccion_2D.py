import segyio
import numpy as np
import matplotlib.pyplot as plt

archivo = "C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"
# Número de trazas que queremos mostrar (no todas para no saturar)
N_TRAZAS = 300

with segyio.open(archivo, "r", ignore_geometry=True) as f:
    n_muestras = f.samples.size

    # Creamos una matriz vacía
    seccion = np.zeros((N_TRAZAS, n_muestras))

    # Llenamos la matriz con trazas
    for i in range(N_TRAZAS):
        seccion[i, :] = f.trace[i]

# Mostramos la sección
plt.imshow(
    seccion.T,
    cmap="seismic",
    aspect="auto"
)

plt.colorbar(label="Amplitud sísmica")
plt.title("Sección sísmica 2D – Dutch F3")
plt.xlabel("Número de traza")
plt.ylabel("Tiempo / Profundidad")
plt.gca().invert_yaxis()
plt.show()
