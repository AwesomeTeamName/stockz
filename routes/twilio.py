from flask import Blueprint, request, Response

blueprint = Blueprint('twilio', __name__)

twiml = """<?xml version="1.0" encoding="UTF-8" ?>
<Response>
    <Message>{0}</Message>
</Response>"""

@blueprint.route('/twilio')
def twilio():
	message = request.form['Body']
	response = twiml.format(message)
	return Response(response, mimetype='text/xml')
