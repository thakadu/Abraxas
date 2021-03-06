"""The base Controller API

Provides the BaseController class for subclassing.
"""
import logging

from pylons.controllers import WSGIController
from pylons.controllers.util import abort
from pylons.templating import render_mako as render
from pylons import cache, config
from pylons import request, response, session, tmpl_context as c

from abraxas.model.meta import Session
from abraxas.model import Tag, Feed

log = logging.getLogger(__name__)

class BaseController(WSGIController):

    def __before__(self, **kwds):

        # Load the hot tags from cache
        mycache = cache.get_cache('hot_tags')
        log.debug('before call to mycache.get_value("tags"))')
        c.tags = mycache.get_value(key='tags', createfunc=Tag.popular,
                                   type="memory", expiretime=3600)

        log.debug('after call to mycache.get_value("tags"))')

        c.sources = mycache.get_value(key='sources', createfunc=Feed.active_feeds,
                                    type='memory', expiretime=3600)

        log.debug('after call to mycache.get_value("feeds"))')

        # Pass the logo_file name to the template context
        c.logo_file = config.get('logo_file', 'logo.png')

        # Pass the site sub-title to the template context
        c.subtitle = config.get('banner_subtitle', None)

        # Set up pagination
        if self.__class__.__name__ == 'EntryController':
            if not 'view' in kwds:
                return
            c.pagesize = 25
            c.totlinks = 5000 # Probably should look this up from db and cache it...
            c.page = kwds.get('page', 0)
            try:
                c.page_numeric = long(c.page)
            except:
                abort(404)
            if c.page_numeric < 0:
                abort(404)
            c.slicestart = c.pagesize * c.page_numeric


    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()
