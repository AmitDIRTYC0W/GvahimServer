import ashf
import os
from functools import partial

from content_types import predict_content_type

def _static_route(context: ashf.Ctxt, match, body: bytes, content_type: bytes):
	context.response.body = body
	context.response.status_code = 200
	context.response.reason_phrase = b'OK'
	context.response.headers[b'content-type'] = content_type

def static_page(path: str) -> ashf.utils.Route:
	with open(path, 'rb') as f:
		return partial(_static_route, body=f.read(), content_type=predict_content_type(path))

def use_dir(router: ashf.utils.Router, directory: str='.'):
	for root, dirs, files in os.walk(directory):
		for file in files:
			path = os.path.join(root, file)
			resource = path[len(directory):].replace('/', '\\/').encode()

			router.use(b'GET', resource, static_page(path))
