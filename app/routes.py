from flask import Flask, redirect, request, render_template, session, url_for, flash
from app import app
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)
from app.forms import PostForm
from flask_sqlalchemy import SQLAlchemy
from app.modules import Post
db = SQLAlchemy(app)





# function to render index page
@app.route('/')
def index():
	posts = Post.query.all()
	return render_template('blog.html', posts=posts)

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
	form = PostForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		text = form.text.data
		form.text.data = ''
		p = Post(name=name, text=text)
		db.session.add(p)
		db.session.commit()
		return redirect(url_for('index'))	
	return render_template('add_post.html', form=form)



"""@app.route('/delete/<int:id>')
def erase(id):
	
	# deletes the data on the basis of unique id and
	# directs to home page
	data = Post.query.get(id)
	db.session.delete(data)
	db.session.commit()
	return redirect('/')"""