import ashf
import re

def calculate_next(context: ashf.Ctxt, match: re.Match):
	try:
		num = int(context.request.parameters[b'num'])

		context.response.body = str(num + 1).encode()
		context.response.status_code = 200
		context.response.reason_phrase = b'OK'
	except:
		context.response.body = b'<html><head><title>Bad Request</title></head><body><h2>Error: Bad Request</h2></body></html>'
		context.response.status_code = 400
		context.response.reason_phrase = b'Bad Request'
