import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from abraxas.lib.base import BaseController, render

log = logging.getLogger(__name__)

class OtherController(BaseController):

    def download(self):
        return render('/download.mako')



