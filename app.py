import re
import os
import ashf
from functools import partial

from router import router

app = ashf.Ashf()
app.early_use(ashf.utils.timeout(0.1))
app.use(router)
app.use(ashf.utils.content_encode)
app.use(ashf.utils.content_length)
app.compile()

print(f'Listening on http://localhost:8080')
app.listen(port=8080)