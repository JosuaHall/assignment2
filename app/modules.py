from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate, migrate
from app import app


# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ifa16A2019nD%21@localhost/blogpostsHW2'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

# Models
class Post(db.Model):
	# Id : Field which stores unique id for every row in
	# database table.
	# first_name: Used to store the first name if the user
	# last_name: Used to store last name of the user
	# Age: Used to store the age of the user
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), unique=False, nullable=False)
	text = db.Column(db.Text, unique=False, nullable=False)
	created_date = db.Column(db.DateTime(timezone=True), default=func.now())
	# repr method represents how one object of this data table
	# will look like
	#def __repr__(self):
	#	return f"Name : {self.first_name}, Age: {self.age}"