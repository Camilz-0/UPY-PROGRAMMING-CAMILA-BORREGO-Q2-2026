# Obtener el rol del usuario como texto
rol = input("Ingrese el rol UTFSM: ")

if "-" not in rol or rol.count("-") != 1:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
    exit()

partes = rol.split("-")
numero_base = partes[0]
digito_v = partes[1]

if not numero_base.isdigit():
    print("Los digitos del rol deben ser numéricos")
    exit()

if not digito_v.isdigit():
    print("El digito verificador debe ser numérico")
    exit()

rol_invertido = numero_base[::-1]

suma = 0
multiplicador = 2

for digito in rol_invertido:
    suma += int(digito) * multiplicador
    
    multiplicador += 1
    if multiplicador > 7:
        multiplicador = 2

modulo = suma % 11

digito_verificador = 11 - modulo
if digito_verificador == 11:
    digito_verificador = 0

if int(digito_v) == digito_verificador:
    print(f"{rol}")
else:
    print(f"Error: El dígito verificador no conicide, se esperaba {digito_verificador}")