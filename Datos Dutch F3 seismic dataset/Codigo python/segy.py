import segyio
import numpy as np
import matplotlib.pyplot as plt

archivo = "C:/Users/diaz7/OneDrive/Documentos/Proyecto GeoSismic3D/Datos Dutch F3 seismic dataset/Datos/Dutch F3 seismic data/Dutch_Government_F3_entire_8bit_seismic.segy"

with segyio.open(archivo, "r", ignore_geometry=True) as f:    
    print("Número de trazas:", f.tracecount)
    print("Número de muestras por traza:", f.samples.size)

    # Leemos una traza
    traza = f.trace[0]

plt.plot(traza)
plt.title("Traza sísmica individual")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()
