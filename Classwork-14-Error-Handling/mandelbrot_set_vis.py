from PIL import Image

config = {}
file = open("config.txt", "r")
lines = file.readlines()
for line in lines:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)
file.close()

max_iter = config["max_iter"]
ancho = config["ancho"]
alto = config["alto"]

archivo = open("mandelbrot.csv", "r")
lineas = archivo.readlines()
archivo.close()

datos = lineas[1:]

img = Image.new("L", (ancho, alto))

for linea in datos:
    fila, columna, iteraciones = linea.strip().split(",")
    row = int(fila)
    column = int(columna)
    iterations = int(iteraciones)
    
    if iterations == max_iter:
        brillo = 0  
    else:
        brillo = int((iterations / max_iter) * 255) 
    
    img.putpixel((column, row), brillo)
    
img.save("mandelbrot.png")
print("DONE")