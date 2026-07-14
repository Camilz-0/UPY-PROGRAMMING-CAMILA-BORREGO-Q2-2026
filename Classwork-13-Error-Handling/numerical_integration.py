import math

try:
    a_input = input("Límite izquierdo (a): ")
    b_input = input("Límite derecho (b): ")
    f_x = input("Función (ej. x**2): ")
    method = input("Método (LRM, RRM, MPM, TM): ").upper()

    try:
        a = float(eval(a_input.replace("pi", str(math.pi))))
    except:
        raise ValueError("El límite inferior debe ser numérico")

    try:
        b = float(eval(b_input.replace("pi", str(math.pi))))
    except:
        raise ValueError("El límite superior debe ser numérico")

    if a >= b:
        raise ValueError("El límite inferior debe ser menor que el límite superior")

    if method not in ["LRM", "RRM", "MPM", "TM"]:
        raise ValueError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")

    n = 1000
    h = (b - a) / n
    area = 0.0

    if method == "LRM": offset = 0.0
    elif method == "RRM": offset = h
    elif method == "MPM": offset = h / 2.0
    else: offset = 0.0

    for i in range(n):
        xi = a + (i * h) + offset
        
        try:
            valor_funcion = f_x.replace("x", f"({xi})")
            height = float(eval(valor_funcion))
        except ZeroDivisionError:
            raise ValueError("La función no está definida en algún punto del intervalo")
        except:
            raise ValueError("La función ingresada no es válida")
        
        area += height * h

    print(f"The integration of {f_x} is {area:.3f}")

except ValueError as e:
    print(f"{e}")
except Exception:
    print("Ocurrió un error inesperado al procesar la función")