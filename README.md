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

2. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

3. Abre tu navegador y ve a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver la aplicación en funcionamiento.

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

Company
└── manage.py
└── README.md
└── Company\asgi.py
└── Company\settings.py
└── Company\urls.py
└── Company\wsgi.py
└── Company\__init__.py
└── management\admin.py
└── management\apps.py
└── management\models.py
└── management\tests.py
└── management\views.py
└── management\__init__.py
└── management\migrations\0001_initial.py
└── management\migrations\0002_rename_start_date_leave_date_remove_leave_leave_type_and_more.py
└── management\migrations\0003_rename_reason_leave_actions_and_more.py
└── management\migrations\0004_remove_shift_actions_alter_leave_actions.py
└── management\migrations\0005_remove_leave_end_time_remove_leave_start_time.py
└── management\migrations\__init__.py


## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.