# CW07 - Dígito verificador de rol UTFSM

Se agregó la carpeta `Classwork-07-Digit-Verification` con el programa `cw07.py`, que calcula el dígito verificador de un rol UTFSM.

El programa realiza los siguientes pasos:

1. **Obtener el rol** sin guion ni dígito verificador.
2. **Invertir el número**.
3. **Multiplicar los dígitos** por la secuencia 2, 3, 4, 5, 6, 7 (comenzando de nuevo si se acaban los números) y sumar los resultados.
4. **Sacarle el módulo 11** al resultado obtenido.
5. **Restarlo de 11** para obtener el dígito verificador final.

Ejemplo de uso:

```text
Ingrese el rol UTFSM (sin guion ni digito verificador): 201012341
El digito verificador sera el obtenido en la resta: 201012341-3