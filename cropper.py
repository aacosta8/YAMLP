import pandas as pd
import numpy as np
import os.path
import os

save_path = os.getcwd()
files_path = r"D:\SatelliteData\CSV"

red_shape = 6002
blue_shape = 3001

crop_size = 15

#Definir coordenadas. Son la esquina superior izquierda del recorte
coordinates = {
    'red' : {
        1: (2980, 2987),
        2: (3000, 2976),
        3: (2981, 2997)
    },
    'blue' : {
        1 : (1491, 1495),
        2 : (1501, 1489),
        3 : (1491, 1500)
    }
}

#Funcion para convertir un arreglo a otro tamano, de https://stackoverflow.com/questions/8090229/resize-with-averaging-or-rebin-a-numpy-2d-array
def rebin(a, shape):
    sh = shape[0],a.shape[0]//shape[0],shape[1],a.shape[1]//shape[1]
    return a.reshape(sh).mean(-1).mean(1)

#Leer archivo maestro
files = pd.read_csv(r"C:\Users\Lombardo\Downloads\allDatacolumns.csv")

crops = []
os.chdir(files_path)
indexes = []
i = 0
for index, row in files.iterrows():
    #Solo leemos si existen los 3 canales.
    if os.path.exists(row[2]) and os.path.exists(row[3]) and os.path.exists(row[4]):
        channel1 = np.reshape(np.fromfile(row[2],dtype="int16"),[-1,blue_shape])
        channel2 = np.reshape(np.fromfile(row[3],dtype="int16"),[-1,red_shape])
        channel3 = np.reshape(np.fromfile(row[4],dtype="int16"),[-1,blue_shape])
        #Recortamos
        blue_coordinate = coordinates['blue'][row[0]]
        red_coordinate = coordinates['red'][row[0]]
        channel1 = channel1[blue_coordinate[0]:blue_coordinate[0]+crop_size,blue_coordinate[1]:blue_coordinate[1]+crop_size]
        channel2 = channel2[red_coordinate[0]:red_coordinate[0]+2*crop_size,red_coordinate[1]:red_coordinate[1]+2*crop_size]
        channel3 = channel3[blue_coordinate[0]:blue_coordinate[0]+crop_size,blue_coordinate[1]:blue_coordinate[1]+crop_size]
        #Resizing
        channel2 = rebin(channel2, (crop_size, crop_size))
        #Guardamos
        crop = np.stack((channel1, channel2, channel3), axis=2)
        crops.append(crop)
        indexes.append(index)
        
os.chdir(save_path)

np.save("index_list", np.array(indexes))
np.save("crops", np.array(crops))