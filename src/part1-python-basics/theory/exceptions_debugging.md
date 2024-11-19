### **Manejo y Depuración de Excepciones**

#### **Descripción**
El manejo de excepciones es una habilidad clave para garantizar que tus aplicaciones puedan gestionar errores de manera adecuada sin detenerse abruptamente. Python ofrece un sistema robusto para capturar y manejar excepciones que permite identificar, resolver y registrar problemas en tiempo de ejecución.

En esta sección, aprenderás cómo manejar excepciones comunes, definir tus propias excepciones y depurar código para mejorar la calidad de tus aplicaciones.

---

#### **Objetivos**
Al finalizar esta sección, serás capaz de:
1. Identificar y manejar excepciones comunes en Python.
2. Utilizar bloques `try`, `except`, `else` y `finally`.
3. Crear excepciones personalizadas.
4. Implementar herramientas y prácticas para depurar código de manera eficiente.

---

#### **Contenido**

##### **1. Introducción a las Excepciones**
- **¿Qué es una excepción?**
  Una excepción es un evento inesperado que interrumpe la ejecución normal de un programa. Python genera excepciones automáticamente cuando ocurre un error.

- **Ejemplo de excepción común:**
  ```python
  print(10 / 0)  # ZeroDivisionError
  ```

---

##### **2. Manejo Básico de Excepciones**
- **Uso de `try` y `except`:**
  ```python
  try:
      resultado = 10 / 0
  except ZeroDivisionError:
      print("Error: División entre cero.")
  ```

- **Bloques `else` y `finally`:**
  ```python
  try:
      resultado = 10 / 2
  except ZeroDivisionError:
      print("Error: División entre cero.")
  else:
      print("Operación exitosa:", resultado)
  finally:
      print("Finalizando operación.")
  ```

---

##### **3. Tipos Comunes de Excepciones**
- **Algunos ejemplos:**
  - `ValueError`: Cuando un valor tiene el tipo incorrecto.
  - `IndexError`: Cuando se intenta acceder a un índice fuera de rango en una lista.
  - `KeyError`: Cuando se intenta acceder a una clave inexistente en un diccionario.
  - `FileNotFoundError`: Cuando un archivo no se encuentra.

  ```python
  try:
      archivo = open("inexistente.txt", "r")
  except FileNotFoundError:
      print("El archivo no existe.")
  ```

---

##### **4. Definición de Excepciones Personalizadas**
- **Crear tus propias excepciones:**
  ```python
  class MiExcepcion(Exception):
      def __init__(self, mensaje):
          self.mensaje = mensaje

  try:
      raise MiExcepcion("Ocurrió un error personalizado.")
  except MiExcepcion as e:
      print(e.mensaje)
  ```

---

##### **5. Registro de Errores**
- **Uso del módulo `logging`:**
  En lugar de imprimir errores, utiliza `logging` para registrar información.
  ```python
  import logging

  logging.basicConfig(level=logging.ERROR, filename="errores.log")
  
  try:
      resultado = 10 / 0
  except ZeroDivisionError as e:
      logging.error(f"Error: {e}")
  ```

---

##### **6. Depuración de Código**
- **Uso de `pdb` (Python Debugger):**
  Inserta un punto de interrupción para analizar el código paso a paso.
  ```python
  import pdb

  def dividir(a, b):
      pdb.set_trace()  # Punto de interrupción
      return a / b

  dividir(10, 0)
  ```

- **Depuración en entornos IDE:**
  Utiliza herramientas como los depuradores integrados de VSCode, PyCharm o similares para inspeccionar variables y flujos.

---

##### **7. Aplicaciones Prácticas**
- **Middleware para manejo de errores en FastAPI:**
  FastAPI permite capturar errores globalmente con middlewares.
  ```python
  from fastapi import FastAPI, HTTPException

  app = FastAPI()

  @app.exception_handler(HTTPException)
  async def http_excepcion_handler(request, exc):
      return {"detalle": exc.detail}

  @app.get("/")
  async def raiz():
      raise HTTPException(status_code=404, detail="No encontrado.")
  ```

---

#### **Recursos Adicionales**
- [Documentación Oficial de Manejo de Excepciones en Python](https://docs.python.org/3/tutorial/errors.html)
- Guía sobre `logging` en Python: [Enlace aquí](https://docs.python.org/3/library/logging.html)
- Tutorial interactivo sobre depuración en Python: [realpython.com/debugging-python](https://realpython.com/python-debugging-pdb/)

---

#### **Prácticas Recomendadas**
1. **Ejercicio 1:** Escribe un programa que lea un archivo y maneje la excepción si el archivo no existe.
2. **Ejercicio 2:** Crea una calculadora que maneje excepciones como `ZeroDivisionError` o entradas no válidas.
3. **Mini Proyecto:** Implementa un sistema de registro de errores en una API FastAPI para monitorear excepciones y generar logs.
