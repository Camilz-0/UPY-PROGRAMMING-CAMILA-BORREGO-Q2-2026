# UPY-PROGRAMMING-CAMILA-BORREGO-Q2-2026

Repositorio para las tareas de la asignatura de Programación.

---

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
```

---

# CW08 - Numerical Integration

Se agregó la carpeta `Classwork-08-Numerical-Integration` que contiene las herramientas para calcular aproximaciones de integrales definidas mediante métodos numéricos de rectángulos.

Archivos incluidos:

* **`PPP.txt`:** Pseudocódigo completo en inglés estructurado bajo las reglas de clase.
* **`Flowchart.png`:** Diagrama de flujo que explica el bucle principal y las desviaciones de los tres métodos.
* **`numerical_integration.py`:** Código funcional en Python organizado con comentarios de `# INPUT`, `# PROCESS` y `# OUTPUT`.

Ejemplo de uso:

```text
Enter the left interval limit (a): 0
Enter the right interval limit (b): pi
Enter the function in terms of x (e.g., x**2): x**2
Select calculation method (LRM, RRM, MRM): MRM
The integration of x**2 using MRM is: 10.3354
```

---

# CW09 - Spanish Verb Conjugator

Se agregó la carpeta `Classwork-09-Spanish-Verb-Conjugator` que contiene la lógica para la conjugación automática de verbos.

### Archivos incluidos:
* **`PPP.txt`:** Pseudocódigo que detalla la lógica de separación de raíces y terminaciones verbales.
* **`Flowchart.png`:** Diagrama de flujo detallando el proceso de conjugación y decisiones.
* **`spanish_verb_conjugator.py`:** Programa que utiliza diccionarios para organizar los datos y generar las conjugaciones.

Ejemplo de uso:

```text
Write a spanish verb (ar/er/ir): hablar
yo hablo
tu hablas
el habla
nosotros hablamos
vosotros hablais
ellos hablan
```

---

# CW10 - School Management System

Se agregó la carpeta `Classwork-10-School-Management-System` que contiene el simulador de un sistema de gestión escolar con tres niveles de acceso (estudiante, profesor y coordinador).

### Archivos incluidos:
* **`PPP.txt`:** Pseudocódigo que detalla la lógica de validación de usuarios y la gestión de permisos según el rol.
* **`Flowchart.png`:** Diagrama que ilustra las condiciones lógicas necesarias para filtrar la información según el usuario autenticado.
* **`school_management.py`:** Código con el programa principal que utiliza diccionarios para organizar los datos de usuarios, materias y calificaciones, permitiendo la consulta y edición de registros.

### Ejemplo de uso:
```text
User: cborrego
Password: 1234
Bienvenid@!, Camila Borrego (alumno)
=======================================
  School Report
=======================================
Discrete Mathematics                        : 8.5
Programming                                 : 8.0
English II                                  : 9.0
Differential Calculus                       : 9.8
Probability and Statistics                  : 8.3
Computer and Server Architecture            : 9.0
Socio-Emotional Skills and Conflict Management : 9.5
Approved: {'English II', 'Computer and Server Architecture', 'Discrete Mathematics', 'Programming', 'Differential Calculus', 'Socio-Emotional Skills and Conflict Management', 'Probability and Statistics'}
Pending : set()
```

---

## Declaración de Autoría

Yo, **`Camila Berenice Borrego Ayala`**, declaro que este trabajo fue desarrollado de forma personal y original por su autora. Afirmo que **NO** he utilizado herramientas de Inteligencia Artificial para la generación de la lógica, documentación o entregables incluidos en este proyecto.