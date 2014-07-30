from flask import Blueprint, request, Response
from client import StockzClient

client = StockzClient()

blueprint = Blueprint('twilio', __name__)

twiml = """<?xml version="1.0" encoding="UTF-8" ?>
<Response>
    <Message>{0}</Message>
</Response>"""

@blueprint.route('/twilio', methods = ['GET', 'POST'])
def twilio():
	try:
		message = client.execute('hello')
	except:
		message = 'Something went wrong!'

	response = twiml.format(message)
	return Response(response, mimetype='text/xml')
