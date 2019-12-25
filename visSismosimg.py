from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

import cartopy.feature
from cartopy.mpl.patch import geos_to_path
import cartopy.crs as ccrs

import itertools

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import matplotlib.cm as cm
import cartopy.feature
from cartopy.mpl.patch import geos_to_path
import cartopy.crs as ccrs
import pandas as pd


# importo las tablas de excel donde estan los sismos del servicio geológico

sismos = pd.read_excel('repo1893.xlsx')
# Selecciono los datos a usar de latitud, longitud, profundidad, magnitud
# tanto los picados por mi (ms) como los picados por el servicio (ss)

lats = np.asarray(sismos['LATITUD (°)'])
lons = np.asarray(sismos['LONGITUD (°)'])
deps = np.asarray(sismos['PROF. (Km)'])
mags = np.asarray(sismos['MAGNITUD'])

fechas = np.asarray(sismos['FECHA - HORA UTC'])
c_lons = lons - lons.min()
c_lats = lats - lats.min()

prof = 0

maxMg = mags.max()
minMg = mags.min()

def numero(i):
    num = ((mags[i]-minMg)/(maxMg-minMg))*250
    return num

for i in range(0,len(lats)):
    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(111, projection='3d')
    # proj_ax = plt.figure().add_axes([0, 0, 1, 1], projection=ccrs.Mercator())


    color_pri = 'black'
    color_sec = 'red'
    
    
    
    if (i-5)==-5:
        pass
    elif (i-5)==-4:
        ax.scatter(c_lons[i-1], c_lats[i-1], -deps[i-1],s=numero(i-1), c=color_sec, alpha=0.70)
    elif (i-5)==-3:
        ax.scatter(c_lons[i-1], c_lats[i-1], -deps[i-1],s=numero(i-1), c=color_sec, alpha=0.70)
        ax.scatter(c_lons[i-2], c_lats[i-1], -deps[i-2],s=numero(i-2), c=color_sec, alpha=0.5)
    elif (i-5)==-2:
        ax.scatter(c_lons[i-1], c_lats[i-1], -deps[i-1],s=numero(i-1), c=color_sec, alpha=0.70)
        ax.scatter(c_lons[i-2], c_lats[i-1], -deps[i-2],s=numero(i-2), c=color_sec, alpha=0.5)
        ax.scatter(c_lons[i-3], c_lats[i-3], -deps[i-3],s=numero(i-3), c=color_sec, alpha=0.5)       
    else:
        ax.scatter(c_lons[i-1], c_lats[i-1], -deps[i-1],s=numero(i-1), c=color_sec, alpha=0.70)
        ax.scatter(c_lons[i-2], c_lats[i-1], -deps[i-2],s=numero(i-2), c=color_sec, alpha=0.5)
        ax.scatter(c_lons[i-3], c_lats[i-3], -deps[i-3],s=numero(i-3), c=color_sec, alpha=0.25)
        ax.scatter(c_lons[i-4], c_lats[i-4], -deps[i-4],s=numero(i-4), c=color_sec, alpha=0.15)
    
    ax.scatter(c_lons[i], c_lats[i], -deps[i], s=numero(i), c=color_sec, alpha=1)
    ax.scatter(c_lons[1], c_lats[1], 60, s=numero(1), c=color_sec, alpha=1, label="sismos") 

    
    xx, yy = np.meshgrid(range(2), range(2)) # se crea la red que genera el plano
    xx, yy = xx/2, yy/2
    z = np.zeros((2,2))
    a = 0
    z= np.array([[ a,  a],[a, a]]) # plano en cero, se crea variable a para controlar su ubicación
    ax.plot_surface(xx, yy, z,alpha=0.2)

    ind = np.arange(0.0,0.6,0.1)
    latgraph = np.linspace(lats.min(),lats.max(),6)
    longraph = np.linspace(lons.min(),lons.max(),6)
    plt.xticks(ind, (str(round(latgraph[0],4)), str(round(latgraph[1],4)),str(round(latgraph[2],4)), str(round(latgraph[3],4)), str(round(latgraph[4],4)), str(round(latgraph[5],4) )))
    plt.yticks(ind, (str(round(longraph[0],4)), str(round(longraph[1],4)),str(round(longraph[2],4)), str(round(longraph[3],4)), str(round(longraph[4],4)), str(round(longraph[5],4) )))
    ax.set_zlim(-42,2)
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.set_zlabel('Profundidad')
    ax.set_title("Sismo y Réplicas. Mesetas - Meta (24 y 25 de Diciembre)\n MAGNITUD: %2.1f\n HORA (UTC): %s"%(float(mags[i]), str(fechas[i])))

    plt.legend()
    plt.savefig("imgs/anima"+str(i)+".png")
