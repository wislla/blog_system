from flask import Flask
from .extensions import db
from .routes import apply_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/database.db'
db.init_app(app)

# Importar e aplicar rotas após inicializar o app
apply_routes(app)
