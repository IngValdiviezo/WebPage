# Importamos las librerías necesarias de Flask y extensiones

from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy  # ORM para manejar la base de datos
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from flask import request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import os  # Para operaciones del sistema si se necesitan
from flask import send_from_directory

# Creamos la instancia principal de la aplicación Flask
app = Flask(__name__)

# Configuramos la clave secreta para sesiones y seguridad (como cookies)
app.config['SECRET_KEY'] = 'tu_clave_secreta'

# Configuramos la conexión a la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Inicializamos SQLAlchemy con la app para manejar modelos y consultas
db = SQLAlchemy(app)

# Inicializamos el sistema de login
login_manager = LoginManager()
login_manager.init_app(app)  # Lo conectamos con la app Flask
login_manager.login_view = 'login'  # Si el usuario no está logueado, lo redirige a esta vista

# Creamos el modelo de usuario que se guardará en la base de datos
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID único para cada usuario
    email = db.Column(db.String(150), unique=True, nullable=False)  # Email del usuario
    password = db.Column(db.String(150), nullable=False)  # Contraseña cifrada

# Función que Flask-Login usa para cargar el usuario actual desde la base de datos
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Busca el usuario por ID

# Ruta principal que muestra la página de login
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Ruta para iniciar sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # Si el usuario envía el formulario
        email = request.form['email']  # Captura el email del formulario
        password = request.form['password']  # Captura la contraseña
        # Busca el usuario en la base de datos
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)  # Inicia sesión
            return redirect(url_for('dashboard'))  # Redirige al dashboard
        else:
            flash('Credenciales incorrectas')  # Muestra mensaje de error
    return render_template('login.html')  # Si es GET, muestra el formulario

# Ruta para registrar nuevos usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':  # Si el usuario envía el formulario
        email = request.form['email']
        password = request.form['password']
        # Cifra la contraseña antes de guardarla
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario registrado con éxito')  # Muestra mensaje de éxito
        return redirect(url_for('login'))  # Redirige al login
    return render_template('register.html')  # Si es GET, muestra el formulario

# Ruta protegida que solo se puede acceder si el usuario está logueado
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')  # Muestra el panel principal

# Ruta para cerrar sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Cierra la sesión
    return redirect(url_for('login'))  # Redirige al login

@app.route('/sources/<path:filename>')
def sources(filename):
    return send_from_directory('sources', filename)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Esto crea todas las tablas definidas en tus modelos
    app.run(debug=True)  # Ejecuta la app en modo desarrollo