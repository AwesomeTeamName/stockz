from flask import Blueprint, request, Response
from client import StockzClient

client = StockzClient()

blueprint = Blueprint('twilio', __name__)

twiml = """<?xml version="1.0" encoding="UTF-8" ?>
<Response>
    <Message>{0}</Message>
</Response>"""

def generate_response(message):
	return Response(twiml.format(message), mimetype='text/xml')

@blueprint.route('/twilio', methods = ['GET', 'POST'])
def twilio():
	if not 'Body' in request.form:
		return generate_response('Something went wrong!')

	user_message = request.form['Body']

	try:
		message = client.execute(user_message)
	except:
		message = 'Something went wrong!'

	response = twiml.format(message)
	return generate_response(message)
