from app import app
from flask import render_template, flash, redirect 
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Beautiful day in Sunderland'
        },
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logn requested fir user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
