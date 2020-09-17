from flask import flash, redirect, render_template, url_for, request
from flask_login import login_user, logout_user, current_user

from consistente import app, lm, db
from consistente.models.forms import LoginForm, UserEditForm
from consistente.models.tables import User


@lm.user_loader
def load_user(session_token):
    return User.query.filter_by(id=session_token).first()

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.is_submitted() and form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash('Acesso liberado!')
            return redirect(url_for("home"))            
        else:
            flash('Senha inválida.')
    return render_template(
        'admin/login.html', 
        form=form
    )

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))            

@app.route("/")
@app.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template('home.html')
    return redirect('login')

@app.route('/users/', methods=["GET"])
def list_users():
    form = request.args
    filter_data = {}
    username = None
    name = None
    for i in form:
        if i == 'username' and form['username']:
            username = form[i]
            filter_data['username'] = form[i]
        if i == 'name' and form['name']:
            name = form[i]
            print(name)
            filter_data['name'] = form[i]
    u = User.query.filter_by(**filter_data)
    data = []
    for i in u:
        data.append(
            [
                {'t': i.username}, {'t': i.name}, {'t': i.email}, {'t': i.phone}, {'b': {'caption': 'Editar', 'href': '/users/edit/' + str(i.id)}}
            ]
        )
    table_data = {
        'href': '/users/add',
        'headers': ['Usuário', 'Nome Completo', 'Email', 'Telefone', 'Status'],
        'data': data
    }
    table = render_template(
        'table_default.html',
        table=table_data,
    )
    return render_template(
        'admin/user_list.html',
        table=table,
        username=username,
        name=name
    )

@app.route('/users/add/', methods=["GET", "POST"], defaults={'user': None})
@app.route('/users/edit/<user>', methods=["GET", "POST"])
def edit_users(user):
    if user:
        # Edição de usuários existentes.
        u = User.query.filter_by(id=user).first()
        if u:
            form = UserEditForm(
                username=u.username,
                name=u.name,
                email=u.email,
                phone=u.phone,
                password=u.password,
                active=u.active
            )
        else:
            flash('Usuário não localizado!', 'error')
            form = UserEditForm()
        if form.is_submitted() and form.validate_on_submit:
            try:
                u.username = form.username.data
                u.name = form.name.data
                u.email = form.email.data
                u.phone = form.phone.data
                u.password = form.password.data
                u.save()
                flash('Usuário alterado com sucesso!', 'info')
                return redirect('/users/')
            except:
                flash('Existe alguma informação errado no formulário! Revise.', 'warning')
                return redirect('/users/')
        else:
            return render_template(
                'admin/user_edit.html',
                form=form
            )
    else:
        # Inclusão de novos usuários.
        form = UserEditForm()
        if form.is_submitted() and form.validate_on_submit:
            try:
                u = User(
                    username=form.username.data,
                    name=form.name.data,
                    email=form.email.data,
                    phone=form.phone.data,
                    password=form.password.data,
                    active=form.active.data,
                )
                db.session.add(u)
                db.session.commit()
                flash('Usuário adicionado com sucesso!', 'info')
                return redirect('/users/')
            except:
                flash('Existe alguma informação errado no formulário! Revise.', 'warning')
                return redirect('/users/')
        else:
            return render_template(
                'admin/user_edit.html',
                form=form
            )

@app.route('/renan/', defaults={'name': None})
@app.route('/renan/<name>')
def renan(name):
    if name:
        # return "<h1>Olá, {}!</h1>".format(name)
        return render_template('renan.html', name=name)
    else:
        #return "<h1>Olá, Usuário!</h1>"
        table = {
            'headers': ['Nome', 'Endereço', 'Telefone'],
            'data': [
                ['Renan Souza', 'Rua França, 161', '16 981579135'],
                ['Elton Souza', 'Rua XXX, 161', '16 981579135'],
            ]
        }
        return render_template('table_default.html', table=table)
