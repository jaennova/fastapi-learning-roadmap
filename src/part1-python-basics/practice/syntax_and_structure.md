# **Sintaxis y Estructura**

### **Introducción**

La sintaxis y estructura son los fundamentos de cualquier lenguaje de programación. En esta sección, aprenderás los elementos básicos de Python, como palabras clave, indentación, y cómo estructurar tu código de forma clara y funcional. Estos conceptos son esenciales para escribir programas que sean legibles y fáciles de mantener.

---

### **Contenido**

#### **1. Palabras clave**
Las palabras clave en Python son identificadores reservados que tienen un significado especial y no pueden ser utilizadas como nombres de variables, funciones, o clases.

**Ejemplo:**
```python
# Algunas palabras clave en Python
if, else, for, while, def, return, class, import, try, except, finally, pass, break, continue, with, as
```

**Ver la lista completa de palabras clave:**
```python
import keyword
print(keyword.kwlist)
```

---

#### **2. Identificadores**
- Son los nombres que defines para variables, funciones, clases, etc.
- **Reglas:**
  - Pueden contener letras (a-z, A-Z), dígitos (0-9) y el guion bajo `_`.
  - No pueden comenzar con un dígito.
  - Sensibles a mayúsculas y minúsculas (`Variable` ≠ `variable`).

---

#### **3. Literales**
- Representan valores constantes en el código.
  - **Números:** `42`, `3.14`, `0b1010`.
  - **Cadenas:** `"Hola"`, `'Python'`.
  - **Booleanos:** `True`, `False`.

**Ejemplo:**
```python
num = 42
pi = 3.14
greeting = "Hola, Python"
flag = True
```

---

#### **4. Indentación**
- Python utiliza la indentación (espacios o tabulaciones) para definir bloques de código en lugar de llaves `{}`.
- La **consistencia** es crucial; se recomienda usar 4 espacios por nivel de indentación.

**Ejemplo correcto:**
```python
if True:
    print("Esto está correctamente indentado")
```

**Ejemplo incorrecto:**
```python
if True:
print("Error: falta indentación")  # Esto generará un error
```

---

#### **5. Comentarios**
- **Comentarios de una línea:** Usa `#` para añadir un comentario.
- **Comentarios de varias líneas:** Usa comillas triples (`'''` o `"""`).

**Ejemplo:**
```python
# Esto es un comentario de una línea
"""
Esto es un comentario
de varias líneas
"""
```

---

#### **6. Bloques de código**
- Los bloques de código en Python se definen mediante indentación. 
- Las estructuras como funciones, bucles, y condicionales terminan automáticamente al cambiar el nivel de indentación.

**Ejemplo:**
```python
def suma(a, b):
    resultado = a + b  # Este código pertenece al bloque de la función
    return resultado

print(suma(3, 5))  # Fuera del bloque
```

---

### **Buenas prácticas**

1. Usa 4 espacios por nivel de indentación.
2. Elige nombres de identificadores descriptivos y significativos.
3. Añade comentarios solo donde sea necesario para mejorar la comprensión del código.
4. Sigue las convenciones de estilo de Python (PEP 8).

---

### **Recursos adicionales**

- [PEP 8 - Guía de estilo para Python](https://peps.python.org/pep-0008/)
- [Documentación oficial sobre palabras clave](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
- [Guía de sintaxis en Python](https://docs.python.org/3/tutorial/introduction.html)
