import yaml, os
from flask import Flask

# Configuration #

try:
	config = yaml.load(open('config.yml', 'r'))

	if not isinstance(config, dict):
		raise Exception()
except:
	raise Exception('Invalid config.yml')

if 'flask' not in config or not isinstance(config['flask'], dict):
	raise Exception('Missing flask from config')

# Application #

app = Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.secret_key = os.urandom(16)

# Routes #

@app.route('/')
def index():
	return 'Hello!'

# Server #

if __name__ == '__main__':
	app.run(**config['flask'])
