# Ejercicios para practicar

Aquí tienes algunos ejercicios prácticos enfocados en la creación de entornos virtuales con `env` y `poetry`, específicamente para el desarrollo de aplicaciones backend con **FastAPI**. Estos ejercicios te ayudarán a entender cómo gestionar dependencias, configurar entornos y utilizar herramientas para el desarrollo backend.

### 1. **Creación de un Entorno Virtual con `env`**
- **Objetivo**: Aprender a crear un entorno virtual con `env` y configurar un proyecto básico de FastAPI.
- **Instrucciones**:
  1. Crea un nuevo directorio para tu proyecto de FastAPI.
  2. Dentro del directorio, crea un entorno virtual usando `python -m venv .env`.
  3. Activa el entorno virtual.
  4. Instala FastAPI y Uvicorn (el servidor ASGI para ejecutar FastAPI) usando `pip install fastapi uvicorn`.
  5. Crea un archivo `main.py` con un endpoint básico de FastAPI, que responda con un "Hello, World!".
  6. Ejecuta el servidor de FastAPI con `uvicorn main:app --reload`.
  7. Accede a `http://127.0.0.1:8000` en tu navegador y verifica que el endpoint funcione.

### 2. **Manejo de Dependencias con `env`**
- **Objetivo**: Gestionar dependencias de manera eficiente en el entorno virtual con `env`.
- **Instrucciones**:
  1. Asegúrate de tener un entorno virtual activo.
  2. Instala algunas dependencias adicionales como `pydantic` (para validaciones de datos en FastAPI) y `databases` (para interactuar con bases de datos SQL).
  3. Genera un archivo `requirements.txt` con `pip freeze > requirements.txt`.
  4. Crea un nuevo entorno virtual, activa el entorno y utiliza `pip install -r requirements.txt` para instalar las dependencias.
  5. Verifica que tu aplicación siga funcionando correctamente con las dependencias instaladas.

### 3. **Creación de un Entorno Virtual con `poetry`**
- **Objetivo**: Usar `poetry` para crear y gestionar entornos virtuales y dependencias.
- **Instrucciones**:
  1. Instala `poetry` si aún no lo tienes: `pip install poetry`.
  2. Crea un nuevo proyecto con `poetry new fastapi_app` (esto generará la estructura básica de un proyecto).
  3. Dentro del directorio del proyecto, ejecuta `poetry init` para inicializar el entorno virtual y gestionar dependencias.
  4. Instala FastAPI y Uvicorn usando `poetry add fastapi uvicorn`.
  5. Crea un archivo `main.py` similar al ejercicio anterior con FastAPI.
  6. Ejecuta el servidor con `poetry run uvicorn main:app --reload` y verifica el funcionamiento del servidor.
  7. Usa `poetry show` para listar todas las dependencias instaladas en el entorno virtual.

### 4. **Gestión de Dependencias de Base de Datos con `poetry`**
- **Objetivo**: Aprender a gestionar dependencias relacionadas con bases de datos utilizando `poetry`.
- **Instrucciones**:
  1. En un proyecto existente de FastAPI creado con `poetry`, instala dependencias para manejar bases de datos. Por ejemplo, si vas a usar SQLite, instala `databases` con `poetry add databases sqlite`.
  2. Crea un archivo de configuración para la base de datos en FastAPI y configura un modelo básico.
  3. Crea un endpoint para realizar operaciones básicas de CRUD en la base de datos (por ejemplo, crear, leer y borrar datos de una tabla).
  4. Ejecuta la aplicación y verifica que las operaciones con la base de datos funcionen correctamente.

### 5. **Uso de Archivos `.env` para Configuración**
- **Objetivo**: Configurar variables de entorno con un archivo `.env` y gestionarlas con `python-dotenv`.
- **Instrucciones**:
  1. En tu proyecto de FastAPI, crea un archivo `.env` en la raíz del proyecto.
  2. Define algunas variables de entorno en el archivo `.env`, como `DATABASE_URL` para la conexión a la base de datos y `SECRET_KEY` para la configuración de seguridad.
  3. Instala la biblioteca `python-dotenv` con `poetry add python-dotenv`.
  4. En tu archivo `main.py`, carga estas variables de entorno utilizando `dotenv.load_dotenv()` y accede a ellas con `os.getenv()`.
  5. Asegúrate de que el proyecto funcione correctamente y que las variables de entorno estén siendo leídas desde el archivo `.env`.

### 6. **Configuración de Dependencias para Desarrollo con `poetry`**
- **Objetivo**: Configurar dependencias específicas para desarrollo y producción.
- **Instrucciones**:
  1. En tu proyecto de FastAPI con `poetry`, agrega dependencias para desarrollo como `pytest` (para pruebas unitarias) y `black` (para formateo de código).
  2. Usa `poetry add --dev pytest black` para instalar las dependencias de desarrollo.
  3. Crea un archivo de prueba básico que use `pytest` para probar un endpoint de FastAPI.
  4. Ejecuta las pruebas con `poetry run pytest` y verifica que todas las pruebas pasen.
  5. Asegúrate de que las dependencias de desarrollo no se incluyan en el entorno de producción.

### 7. **Estructura de Proyecto con `poetry` y FastAPI**
- **Objetivo**: Aprender a estructurar un proyecto de FastAPI utilizando `poetry` para gestionar dependencias y entornos.
- **Instrucciones**:
  1. Crea un proyecto de FastAPI con `poetry`.
  2. Estructura el proyecto de la siguiente manera:
     ```
     fastapi_app/
     ├── app/
     │   ├── __init__.py
     │   ├── main.py
     │   ├── models.py
     │   └── routers/
     │       └── items.py
     ├── pyproject.toml
     ├── .env
     └── README.md
     ```
  3. En `main.py`, incluye el código para inicializar la aplicación FastAPI y registrar los routers desde `routers/items.py`.
  4. Usa `poetry run uvicorn app.main:app --reload` para iniciar el servidor y verifica que la estructura modular funcione correctamente.

### 8. **Generación de Paquete de Distribución con `poetry`**
- **Objetivo**: Crear un paquete distribuible de tu aplicación backend.
- **Instrucciones**:
  1. Usa `poetry` para crear un paquete distribuible de tu aplicación FastAPI. Ejecuta `poetry build` para generar el paquete.
  2. Publica tu paquete en el índice de PyPI (o en un índice privado si lo prefieres).
  3. Instala el paquete en un nuevo entorno virtual usando `pip install <ruta_del_paquete>` y verifica que tu aplicación siga funcionando correctamente.

---

Estos ejercicios te ayudarán a familiarizarte con el uso de entornos virtuales, la gestión de dependencias y la configuración de proyectos backend con FastAPI utilizando herramientas como `env` y `poetry`. Cuando termines estos ejercicios, tendrás una sólida comprensión de cómo gestionar un entorno de desarrollo backend moderno.