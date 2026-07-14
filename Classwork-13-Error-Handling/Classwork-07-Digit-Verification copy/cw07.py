# Obtener el rol del usuario como texto
rol = input("Ingrese el rol UTFSM: ")

# Invertir el numero
rol_invertido = rol[::-1]

# Variables para la suma y el control de la serie
suma = 0
multiplicador = 2

# Multiplicar los digitos y sumarlos
for digito in rol_invertido:
    suma += int(digito) * multiplicador
    
    # Avanzar el multiplicador. Si pasa de 7, vuelve a empezar en 2
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

# Sacar el modulo 11
modulo = suma % 11

# Restarlo de 11
digito_verificador = 11 - modulo

print(f"{rol}-{digito_verificador}")