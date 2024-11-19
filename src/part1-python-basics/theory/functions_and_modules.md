### **Funciones y Módulos en Python**

#### **Descripción**
Las funciones y módulos son fundamentales en Python para estructurar el código de manera eficiente y reutilizable. Una función encapsula un bloque de código que realiza una tarea específica, mientras que los módulos permiten organizar el código en archivos separados, facilitando su mantenimiento y reutilización.

En esta sección, aprenderás cómo definir funciones, trabajar con parámetros y valores de retorno, y utilizar módulos estándar o personalizados para mejorar la modularidad de tus proyectos.

---

#### **Objetivos**
Al finalizar esta sección, serás capaz de:
1. Definir y usar funciones en Python.
2. Trabajar con diferentes tipos de parámetros y valores de retorno.
3. Crear y usar módulos personalizados.
4. Importar y utilizar módulos estándar de Python.

---

#### **Contenido**

##### **1. Introducción a las Funciones**
- **Definición de una función:**
  ```python
  def saludar():
      print("¡Hola, mundo!")
  
  saludar()  # Llamada a la función
  ```

- **Funciones con parámetros:**
  ```python
  def sumar(a, b):
      return a + b
  
  resultado = sumar(5, 3)
  print("La suma es:", resultado)
  ```

---

##### **2. Tipos de Parámetros**
- **Parámetros por posición:**
  ```python
  def multiplicar(a, b):
      return a * b
  
  print(multiplicar(2, 3))  # 6
  ```

- **Parámetros con valores por defecto:**
  ```python
  def saludar(nombre="mundo"):
      print(f"¡Hola, {nombre}!")
  
  saludar()  # Hola, mundo
  saludar("Ana")  # Hola, Ana
  ```

- **Parámetros arbitrarios:**
  - *Tuplas (`*args`):*
    ```python
    def sumar(*numeros):
        return sum(numeros)
    
    print(sumar(1, 2, 3, 4))  # 10
    ```
  - *Diccionarios (`**kwargs`):*
    ```python
    def mostrar_info(**datos):
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    
    mostrar_info(nombre="Ana", edad=25, ciudad="México")
    ```

---

##### **3. Retorno de Valores**
- **Retornar un solo valor:**
  ```python
  def cuadrado(x):
      return x ** 2
  
  print(cuadrado(4))  # 16
  ```

- **Retornar múltiples valores:**
  ```python
  def operaciones(a, b):
      return a + b, a - b, a * b, a / b
  
  suma, resta, producto, division = operaciones(10, 2)
  print("Suma:", suma, "Resta:", resta)
  ```

---

##### **4. Funciones Lambda**
- **Funciones anónimas de una línea:**
  ```python
  cuadrado = lambda x: x ** 2
  print(cuadrado(5))  # 25
  ```

- **Uso con funciones como `map` y `filter`:**
  ```python
  numeros = [1, 2, 3, 4]
  cuadrados = list(map(lambda x: x ** 2, numeros))
  print(cuadrados)  # [1, 4, 9, 16]
  ```

---

##### **5. Introducción a los Módulos**
- **Importar un módulo estándar:**
  ```python
  import math
  
  print(math.sqrt(16))  # 4.0
  ```

- **Importar una función específica de un módulo:**
  ```python
  from math import pi, sqrt
  
  print(pi)  # 3.141592653589793
  print(sqrt(9))  # 3.0
  ```

- **Renombrar un módulo o función:**
  ```python
  import math as m
  
  print(m.sin(0))  # 0.0
  ```

---

##### **6. Crear Módulos Propios**
- **Ejemplo de un módulo personalizado:**
  - Archivo `calculadora.py`:
    ```python
    def sumar(a, b):
        return a + b
    
    def restar(a, b):
        return a - b
    ```

  - Archivo principal:
    ```python
    import calculadora as calc

    print(calc.sumar(5, 3))  # 8
    print(calc.restar(5, 3))  # 2
    ```

- **Organización en paquetes:**
  - Estructura de directorios:
    ```
    mi_paquete/
    ├── __init__.py
    ├── modulo1.py
    └── modulo2.py
    ```
  - Uso del paquete:
    ```python
    from mi_paquete.modulo1 import funcion1
    ```

---

##### **7. Módulos Estándar de Python**
- **Algunos ejemplos útiles:**
  - `os`: Manejo del sistema operativo.
  - `sys`: Interacción con el intérprete.
  - `random`: Generación de números aleatorios.
  - `datetime`: Manejo de fechas y horas.

  ```python
  import random
  print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
  ```

---

#### **Prácticas Recomendadas**
1. **Ejercicio 1:** Crea una función que reciba una lista de números y retorne el promedio.
2. **Ejercicio 2:** Define un módulo llamado `utilidades` que contenga funciones para convertir temperaturas (Celsius a Fahrenheit y viceversa).
3. **Mini Proyecto:** Crea un módulo que gestione un sistema básico de tareas, permitiendo agregar, listar y eliminar tareas.

---

#### **Recursos Adicionales**
- [Documentación Oficial sobre Funciones en Python](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Documentación Oficial sobre Módulos](https://docs.python.org/3/tutorial/modules.html)
- Tutorial sobre funciones lambda: [realpython.com/python-lambda](https://realpython.com/python-lambda/)
