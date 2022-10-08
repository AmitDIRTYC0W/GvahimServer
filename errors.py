from ashf import Ctxt

def error_404(context: Ctxt):
	context.response.body = b'<html><head><title>Not Found</title></head><body><h2>Error: Not Found</h2></body></html>'
	context.response.status_code = 404
	context.response.reason_phrase = b'Not Found'

def error_405(context: Ctxt):
	context.response.body = b'<html><head><title>Method Not Allowed</title></head><body><h2>Error: Method Not Allowed</h2></body></html>'
	context.response.status_code = 405
	context.response.reason_phrase = b'Method Not Allowed'

def error_500(context: Ctxt):
	context.response.body = b'<html><head><title>Internal Server Error</title></head><body><h2>Error: Internal Server Error</h2></body></html>'
	context.response.status_code = 500
	context.response.reason_phrase = b'Internal Server Error'
