import yaml
from flask import Flask

# Configuration #

try:
	config = yaml.load(open('config.yml', 'r'))
except:
	raise Exception('Invalid config.yml')

# Application #

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, world!'

# Server #

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')

