import segyio
import numpy as np
import matplotlib.pyplot as plt

archivo = r"C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"

with segyio.open(archivo, "r") as f:
    crosslines = f.xlines[:]        # ya no es None
    crossline_id = crosslines[len(crosslines)//2]
    crossline = f.xline[crossline_id]

plt.imshow(crossline.T, cmap="seismic", aspect="auto")
plt.title(f"CROSSLINE {crossline_id}")
plt.xlabel("Inline")
plt.ylabel("Tiempo / Profundidad")
plt.colorbar(label="Amplitud")
plt.gca().invert_yaxis()
plt.show()

