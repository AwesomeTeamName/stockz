import yaml, os.path, router
from flask import Flask

# Configuration #

try:
	config = yaml.load(open('config.yml', 'r'))

	if not isinstance(config, dict):
		raise Exception()
except:
	raise Exception('Invalid config.yml')

if not isinstance(config['flask'], dict):
	raise Exception('Missing flask from config')

if not isinstance(config['routes'], list):
	raise Exception('Missing routes from config')

if not isinstance(config['route_path'], str):
	raise Exception('Missing route_path from config')

# Application #

app = Flask(__name__)

for route in config['routes']:
	if os.path.isfile('./{0}/{1}'.format(config['route_path'], route)):
		raise Exception('route \"' + route + '\" not found')

	router.load(route, config['route_path'])

router.register_blueprints(app)

# Server #

if __name__ == '__main__':
	app.run(**config['flask'])