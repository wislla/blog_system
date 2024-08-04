# blog_system/core/routes.py
from flask import request, jsonify
from .models import Post
from .extensions import db


def register_routes(app):
    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.get_json()
        post = Post(title=data['title'], content=data['content'])
        db.session.add(post)
        db.session.commit()
        return jsonify({'id': post.id}), 201

    @app.route('/posts', methods=['GET'])
    def get_posts():
        posts = Post.query.all()
        return jsonify([
            {'id': p.id, 
             'title': p.title, 
             'content': p.content
             } 
            for p in posts
            ])

