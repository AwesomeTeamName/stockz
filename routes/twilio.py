from flask import Blueprint, Response

blueprint = Blueprint('twilio', __name__)

@blueprint.route('/twilio')
def twilio():
	response = """<?xml version="1.0" encoding="UTF-8" ?>
<Response>
    <Message>I like cats!</Message>
</Response>"""
	return Response(response, mimetype='text/xml')
