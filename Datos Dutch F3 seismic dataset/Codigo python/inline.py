import segyio
import numpy as np
import matplotlib.pyplot as plt

archivo = "C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"


with segyio.open(archivo, "r") as f:

    # Obtenemos las inlines disponibles
    inlines = list(f.ilines)

    # Tomamos una inline del centro
    inline_id = inlines[len(inlines)//2]

    # Leemos la inline completa
    inline = f.iline[inline_id]

plt.imshow(inline.T, cmap="seismic", aspect="auto")
plt.title(f"INLINE {inline_id}")
plt.xlabel("Crossline")
plt.ylabel("Tiempo / Profundidad")
plt.colorbar(label="Amplitud")
plt.gca().invert_yaxis()
plt.show()
