# scripts/create_database.py

from blog_system import app, db
# from blog_system.models import User, Post

# Garantindo que estamos no contexto da aplicação Flask
with app.app_context():
    # Cria todas as tabelas definidas nos modelos
    db.create_all()

print("Banco de dados criado com sucesso!")
