# Proyectos para poner en practica las bases de python

### 1. **Sistema de Gestión de Biblioteca**
Crea un sistema para gestionar una biblioteca donde puedas:
- Agregar libros con atributos como título, autor, género, y si está disponible o prestado.
- Prestar libros a usuarios (usando una clase `Usuario` que tenga el nombre y los libros que ha prestado).
- Controlar la disponibilidad de los libros.
- Permitir la devolución de libros y actualizar el estado de disponibilidad.
  
**Conceptos involucrados:**
- POO: Clases para `Libro`, `Usuario`, `Biblioteca`.
- Excepciones: Manejo de casos como libro no disponible o usuario que no existe.
- Control de flujo: Condicionales para manejar los estados de los libros.
- Métodos: Para prestar libros, devolver libros, y ver los libros disponibles.

### 2. **Aplicación de Control de Gastos**
Desarrolla una aplicación que permita a los usuarios registrar y categorizar sus gastos:
- Los usuarios pueden ingresar gastos y asignarles categorías (alimentación, entretenimiento, transporte, etc.).
- El sistema debe permitir ver el total gastado por categoría y el total general.
- Los usuarios deben poder actualizar y eliminar gastos, y el sistema debe actualizar los totales automáticamente.
  
**Conceptos involucrados:**
- POO: Clases para `Gasto`, `Categoria`, `Usuario`.
- Manejo de excepciones: Verificar que los gastos ingresados sean numéricos y que las categorías existan.
- Control de flujo: Usar ciclos para mostrar los gastos y calcular totales.
- Herencia: Puedes extender la funcionalidad agregando diferentes tipos de usuarios (por ejemplo, usuario administrador y usuario normal).
  
### 3. **Juego de Rol por Texto**
Desarrolla un juego de rol simple donde los jugadores puedan elegir entre diferentes personajes (por ejemplo, guerrero, mago, arquero). Cada personaje tendrá:
- Atributos como salud, fuerza, y defensa.
- Métodos para atacar, defender y usar habilidades especiales.
- Un sistema de combate que permita a los personajes luchar contra enemigos y ganar experiencia.

**Conceptos involucrados:**
- POO: Clases para `Personaje`, `Enemigo`, `Habilidad`, `Combate`.
- Herencia: Crear subclases como `Guerrero`, `Mago` y `Arquero` que heredan de `Personaje`.
- Excepciones: Manejar errores de entrada de usuario (por ejemplo, si el usuario elige un personaje inexistente).
- Control de flujo: Uso de condicionales para definir las interacciones y resultados del combate.
  
### 4. **Sistema de Gestión de Tareas**
Desarrolla una aplicación para gestionar tareas y proyectos:
- Los usuarios pueden agregar, editar y eliminar tareas.
- Las tareas pueden tener fechas límite y prioridades (baja, media, alta).
- El sistema debe permitir ver las tareas por prioridad, por fecha límite o por estado (completada/no completada).
  
**Conceptos involucrados:**
- POO: Clases para `Tarea`, `Proyecto`, `Usuario`.
- Métodos: Métodos para agregar, eliminar y editar tareas.
- Excepciones: Manejo de excepciones al agregar tareas (por ejemplo, evitar que se ingresen tareas sin nombre).
- Control de flujo: Condicionales para filtrar tareas por prioridad y fechas.
  
### 5. **Simulador de Tienda de Ropa Online**
Crea una tienda online donde los usuarios puedan:
- Ver los productos disponibles (con nombre, precio, tamaño y cantidad).
- Agregar productos al carrito de compras.
- Calcular el total de la compra, incluyendo descuentos si aplican.
- Realizar el pago (con una opción ficticia de pago).
  
**Conceptos involucrados:**
- POO: Clases para `Producto`, `CarritoDeCompras`, `Usuario`, `Pago`.
- Excepciones: Verificación de stock antes de agregar productos al carrito.
- Control de flujo: Cálculo de totales, aplicación de descuentos y gestión del carrito.
- Métodos: Métodos para agregar productos al carrito, calcular totales y procesar el pago.
  
### 6. **Sistema de Reserva de Vuelos**
Desarrolla un sistema de reservas de vuelos donde los usuarios puedan:
- Buscar vuelos según destino, fecha y disponibilidad.
- Realizar reservas, especificando nombre, número de pasajeros y detalles de pago.
- Ver el estado de la reserva (confirmada o pendiente).
  
**Conceptos involucrados:**
- POO: Clases para `Vuelo`, `Reserva`, `Usuario`, `Pago`.
- Excepciones: Manejo de excepciones cuando un vuelo no esté disponible o cuando la entrada de datos sea incorrecta.
- Control de flujo: Condicionales para verificar disponibilidad de vuelos y fechas.
  
### 7. **Sistema de Gestión de Empleados**
Desarrolla un sistema para gestionar empleados dentro de una empresa:
- Los empleados tienen atributos como nombre, puesto, salario y fecha de contratación.
- El sistema permite agregar, editar, eliminar y mostrar empleados.
- El sistema también permite calcular el salario mensual de los empleados, aplicando bonificaciones si corresponde.
  
**Conceptos involucrados:**
- POO: Clases para `Empleado`, `Departamento`, `Empresa`.
- Métodos: Métodos para agregar, editar, eliminar y mostrar empleados.
- Excepciones: Manejar errores en la entrada de datos, como salario negativo o fecha de contratación inválida.
- Control de flujo: Condicionales para calcular bonificaciones y verificar requisitos.

---

### Consideraciones:
- **Interfaz de Usuario**: No es necesario, pero puedes mejorar estos proyectos con una interfaz de usuario (CLI o GUI usando módulos como `Tkinter`).
- **Persistencia de Datos**: Para hacerlo más desafiante, puedes almacenar la información en archivos (por ejemplo, JSON o CSV) o utilizar una base de datos (como SQLite).
- **Escalabilidad**: Estos proyectos pueden ampliarse para agregar más funcionalidades, como administración de roles de usuario (por ejemplo, administrador, usuario común) o interacciones más complejas.

Estos proyectos son lo suficientemente complejos como para permitirte poner en práctica todos los conceptos aprendidos, sin que se sientan forzados. Además, ofrecen una excelente manera de demostrar tus habilidades de programación y lógica en situaciones del mundo real.