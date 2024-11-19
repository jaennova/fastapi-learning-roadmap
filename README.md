# FastAPI Learning Roadmap  

Este repositorio contiene mi progreso mientras sigo un roadmap para aprender **FastAPI** de forma práctica y estructurada.  

![Roadmap](./docs/roadmap-image.png)  

## **Índice de Contenidos**

### **1. Conceptos Básicos de Python**
- [Sintaxis y Estructura de Python](./src/part1-python-basics/theory/syntax_and_structure.md)
- [Funciones y Módulos](./src/part1-python-basics/theory/functions_and_modules.md)
- [Tipos de Datos y Variables](./src/part1-python-basics/theory/data_types_and_variables.md)
- [Operaciones de Control de Flujo](./src/part1-python-basics/theory/control_flow.md)
- [Manejo y Depuración de Excepciones](./src/part1-python-basics/theory/exceptions_debugging.md)
- [Programación Orientada a Objetos](./src/part1-python-basics/theory/OOP.md)

### **2. Introducción a FastAPI**
- [Breve Historia y Aplicaciones de FastAPI](./fastapi/introduction.md)
- [Ventajas de FastAPI](./fastapi/advantages.md)
- [Instalación de FastAPI](./fastapi/installation.md)
- [Entendiendo la Arquitectura de FastAPI](./fastapi/architecture.md)
- [Creando una Aplicación Básica en FastAPI](./fastapi/basic_app.md)

### **3. Trabajando con Rutas en FastAPI**
- [Conceptos de Rutas y Métodos HTTP](./fastapi/routes_and_methods.md)
- [Creando Rutas en FastAPI](./fastapi/creating_routes.md)
- [Manejando Parámetros de Ruta y Consulta](./fastapi/parameters.md)
- [Cargando y Devolviendo JSON](./fastapi/returning_json.md)

### **4. Validación de Datos con Pydantic**
- [Introducción a Pydantic](./pydantic/introduction.md)
- [Validación de Format y Manejo de Errores](./pydantic/validation_and_errors.md)
- [Creación de Modelos con Pydantic](./pydantic/models.md)
- [Uso de Modelos en FastAPI](./pydantic/models_in_fastapi.md)
- [Validación Avanzada con Pydantic](./pydantic/advanced_validation.md)

### **5. Autenticación y Autorización en FastAPI**
- [Introducción a OAuth2 y JWT](./auth/introduction_oauth2_jwt.md)
- [Implementando Autenticación con Password y Tokens](./auth/password_and_tokens.md)
- [Protegiendo Rutas con Dependencias](./auth/protecting_routes.md)
- [Roles y Permisos de Usuario](./auth/roles_and_permissions.md)
- [Errores en Autenticación y Autorización](./auth/errors.md)

### **6. Gestión de Bases de Datos**
- [Introducción a SQLAlchemy y Databases](./database/introduction_sqlalchemy.md)
- [Creación y Conexión a Bases de Datos](./database/connection.md)
- [Mapeo de Modelos con Pydantic y SQL](./database/model_mapping.md)
- [Ejecución de Consultas SQL](./database/sql_queries.md)

### **7. Gestión de Errores y Excepciones**
- [Definición de Excepciones Personalizadas](./errors/custom_exceptions.md)
- [Manejo de Errores con Middlewares](./errors/middleware_handling.md)
- [Registro de Errores](./errors/logging.md)
- [Testing de Casos de Error](./errors/error_testing.md)

### **8. Creación de Documentación**
- [Introducción a Swagger UI y ReDoc](./documentation/swagger_redoc.md)
- [Personalización de Documentación](./documentation/customization.md)

### **9. Pruebas Unitarias en FastAPI**
- [Introducción a PyTest](./testing/pytest_intro.md)
- [Creación de Pruebas](./testing/test_creation.md)
- [Interpretación de Resultados](./testing/result_analysis.md)

### **10. Despliegue de Aplicaciones FastAPI**
- [Despliegue en Local con Uvicorn e Hypercorn](./deployment/local_deployment.md)
- [Despliegue en la Nube (AWS, Google Cloud)](./deployment/cloud_deployment.md)
- [Diseño de un Plan de Despliegue](./deployment/deployment_plan.md)

### **11. Programación Avanzada con FastAPI**
- [Creación de APIs RESTful Complejas](./advanced/restful_apis.md)
- [Trabajando con Websockets y GraphQL](./advanced/websockets_graphql.md)
- [Optimización de Aplicaciones con Starlette](./advanced/optimization.md)
- [Integración con Aplicaciones de Terceros](./advanced/third_party_integration.md)

### **12. Proyectos Prácticos**
- [Aplicación CRUD de Notas](./projects/notes_crud.md)
- [Sistema de Autenticación de Usuarios](./projects/user_authentication.md)
- [Aplicación de Chat con Websockets](./projects/chat_websockets.md)
- [Despliegue de una Aplicación en la Nube](./projects/cloud_deployment.md)

---

## **Instrucciones**
1. Haz clic en cualquier tema para ir directamente al archivo correspondiente.
2. Sigue los ejercicios y ejemplos proporcionados en cada archivo.
3. Al final de cada tema encontrarás recursos adicionales para profundizar.


## Estructura del Repositorio  
- **`docs/`**: Documentación adicional, como diagramas e imágenes.  
- **`src/`**: Código dividido en carpetas por cada tema del roadmap.  
- **`tests/`**: Pruebas unitarias e integrales.  

## Cómo ejecutar los ejemplos  
1. Clona este repositorio:  
   ```bash
   git clone https://github.com/tu-usuario/fastapi-learning-roadmap.git
   ```
2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta un servidor de desarrollo con Uvicorn:

    ```bash
    uvicorn src.part2-intro-fastapi.main:app --reload
    ```