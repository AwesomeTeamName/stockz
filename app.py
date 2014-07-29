import yaml
from flask import Flask
import router

# Configuration #

try:
	config = yaml.load(open('config.yml', 'r'))

	if not isinstance(config, dict):
		raise Exception()
except:
	raise Exception('Invalid config.yml')

if not isinstance(config['flask'], dict):
	raise Exception('Missing flask from config')

# Application #

app = Flask(__name__)

# Server #

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')

