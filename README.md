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

---

# CW08 - Numerical Integration

Se agregó la carpeta `Classwork-08-Numerical-Integration` que contiene las herramientas para calcular aproximaciones de integrales definidas mediante métodos numéricos de rectángulos.

### Archivos incluidos:
* **`PPP.txt`:** Pseudocódigo completo en inglés estructurado bajo las reglas de clase.
* **`Flowchart.png`:** Diagrama de flujo que explica el bucle principal y las desviaciones de los tres métodos.
* **`numerical_integration.py`:** Código funcional en Python organizado con comentarios de `# INPUT`, `# PROCESS` y `# OUTPUT`.

### Ejemplo de uso:
```text
Enter the left interval limit (a): 0
Enter the right interval limit (b): pi
Enter the function in terms of x (e.g., x**2): x**2
Select calculation method (LRM, RRM, MRM): MRM
The integration of x**2 using MRM is: 10.3354

---

# AI use declaration

`Yo, Camila Berenice Borrego Ayala, declaro que NO he utilizado herramientas de Inteligencia Artificial para la elaboración de este trabajo académico.`