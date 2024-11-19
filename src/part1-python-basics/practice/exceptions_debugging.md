# Ejercicios para practicar

**Manejo y Depuración de Excepciones** en Python. Estos ejercicios te ayudarán a mejorar tus habilidades para manejar errores y excepciones utilizando `try`, `except`, `else`, `finally`, y te permitirán aprender cómo depurar tu código.

### 1. **Manejo de Entrada de Usuario Inválida**
Escribe un programa que reciba un número entero del usuario. Si el usuario ingresa algo que no sea un número (como una cadena de texto), el programa debe mostrar un mensaje de error adecuado y pedir al usuario que ingrese un número válido.

### 2. **División con Manejo de Errores**
Crea un programa que reciba dos números del usuario e intente realizar una división. Si el segundo número es cero, el programa debe capturar la excepción de división por cero y mostrar un mensaje de error. Si ambos números son válidos, el programa debe mostrar el resultado de la división.

### 3. **Leer un Archivo que No Existe**
Escribe un programa que intente abrir un archivo que no existe (por ejemplo, `"archivo_inexistente.txt"`) y maneje la excepción `FileNotFoundError`. Si el archivo no existe, el programa debe mostrar un mensaje adecuado. Si el archivo existe, debe mostrar su contenido.

### 4. **Conversión de Tipo Incorrecto**
Escribe un programa que reciba un valor del usuario y lo intente convertir en un número flotante. Si la conversión falla (por ejemplo, si el usuario ingresa texto que no se puede convertir a flotante), el programa debe manejar la excepción y mostrar un mensaje adecuado.

### 5. **Manejo de Múltiples Excepciones**
Escribe un programa que reciba dos números del usuario y realice la operación de suma, resta, multiplicación y división. Si el usuario ingresa un valor no numérico o intenta dividir entre cero, el programa debe manejar ambas excepciones (`ValueError` para entradas no numéricas y `ZeroDivisionError` para la división por cero).

### 6. **Ejemplo de Uso de `else` y `finally`**
Escribe un programa que reciba un número y calcule su raíz cuadrada. Si el número es negativo, el programa debe manejar la excepción `ValueError`. Usa un bloque `else` para imprimir el resultado de la raíz cuadrada si no ocurre ninguna excepción, y un bloque `finally` para imprimir un mensaje de que el proceso ha terminado, sin importar si hubo un error o no.

### 7. **Buscar un Elemento en una Lista**
Escribe un programa que reciba un número de una lista y lo busque. Si el número no está en la lista, debe capturar la excepción `ValueError` y mostrar un mensaje indicando que el número no está en la lista.

### 8. **Manejo de Excepciones Personalizadas**
Crea una excepción personalizada llamada `NumeroNegativoError` que se levante cuando el usuario ingrese un número negativo. Luego, crea un programa que reciba un número del usuario y lance esta excepción si el número es negativo, mostrando un mensaje personalizado.

### 9. **Calcular el Promedio de una Lista de Números**
Escribe un programa que reciba una lista de números y calcule su promedio. Si la lista está vacía, el programa debe lanzar una excepción personalizada llamada `ListaVaciaError` y mostrar un mensaje adecuado.

### 10. **Resta de Elementos de una Lista**
Escribe un programa que reciba una lista de números y calcule la resta sucesiva de los elementos (restando el siguiente número del anterior). Si la lista tiene menos de dos elementos, el programa debe lanzar una excepción personalizada que indique que no se puede realizar la operación.

---

Estos ejercicios te ayudarán a mejorar tu capacidad para manejar y depurar excepciones en Python, lo cual es crucial para escribir código robusto y seguro.