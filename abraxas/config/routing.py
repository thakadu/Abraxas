"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    # Note that we need to specify the view and page  if using the entry controller
    # as it is referenced in the __before__ of BaseController
    map.connect('/', controller='entry', action='index', view='latest', page=0)
    map.connect('/Latest', controller='entry', action='index', view='latest', page=0)
    map.connect('/Latest/{page}', controller='entry', action='index', view='latest')
    map.connect('/latest', controller='entry', action='index', view='latest', page=0)
    map.connect('/latest/{page}', controller='entry', action='index', view='latest')

    map.connect('/tag/{keyword}', controller='entry', action='tag', view='tag', page=0)
    map.connect('/tag/{keyword}/{page}', controller='entry', action='tag', view='tag')

    map.connect('/Download', controller='other', action='download')
    map.connect('/About', controller='other', action='download')
    map.connect('/download', controller='other', action='download')
    map.connect('/about', controller='other', action='download')

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
