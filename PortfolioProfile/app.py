import logging
import os

from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix

from models import db, Project  # import db and Project model
from flask_migrate import Migrate

# Remove these imports once DB is used
# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get(
		"SESSION_SECRET", "dev-secret-key-change-in-production"
)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
# Configure SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
	projects = Project.query.all()  # Query projects from DB
	return render_template('index.html', projects=projects)


@app.route('/project/<int:project_id>')
def project_detail(project_id):
	project = Project.query.get(project_id)
	if not project:
		flash('Project not found.', 'error')
		return redirect(url_for('index'))
	return render_template('project.html', project=project)


@app.route('/about')
def about():
	"""About section with personal/professional information"""
	return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	"""Contact section with a contact form"""
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		message = request.form.get('message')

		if name and email and message:
			# In a real application, you would send an email or save to database
			flash(
					f'Thank you {name}! Your message has been sent. I\'ll get back to you soon.',
					'success'
			)
			return redirect(url_for('contact'))
		else:
			flash('Please fill in all fields.', 'error')

	return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(e):
	"""Custom 404 page"""
	return render_template('404.html'), 404


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
