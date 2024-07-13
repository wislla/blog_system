from .extensions import db, bcrypt
from datetime import datetime


class User():
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = (
            bcrypt.generate_password_hash(password).decode('utf-8'))

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Post():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = (
        db.Column(db.DateTime, nullable=False, default=datetime.utcnow))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
