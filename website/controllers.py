# from app import app
from database.classes import Curso, Disciplina, Premio
from flask import Blueprint, render_template, request

website_bp = Blueprint(
    'website',
    __name__,
    template_folder='templates'
)


@website_bp.route('/')
def index():
    return render_template(
        'index.html',
        premios=Premio.listar()
    )


@website_bp.route('/sobre')
def sobre():
    return render_template(
        'sobre.html'
    )


@website_bp.route('/entrar')
def entrar():
    return render_template(
        'entrar.html'
    )


@website_bp.route('/contato', methods=['GET', 'POST'])
def contato():

    if request.method == 'POST':
        form = request.form
        print(f'''
        ++++ MENSAGEM ENVIADA ++++
        -> Nome: {form.get('nome')}
        -> E-mail: {form.get('email')}
        -> Assunto: {form.get('assunto')}
        -> Como Conheceu: {form.get('conheceu')}
        -> Mensagem:
        {form.get('mensagem')}
        ''')

    return render_template(
        'contato.html'
    )


@website_bp.route('/cursos/<sigla>')
def cursos(sigla):
    objeto = Curso.obter(sigla)
    disciplinas = Disciplina.filtrar(objeto.sigla)
    return render_template(
        'curso.html',
        curso=objeto,
        disciplinas=disciplinas
    )
