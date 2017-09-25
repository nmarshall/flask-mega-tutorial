from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Nic' }
    posts = [
		{ 'author' : { 'nickname' : 'John' },
		  'body' : 'Beautiful day today!'
		},
		
		{ 'author' : { 'nickname' : 'Susan' },
		  'body' : 'The latest movie was terrible.'
		}
	]
    
    return render_template('index.html', title = 'Mega-tutorial', user = user, posts = posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login returested for OpenID="%s", remember_me="%s"' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In',
							form=form)
    