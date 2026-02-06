import numpy as np
import segyio

archivo = "C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"

with segyio.open(archivo, "r", ignore_geometry=True) as f:

    n_traces = f.tracecount
    n_samples = f.samples.size

    # Definimos una grilla artificial (20x20)
    n_inline = 20
    n_crossline = 20

    depth_index = 200

    horizonte = np.zeros((n_inline, n_crossline))

    for i in range(n_inline):
        for j in range(n_crossline):
            trace_index = i * n_crossline + j
            horizonte[i, j] = f.trace[trace_index][depth_index]

print("Horizonte creado con forma:", horizonte.shape)

