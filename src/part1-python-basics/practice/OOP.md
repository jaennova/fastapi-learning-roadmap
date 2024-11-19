### **Programación Orientada a Objetos (POO)**

#### **Descripción**
La Programación Orientada a Objetos (POO) es un paradigma de programación que organiza el código en torno a *objetos* y *clases*. Este enfoque es esencial para construir aplicaciones robustas, escalables y reutilizables, especialmente en el desarrollo backend con frameworks como FastAPI.

En esta sección, aprenderás los conceptos fundamentales de POO en Python y cómo aplicarlos en el desarrollo de APIs y proyectos más complejos.

---

#### **Objetivos**
Al finalizar esta sección, serás capaz de:
1. Definir y usar clases y objetos en Python.
2. Implementar conceptos avanzados de POO como herencia, polimorfismo y encapsulación.
3. Utilizar POO para estructurar tus aplicaciones con un diseño más limpio y mantenible.

---

#### **Contenido**

##### **1. Clases y Objetos**
- **Conceptos básicos:**
  - Qué son las clases y los objetos.
  - Diferencias entre una clase y una instancia.
- **Creación de clases:**
  ```python
  class Persona:
      def __init__(self, nombre, edad):
          self.nombre = nombre
          self.edad = edad
      
      def saludar(self):
          print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
  
  persona = Persona("Juan", 30)
  persona.saludar()
  ```
  *Salida:* `Hola, mi nombre es Juan y tengo 30 años.`

---

##### **2. Atributos y Métodos**
- **Atributos de instancia y de clase:**
  ```python
  class Persona:
      especie = "Humano"  # Atributo de clase
      
      def __init__(self, nombre):
          self.nombre = nombre  # Atributo de instancia
  ```
- **Métodos de instancia, clase y estáticos:**
  ```python
  class Calculadora:
      @staticmethod
      def sumar(a, b):
          return a + b
      
      @classmethod
      def mensaje(cls):
          return "Soy una calculadora."
  ```

---

##### **3. Herencia**
- **Extender una clase:**
  ```python
  class Animal:
      def hablar(self):
          print("El animal hace un sonido.")

  class Perro(Animal):
      def hablar(self):
          print("El perro ladra.")
  
  perro = Perro()
  perro.hablar()
  ```
  *Salida:* `El perro ladra.`

---

##### **4. Polimorfismo**
- **Uso de polimorfismo con métodos:**
  ```python
  class Gato:
      def sonido(self):
          return "Miau"

  class Perro:
      def sonido(self):
          return "Guau"

  def imprimir_sonido(animal):
      print(animal.sonido())

  imprimir_sonido(Gato())  # Salida: Miau
  imprimir_sonido(Perro())  # Salida: Guau
  ```

---

##### **5. Encapsulación**
- **Uso de atributos y métodos privados:**
  ```python
  class Banco:
      def __init__(self, saldo):
          self.__saldo = saldo  # Atributo privado
      
      def mostrar_saldo(self):
          return self.__saldo
  ```

---

##### **6. Aplicaciones Prácticas**
- **Modelo de Datos para FastAPI:**
  Utiliza clases para definir modelos de datos con atributos claros y métodos útiles. Este enfoque es esencial al trabajar con herramientas como **Pydantic**.
  
  ```python
  from pydantic import BaseModel

  class Usuario(BaseModel):
      nombre: str
      edad: int
      email: str
  ```

---

#### **Recursos Adicionales**
- [Documentación Oficial de Python sobre POO](https://docs.python.org/3/tutorial/classes.html)
- Tutoriales interactivos de POO en [Real Python](https://realpython.com)

---

#### **Prácticas Recomendadas**
1. **Ejercicio 1:** Crea un sistema de gestión de empleados donde cada empleado tenga atributos como nombre, puesto y salario, y que permita calcular el salario anual.
2. **Ejercicio 2:** Diseña una clase para representar una biblioteca que permita añadir libros, eliminarlos y listar los disponibles.
3. **Mini Proyecto:** Implementa una API en FastAPI que gestione usuarios utilizando POO para estructurar los modelos y lógica de negocio.
