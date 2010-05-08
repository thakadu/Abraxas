"""Fetches feeds and stores fetched items into database"""
import time
import socket
import datetime

from optparse import OptionParser 

import feedparser

from paste.deploy import appconfig
#from pylons import app_globals

from sqlalchemy import create_engine, MetaData, select
#from sqlalchemy.exc import IntegrityError
import sqlalchemy as sa

from abraxas.config.environment import load_environment
from abraxas.model.meta import Session
from abraxas.model import Feed
from abraxas.model import Fetch
from abraxas.model import Entry

from abraxas.lib.tag import *
socket.setdefaulttimeout(20)
feedparser.USER_AGENT = \
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.11) " + \
    "Gecko/20071127 Firefox/2.0.0.11"

# minumum time in minutes that must elapse before getting an rss update
throttle = 5 

def unix_time(dt):
    """Returns the Unix timestamp from a datetime object"""
    return time.mktime(dt.timetuple())

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('--ini',
                      help='INI file to use for application settings',
                      type='str',
                      default='development.ini')
    help_ = 'Force a download of the feed even if its within throttle time.'
    parser.add_option('--force',
                      help=help_,
                      action='store_true',
                      default=False)
    (options, args) = parser.parse_args()

    conf = appconfig('config:' + options.ini, relative_to='.')
    load_environment(conf.global_conf, conf.local_conf)

    engine = create_engine(conf['sqlalchemy.url'], echo=True)
    meta = MetaData()
    conn = engine.connect()

    entries = Session.query(Entry).filter_by(tags=None)
    for e in entries:
        text = e.title
        tags = tag(text)
        print tags
        e.tags = ' '.join(tags)
        Session.add(e)
    Session.commit()



