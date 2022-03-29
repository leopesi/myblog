### Confira o app em https://sifat-blog-teste.herokuapp.com/about
- usuário de teste: guest
- password: 12345678!


# Projeto Postagem - Django framework

### Criar um site de postagem:
- Deverá ter um CRUD (Create, Read, Update, Delete) 
- As informações que devem estar dentro do CARD
- Título – Data – Texto - Autor

### Regras:
- O Texto digitado pelo usuário deverá ser salvo com letra maiúscula;
- As postagens devem estar ordenadas, o que for cadastrado por último deverá estar no
topo da postagem;
- Responsividade obrigatória;
- Inserir navigation bar com:
o Apresentação do Site (Sobre);
o Postagens publicadas;
o Faça sua postagem

 ## Recursos utilizados - *Built with*
- [x] Python 
- [x] Django
- [x] PostgreSQL
- [x] Heroku 
- [x] Virtualenv
- [x] Git e Github
- [x] JavaScript, HTML, CSS e Bootstrap
- [x] Git e Github

## Como instalar? - *How to install?*

**Clone o repositório.**
*Clone this repository*

$ git clone https://github.com/leopesi/myblog.git

**Crie um virtualenv** - *Creating a virtualenv*

- 'pip install virtualenv'
- virtualenv nome_da_virtualenv

**Ativando uma virtualenv** - *Activating a virtialenv*

- souce nome_da_virtualenv/bin/activate (Linux ou macOS)
- nome_da_virtualenvScriptsactivate (Windows)

**Instale as depêndencias.** - *Installing dependencies*
- pip install -r requirements.txt

**Criação das tabelas no DB.** - *Creating tables in DB*
- py manage.py makemigrations
- py manage.py migrate

**Criação de superusuário.** - *Creating SuperUser*
- py manage.py createsuperuser

**Lançamento.** - *Launch*
- py manage.py runserver


