from flask import Blueprint

posts_bp = Blueprint('posts', __name__)

# Aqui você define suas rotas e lógica de posts
# Exemplo:


@posts_bp.route('/create', methods=['POST'])
def create_post():
    pass


@posts_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    pass

# Importar mais funcionalidades conforme necessário
