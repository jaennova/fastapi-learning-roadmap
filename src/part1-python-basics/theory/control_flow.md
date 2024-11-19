### **Operaciones de Control de Flujo en Python**

#### **Descripción**
El control de flujo permite que un programa tome decisiones y repita bloques de código según condiciones específicas. En Python, el control de flujo incluye estructuras condicionales, bucles y palabras clave para modificar el comportamiento de las iteraciones.

En esta sección, aprenderás cómo utilizar las estructuras `if`, `else`, y `elif`, los bucles `for` y `while`, y palabras clave como `break`, `continue` y `pass` para manejar el flujo de ejecución en tus programas.

---

#### **Objetivos**
Al finalizar esta sección, serás capaz de:
1. Utilizar condicionales para tomar decisiones en el programa.
2. Trabajar con bucles para iterar sobre secuencias y realizar tareas repetitivas.
3. Controlar el comportamiento de los bucles con palabras clave como `break` y `continue`.

---

#### **Contenido**

##### **1. Condicionales en Python**
- **Estructura básica de un `if`:**
  ```python
  edad = 18
  if edad >= 18:
      print("Eres mayor de edad.")
  ```

- **Uso de `else`:**
  ```python
  hora = 15
  if hora < 12:
      print("Buenos días.")
  else:
      print("Buenas tardes.")
  ```

- **Uso de `elif` para múltiples condiciones:**
  ```python
  temperatura = 30
  if temperatura < 10:
      print("Hace frío.")
  elif 10 <= temperatura < 25:
      print("El clima es agradable.")
  else:
      print("Hace calor.")
  ```

- **Condicionales anidados:**
  ```python
  numero = 5
  if numero > 0:
      if numero % 2 == 0:
          print("Es un número positivo y par.")
      else:
          print("Es un número positivo e impar.")
  ```

---

##### **2. Operadores en Condicionales**
- **Operadores de comparación:**
  ```python
  a, b = 5, 10
  print(a == b)  # False
  print(a != b)  # True
  print(a < b)   # True
  ```

- **Operadores lógicos (`and`, `or`, `not`):**
  ```python
  es_sol = True
  es_finde = False

  if es_sol and es_finde:
      print("Es un día perfecto para la playa.")
  elif es_sol or es_finde:
      print("Aún puedes disfrutar el día.")
  ```

- **Operador ternario:**
  ```python
  es_mayor = True
  mensaje = "Mayor de edad" if es_mayor else "Menor de edad"
  print(mensaje)
  ```

---

##### **3. Bucles en Python**
- **El bucle `for`:**
  ```python
  frutas = ["manzana", "plátano", "cereza"]
  for fruta in frutas:
      print(fruta)
  ```

  - Iterar con índices usando `enumerate`:
    ```python
    for index, fruta in enumerate(frutas):
        print(f"{index}: {fruta}")
    ```

- **El bucle `while`:**
  ```python
  contador = 0
  while contador < 5:
      print(contador)
      contador += 1
  ```

---

##### **4. Controlar Bucles**
- **Romper el bucle con `break`:**
  ```python
  for numero in range(10):
      if numero == 5:
          break
      print(numero)
  ```

- **Omitir una iteración con `continue`:**
  ```python
  for numero in range(10):
      if numero % 2 == 0:
          continue
      print(numero)  # Imprime solo números impares
  ```

- **Uso de `pass` como marcador de posición:**
  ```python
  for numero in range(5):
      if numero == 3:
          pass  # Por ahora no hago nada
      else:
          print(numero)
  ```

---

##### **5. Iteradores y Generadores**
- **Iterar sobre un rango:**
  ```python
  for i in range(1, 6):
      print(i)  # 1, 2, 3, 4, 5
  ```

- **Uso de generadores con `yield`:**
  ```python
  def generador_pares(n):
      for i in range(n):
          if i % 2 == 0:
              yield i
  
  for par in generador_pares(10):
      print(par)
  ```

---

##### **6. Bucles y Estructuras Compuestas**
- **Bucles con listas y diccionarios:**
  ```python
  diccionario = {"nombre": "Ana", "edad": 25}
  for clave, valor in diccionario.items():
      print(f"{clave}: {valor}")
  ```

- **Bucles anidados:**
  ```python
  for i in range(3):
      for j in range(2):
          print(f"i={i}, j={j}")
  ```

---

#### **Prácticas Recomendadas**
1. **Ejercicio 1:** Escribe un programa que reciba un número e imprima si es primo o no.
2. **Ejercicio 2:** Crea un ciclo que genere los primeros 10 números de la serie de Fibonacci.
3. **Mini Proyecto:** Escribe un programa que reciba calificaciones de varios estudiantes y calcule el promedio, imprimiendo quién aprobó y quién no (nota mínima para aprobar: 70).

---

#### **Recursos Adicionales**
- [Documentación Oficial sobre Condicionales y Bucles](https://docs.python.org/3/tutorial/controlflow.html)
- Tutorial sobre generadores en Python: [realpython.com](https://realpython.com/introduction-to-python-generators/)
