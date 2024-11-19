# Ejercicios para practicar

Ahora vamos con algunos ejercicios para practicar **Programación Orientada a Objetos (POO)** en Python. Estos ejercicios te ayudarán a comprender y aplicar los conceptos fundamentales de la programación orientada a objetos, como clases, objetos, atributos, métodos, herencia, encapsulamiento y polimorfismo.

### 1. **Crear una Clase `Círculo`**
Crea una clase llamada `Círculo` que tenga un atributo `radio` y un método para calcular el área del círculo (usa la fórmula `π * radio^2`). Luego, crea un objeto de la clase y calcula el área.

### 2. **Simulación de un Banco**
Escribe una clase `CuentaBancaria` que tenga los siguientes atributos:
- `titular` (nombre del titular de la cuenta),
- `saldo` (saldo de la cuenta).
La clase debe tener métodos para:
- Depositar dinero,
- Retirar dinero,
- Consultar el saldo.
Asegúrate de que el saldo no sea negativo después de una retirada y que el titular sea un nombre válido.

### 3. **Herencia en Figuras Geométricas**
Crea una clase base llamada `Figura` con un método `area()`, que será sobrescrito por las clases derivadas `Círculo`, `Rectángulo` y `Triángulo`. Cada clase debe implementar su propia versión del método `area()`. Crea objetos de cada figura y calcula sus áreas.

### 4. **Estudiantes y Promedios**
Escribe una clase `Estudiante` con los siguientes atributos:
- `nombre`,
- `notas` (una lista de notas).
La clase debe tener un método para agregar notas y otro para calcular el promedio de las notas. Crea un objeto de la clase, agrega algunas notas y calcula el promedio.

### 5. **Control de Inventario**
Crea una clase `Producto` con los siguientes atributos:
- `nombre`,
- `precio`,
- `cantidad`.
La clase debe tener métodos para:
- Actualizar la cantidad de un producto,
- Calcular el valor total del inventario de ese producto (`precio * cantidad`).
Luego, crea una clase `Inventario` que contenga una lista de productos y un método para calcular el valor total de todos los productos en inventario.

### 6. **Juego de Adivinanza con Clases**
Crea una clase `JuegoAdivinanza` que tenga un atributo `numero` (el número secreto), y un método `adivinar()` que permita a los jugadores adivinar el número. Si el jugador adivina correctamente, el método debe indicar que ha ganado. Si el número es mayor o menor, el juego debe seguir pidiendo intentos.

### 7. **Vehículos y Herencia**
Crea una clase base `Vehículo` con los atributos `marca`, `modelo` y `año`. Luego, crea dos clases derivadas `Coche` y `Moto`, que añadan un atributo específico para cada tipo de vehículo, como `número de puertas` en el coche y `tipo de casco` en la moto. Crea objetos de cada tipo de vehículo y muestra sus atributos.

### 8. **Clases con Métodos Estáticos**
Escribe una clase llamada `Conversor` que tenga métodos estáticos para convertir entre unidades de medida. Por ejemplo, un método para convertir metros a kilómetros, o grados Celsius a Fahrenheit. Crea un objeto de la clase y usa los métodos estáticos sin necesidad de instanciar la clase.

### 9. **Clases con Métodos Privados**
Crea una clase `CuentaBancaria` donde el saldo sea un atributo privado (debe tener un nombre que empiece con `__`). La clase debe tener métodos públicos para depositar, retirar y consultar el saldo. Los métodos de depósito y retiro deben asegurar que el saldo nunca sea negativo.

### 10. **Polimorfismo en Animales**
Crea una clase base llamada `Animal` con un método `hacer_sonido()`. Luego, crea clases derivadas `Perro`, `Gato` y `Vaca`, que sobrescriban el método `hacer_sonido()` para hacer un sonido específico de cada animal. Crea una lista de objetos de estos animales y haz que cada uno haga su sonido, usando un solo ciclo `for`.

---

Estos ejercicios te ayudarán a mejorar tu comprensión de los principios fundamentales de la Programación Orientada a Objetos, como la creación de clases, la herencia, el polimorfismo, el encapsulamiento y los métodos estáticos.