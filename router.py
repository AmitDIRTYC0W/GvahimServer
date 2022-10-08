from ashf.utils import Router

import errors
from calculate_next import calculate_next
import static

router = Router(errors.error_404, errors.error_405, errors.error_500)
router.use(b'GET', b'\\/', static.static_page('./wwwroot/index.htm'))
router.use(b'GET', b'\\/calculate-next', calculate_next)
static.use_dir(router, './wwwroot')