# blog_system/scripts/create_database.py
from core import create_app
from core.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Database created successfully.")
