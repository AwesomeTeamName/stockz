# stockz
Stock market simulator

## Setup
1. Install `virtualenv`.

		pip install virtualenv

2. Create a virtual environment using `virtualenv`.

		virtualenv venv

3. Activate the virtual environment.
	- Linux

			source venv/bin/activate
	- Windows

			venv\Scripts\activate.bat

4. Install requirements using `pip`.

		pip install -r requirements.txt

5. Start the application.

		python app.py
		
- You can also start the server on Linux using `./start.sh`. This requires `screen` to be installed and starts a detached screen session containing the process.
    - **Please note**: When using `start.sh`, any fatal errors will cause the session to die

## `*.py[co]` files
`*.py[co]` files are generated by the Python compiler and contain Python Bytecode. They are not required, and can be disabled using one of the following methods.

- Start the application using `python -B app.py`
- Set the environment variable `PYTHONDONTWRITEBYTECODE`
