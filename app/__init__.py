from flask import Flask
from .database import get_db, close_db

def create_app():
    app = Flask(__name__)

    # Menentukan SECRET_KEY
    app.config['SECRET_KEY'] = 'secretkey'

    # DB Config 
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DATABASE'] = 'resto'

    # Menutup koneksi database otomatis
    @app.teardown_appcontext
    def teardown_db(exception):
        close_db()

    # ROUTES
    from .routes.main_routes import main
    app.register_blueprint(main)

    from .routes.pengguna_routes import pengguna
    app.register_blueprint(pengguna)

    from .routes.admin_routes import admin
    app.register_blueprint(admin)

    return app
