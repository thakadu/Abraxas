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

socket.setdefaulttimeout(20)
feedparser.USER_AGENT = \
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.8.1.11) " + \
    "Gecko/20071127 Firefox/2.0.0.11"

# minumum time in minutes that must elapse before getting an rss update
throttle = 5 

def unix_time(dt):
    """Returns the Unix timestamp from a datetime object"""
    return time.mktime(dt.timetuple())

def fetch(feed):
    """Fetches entries from a feed and stores them in the database"""
    d = feedparser.parse(feed.url)
    got_entries = len(d['entries'])
    fetch_ = Fetch()
    fetch_.feed_id = feed.id
    fetch_.result = str(got_entries)
    Session.add(fetch_)
    feed.last_fetched_at = datetime.datetime.now()
    Session.add(feed)
    count = 0
    for e in d['entries']:
        url = e.get('link')
        exists = Session.query(Entry).filter_by(url=url).first()
        if exists: 
            continue
        title = e.get('title')
        
        # Try to get a published time, differs widely by feed..  
        published = e.get('published_parsed')
        if not published:
            published = e.get('updated_parsed')
        if not published:
            published = e.get('created_parsed')
        if not published:
            # If all aobe failed we will just use current gmtime
            published = time.gmtime()
        
        summary = e.get('summary')
        
        # Now save the entry into the db...
        entry = Entry()
        entry.feed_id = feed.id
        entry.title = title
        entry.url = url
        entry.pubtime = published
        entry.summary = summary
        Session.add(entry)
        Session.commit()
        count += 1
        
    Session.commit()
    return count
    

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

    feed_table = sa.Table('feed', meta, autoload=True, autoload_with=engine)
    query = select([feed_table])

    feeds = Session.query(Feed)
    for f in feeds:
        if f.last_fetched_at:
            ux_time_last_fetched = time.mktime(f.last_fetched_at.timetuple())
            print "last fetched: %s" % \
                (datetime.datetime.now() - f.last_fetched_at)
            seconds_ago = \
                unix_time(datetime.datetime.now()) - ux_time_last_fetched
        else:
            seconds_ago = 99999999
        print seconds_ago
        new = 0
        if seconds_ago < (throttle * 60) and not options.force:
            print "Not updating %s because inside throttle time." % f.title
        else:
            #try:
            new = fetch(f)
            #except:
            #    print 'Error updating feed %s' % f.title
            #    raise
        print "%s new entries added" % new
        print '----------------------------------'

