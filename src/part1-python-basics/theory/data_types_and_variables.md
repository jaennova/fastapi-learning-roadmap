# **Tipos de Datos y Variables**

### **Introducción**

Los tipos de datos y las variables son la base para almacenar y manipular información en Python. Comprenderlos te ayudará a trabajar con datos de manera eficiente y evitar errores comunes. En esta sección, aprenderás a declarar variables, identificar tipos de datos y trabajar con las estructuras básicas.

---

### **Contenido**

#### **1. Variables**
- Las **variables** son contenedores para almacenar valores.
- En Python, no necesitas declarar explícitamente el tipo de una variable; el intérprete lo asigna automáticamente según el valor.

**Declaración:**
```python
nombre = "Juan"  # Variable de tipo cadena
edad = 25        # Variable de tipo entero
pi = 3.14        # Variable de tipo flotante
```

#### **Reglas para nombres de variables**
1. Deben comenzar con una letra o un guion bajo (`_`).
2. Pueden contener letras, números y guiones bajos.
3. No pueden ser palabras clave reservadas de Python.
4. Sensibles a mayúsculas (`edad` ≠ `Edad`).

---

#### **2. Tipos de datos básicos**
Python tiene varios tipos de datos incorporados para representar información:

##### **a) Tipos numéricos**
- **Enteros (`int`):** Números sin decimales.
- **Flotantes (`float`):** Números con decimales.
- **Complejos (`complex`):** Números en forma `a + bj`.

**Ejemplo:**
```python
entero = 10
flotante = 3.14
complejo = 1 + 2j
```

##### **b) Tipo cadena (`str`)**
- Almacenan texto entre comillas simples o dobles.

**Ejemplo:**
```python
mensaje = "Hola, Python"
```

##### **c) Tipo booleano (`bool`)**
- Representan valores de verdad: `True` o `False`.

**Ejemplo:**
```python
es_mayor = True
```

##### **d) Tipo None**
- Representa la ausencia de valor o dato.

**Ejemplo:**
```python
variable = None
```

---

#### **3. Estructuras de datos**
Las estructuras de datos permiten almacenar colecciones de valores.

##### **a) Listas (`list`)**
- Una colección ordenada y modificable.

**Ejemplo:**
```python
frutas = ["manzana", "banana", "cereza"]
frutas.append("uva")  # Agregar un elemento
```

##### **b) Tuplas (`tuple`)**
- Una colección ordenada e inmutable.

**Ejemplo:**
```python
colores = ("rojo", "verde", "azul")
```

##### **c) Diccionarios (`dict`)**
- Una colección no ordenada de pares clave-valor.

**Ejemplo:**
```python
persona = {"nombre": "Juan", "edad": 30}
print(persona["nombre"])
```

##### **d) Conjuntos (`set`)**
- Una colección no ordenada de elementos únicos.

**Ejemplo:**
```python
numeros = {1, 2, 3, 3}  # El conjunto será {1, 2, 3}
```

---

#### **4. Conversión de tipos**
Convierte un dato de un tipo a otro usando funciones integradas.

**Ejemplo:**
```python
entero = 42
cadena = str(entero)  # Convertir a cadena
flotante = float(entero)  # Convertir a flotante
```

---

### **Buenas prácticas**

1. Usa nombres descriptivos para las variables:
   ```python
   edad_usuario = 25
   ```
2. Inicializa las variables antes de usarlas.
3. Evita sobrescribir palabras clave reservadas:
   ```python
   # Incorrecto
   list = [1, 2, 3]  # 'list' es una palabra clave
   ```

---

### **Recursos adicionales**

- [Tipos de datos en Python](https://docs.python.org/3/library/stdtypes.html)
- [Guía de conversión de tipos](https://docs.python.org/3/library/functions.html#type)
- [Documentación oficial sobre estructuras de datos](https://docs.python.org/3/tutorial/datastructures.html)
