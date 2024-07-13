# Blog System

Este é um projeto de um sistema de blog construído com Flask, Flask-SQLAlchemy, Flask-Marshmallow e outras extensões. O objetivo é criar uma API para gerenciar posts e usuários em um blog.

## Estrutura do Projeto

```bash
blog_system/
│
├── blog_system/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── posts.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_posts.py
│
├── create_database.py
├── pyproject.toml
├── README.md

```
## Configuração 

### Clone o repositório:


```console

git clone https://github.com/wislla/blog_system.git
cd blog_system
```
Crie e ative um ambiente virtual:

```bash

python3 -m venv venv
source venv/bin/activate
```
Instale as dependências usando Poetry:

```bash

poetry install
```

Configuração do Banco de Dados:

Crie o arquivo create_database.py para inicializar o banco de dados:

```python

# create_database.py

from blog_system.extensions import db
from blog_system import create_app

app = create_app()
with app.app_context():
    db.create_all()
```

Execute o script para criar o banco de dados:

```bash
  python create_database.py
```

Executando o Projeto
Ative o ambiente virtual:

```bash
source venv/bin/activate
```
Execute o servidor Flask:

```bash

  export FLASK_APP=blog_system
  export FLASK_ENV=development
  flask run
  
  Acesse a aplicação:
  
  Abra seu navegador e vá para http://127.0.0.1:5000.
```
# Estrutura dos Arquivos

    blog_system/init.py: Configura a aplicação Flask e inicializa as extensões.
    blog_system/api/: Contém os blueprints para autenticação e posts.
    blog_system/config.py: Configurações da aplicação.
    blog_system/extensions.py: Inicializa as extensões da aplicação (SQLAlchemy, Marshmallow, etc).
    blog_system/models.py: Define os modelos de banco de dados para usuários e posts.
    blog_system/schemas.py: Define os schemas de serialização para usuários e posts.
    blog_system/routes.py: Define as rotas da aplicação.
    tests/: Contém testes para a aplicação.

# Contribuição

    Fork o projeto.
    Crie uma nova branch (git checkout -b feature/MinhaFeature).
    Commit suas mudanças (git commit -m 'Adicionei uma nova feature').
    Push para a branch (git push origin feature/MinhaFeature).
    Abra um Pull Request.

# Licença
 Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
 
# Contato

Wislla - wislla21@gmail.com

Sinta-se à vontade para abrir uma issue se tiver alguma dúvida ou sugestão.
