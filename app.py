import yaml, os
from flask import Flask

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
	app.run(host = '0.0.0.0', debug = True)
