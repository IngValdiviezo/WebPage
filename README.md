# Clínica de Psicología Web

Una aplicación web desarrollada con Flask para una clínica de psicología que ofrece servicios de terapia individual, en línea, de pareja y familiar.

## Características

- **Página de inicio** con información sobre los servicios
- **Servicios** - Descripción detallada de terapias disponibles
- **Acerca de** - Información sobre la clínica
- **Contacto** - Formulario de contacto para citas
- **Sistema de autenticación** con Flask-Login
- **Base de datos** SQLite para gestión de usuarios
- **Diseño responsivo** con Bootstrap

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de datos**: SQLite con SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Autenticación**: Flask-Login
- **Seguridad**: Werkzeug para hash de contraseñas

## Instalación y Configuración

### Requisitos previos
- Python 3.7+
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/psicologia-web.git
cd psicologia-web
```

2. Crea un entorno virtual:
```bash
python -m venv venv
```

3. Activa el entorno virtual:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. Instala las dependencias:
```bash
pip install flask flask-sqlalchemy flask-login werkzeug
```

5. Ejecuta la aplicación:
```bash
python app.py
```

6. Abre tu navegador y ve a `http://127.0.0.1:5000`

## Estructura del Proyecto

```
PsicologiaWeb/
├── app.py                 # Aplicación principal Flask
├── instance/              # Carpeta de instancia (base de datos)
│   └── database.db       # Base de datos SQLite
├── static/               # Archivos estáticos
│   ├── style.css        # Estilos CSS
│   └── main.js          # JavaScript
├── templates/            # Plantillas HTML
│   ├── base.html        # Plantilla base
│   ├── home.html        # Página de inicio
│   ├── services.html    # Página de servicios
│   ├── about.html       # Página acerca de
│   └── contact.html     # Página de contacto
└── sources/             # Recursos e imágenes
```

## Funcionalidades

- **Gestión de usuarios**: Registro e inicio de sesión
- **Páginas informativas**: Servicios, acerca de, contacto
- **Interfaz intuitiva**: Diseño profesional y responsivo
- **Formularios de contacto**: Para solicitar citas y consultas

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para más información sobre este proyecto, puedes contactar al desarrollador.
