# blog_system/api/posts.py

from flask import Blueprint, request, jsonify
from core.models import Post
from core.extensions import db

posts_bp = Blueprint('posts', __name__)


@posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], 
                    content=data['content'], 
                    user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'})
