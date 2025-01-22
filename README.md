# Gestión de Empleados

## Descripción

Gestión de Empleados es una aplicación web desarrollada en Django que permite gestionar los turnos, ausencias y horarios de los empleados. La aplicación proporciona una interfaz intuitiva para añadir, listar y gestionar empleados, turnos y ausencias, así como generar reportes visuales.

## Características

- **Gestión de Empleados**: Añadir, listar y gestionar empleados.
- **Gestión de Turnos**: Programar y listar turnos de trabajo.
- **Gestión de Ausencias**: Registrar y listar ausencias de empleados.
- **Reportes**: Generar reportes visuales de turnos y ausencias.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd gestion-de-empleados
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

6. Abre tu navegador y ve a [http://127.0.0.1:8000/](http://_vscodecontentref_/0) para ver la aplicación en funcionamiento.

## Uso

### Gestión de Empleados

- **Añadir Empleado**: Navega a `/management/employees/add/` para añadir un nuevo empleado.
- **Listar Empleados**: Navega a `/management/employees/list/` para ver la lista de empleados.

### Gestión de Turnos

- **Añadir Turno**: Navega a `/management/shifts/add/` para programar un nuevo turno.
- **Listar Turnos**: Navega a `/management/shifts/list/` para ver la lista de turnos.

### Gestión de Ausencias

- **Añadir Ausencia**: Navega a `/management/leaves/add/` para registrar una nueva ausencia.
- **Listar Ausencias**: Navega a `/management/leaves/list/` para ver la lista de ausencias.

### Reportes

- **Ver Reportes**: Navega a `/management/report/` para generar y ver reportes visuales de turnos y ausencias.

## Estructura del Proyecto

Company/ init.py asgi.py settings.py urls.py wsgi.py db.sqlite3 manage.py management/ init.py admin.py apps.py migrations/ init.py 0001_initial.py ... models.py tests.py views.py templates/ company-verEspañol.html management/ add_employee.html add_leave.html add_shift.html employee_list.html leave_list.html report.html shift_list.html README.md


## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.