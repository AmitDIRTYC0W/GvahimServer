content_types = {
	'txt': 'text/plain',
	'htm': 'text/html',
	'jpeg': 'image/jpeg',
	'js': 'text/javascript; charset=UTF-8',
	'css': 'text/css',
	'ico': 'image/vnd.microsoft.icon'
}

def predict_content_type(path: str) -> bytes:
	for file_extension in content_types:
		if path.endswith(file_extension):
			return content_types[file_extension].encode()
