from flask import Blueprint

blueprint = Blueprint('twilio', __name__)

@blueprint.route('/twilio')
def twilio():
	return """<?xml version="1.0" encoding="UTF-8" ?>
<Response>
    <Message>I like cats!</Message>
</Response>"""
