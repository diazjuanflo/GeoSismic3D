import numpy as np
from stl import mesh
import segyio

archivo = "C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"

with segyio.open(archivo, "r", ignore_geometry=True) as f:

    n_inline = 20
    n_crossline = 20
    depth_index = 200

    horizonte = np.zeros((n_inline, n_crossline))

    for i in range(n_inline):
        for j in range(n_crossline):
            trace_index = i * n_crossline + j
            horizonte[i, j] = f.trace[trace_index][depth_index]

# Escala para impresión 
horizonte = horizonte - np.min(horizonte)
horizonte = horizonte / np.max(horizonte)
horizonte = horizonte * 10  # altura en mm

# Crea los vértices y las caras
vertices = []
faces = []

for i in range(n_inline - 1):
    for j in range(n_crossline - 1):

        v0 = [i, j, horizonte[i, j]]
        v1 = [i + 1, j, horizonte[i + 1, j]]
        v2 = [i + 1, j + 1, horizonte[i + 1, j + 1]]
        v3 = [i, j + 1, horizonte[i, j + 1]]

        idx = len(vertices)
        vertices.extend([v0, v1, v2, v3])

        faces.append([idx, idx + 1, idx + 2])
        faces.append([idx, idx + 2, idx + 3])

vertices = np.array(vertices)
faces = np.array(faces)

# Crea la malla STL
malla = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

for i, f in enumerate(faces):
    for j in range(3):
        malla.vectors[i][j] = vertices[f[j]]

# Guarda el archivo STL
malla.save("horizonte_sismico.stl")

print("STL generado: horizonte_sismico.stl")
