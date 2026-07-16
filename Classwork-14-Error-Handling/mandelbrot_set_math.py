# INPUT

config = {}

file = open("config.txt", "r")
for line in file:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value)
file.close()

width = int(config["ancho"])
height = int(config["alto"])
max_iter = int(config["max_iter"])

output = open("mandelbrot.csv", "w")
output.write("fila,columna,iteraciones\n")

# PROCESS & OUTPUT

for row in range(height):
    for column in range(width):
        real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
        imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
        c = complex(real, imag)
        
        z = 0 + 0j
        iterations = 0
        
        while (abs(z) <= 2) and (iterations < max_iter):
            z = z * z + c
            iterations += 1
        
        output.write(f"{row},{column},{iterations}\n")

output.close()