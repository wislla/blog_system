# Blog System

Este é um projeto de um sistema de blog construído com Flask, Flask-SQLAlchemy, Flask-Marshmallow e outras extensões. O objetivo é criar uma API para gerenciar posts e usuários em um blog.

## Estrutura do Projeto

```bash
blog_system/
├── api/
│ ├── auth.py
│ ├── posts.py
├── core/
│ ├── init.py
│ ├── config.py
│ ├── extensions.py
│ ├── models.py
│ ├── routes.py
│ └── schemas.py
├── scripts/
│ └── create_database.py
├── tests/
├── venv/
├── requirements.txt
└── pyproject.toml

```

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/wislla/blog_system.git
    cd blog_system
    ```

2. Instale as dependências usando Poetry:

    ```bash
    poetry install
    ```

3. Ative o ambiente virtual:

    ```bash
    poetry shell
    ```

## Configuração do Banco de Dados

1. **Criar o Banco de Dados e as Tabelas:**

    Execute o script para criar o banco de dados e as tabelas:

    ```bash
    poetry run python scripts/create_database.py
    ```

## Uso

1. **Rodar a Aplicação:**

    Inicie o servidor Flask:

    ```bash
    export FLASK_APP=manage.py
    export FLASK_ENV=development
    poetry run flask run
    ```

    A aplicação estará disponível em `http://127.0.0.1:5000/`.

2. **Adicionar Registros ao Banco de Dados via Shell Interativo:**

    Inicie o shell Flask:

    ```bash
    poetry run flask shell
    ```

    Adicione um novo post:

    ```python
    from core import create_app
    from core.models import db, Post

    app = create_app()
    with app.app_context():
        new_post = Post(title='Meu Primeiro Post', content='Este é o conteúdo do meu primeiro post.')

        db.session.add(new_post)
        db.session.commit()

        print(Post.query.all())
    ```

3. **Adicionar Registros ao Banco de Dados via API:**

    Você pode usar o endpoint `/posts` para criar novos posts. Envie uma requisição `POST` com o seguinte corpo JSON:

    ```json
    {
        "title": "Título do Post",
        "content": "Conteúdo do post."
    }
    ```

## Estrutura dos Modelos

- **Post:** Representa um post no blog com campos para `title` e `content`.

## Contribuindo

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações.
3. Faça um commit e envie suas alterações.
4. Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
