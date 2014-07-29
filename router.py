import os, sys

imports = []

current_module = __import__(__name__)
current_path = os.path.dirname(os.path.realpath(__file__))

def load(name, path = current_path):
	sys.path.append(path)

	module = __import__(name)

	if hasattr(module, 'blueprint'): 
		imports.append(module.blueprint)
		setattr(current_module, name, module.blueprint)

	sys.path.remove(path)

def register_blueprints(app):
	for blueprint in imports:
		app.register_blueprint(blueprint)
