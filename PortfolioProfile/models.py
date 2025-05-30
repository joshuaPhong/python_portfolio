from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
	__tablename__ = 'projects'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(150), nullable=False)
	category = db.Column(db.String(100), nullable=False)
	description = db.Column(db.Text, nullable=False)
	image = db.Column(db.String(500), nullable=True)

	# Flattened details
	client = db.Column(db.String(150))
	year = db.Column(db.String(4))
	technologies = db.Column(db.Text)  # store as comma-separated string
	challenge = db.Column(db.Text)
	solution = db.Column(db.Text)
	result = db.Column(db.Text)

	def tech_list(self):
		"""Return technologies as a list"""
		return self.technologies.split(', ') if self.technologies else []

	def __repr__(self):
		return f'<Project {self.title}>'
