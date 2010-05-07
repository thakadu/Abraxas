"""Loads Feed data from a csv file into the feed table of the database"""
import logging
import csv

from optparse import OptionParser 

from paste.deploy import appconfig
#from pylons import app_globals
from abraxas.config.environment import load_environment

from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import IntegrityError
import sqlalchemy as sa

"""
The format of the input file should be csv with these fields
Title, Web Url, Feed Url
"""

log = logging.getLogger(__name__)

class DataFormatException(Exception):
    """Raise when the csv file does not have the correct number of fields"""
    pass

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('--ini',
                      help='INI file to use for application settings',
                      type='str',
                      default='development.ini')
    parser.add_option('--filename',
                      help='File containing place names data.',
                      type='str',
                      default='data/feeds.csv')
    (options, args) = parser.parse_args()

    conf = appconfig('config:' + options.ini, relative_to='.')
    load_environment(conf.global_conf, conf.local_conf)

    engine = create_engine(conf['sqlalchemy.url'], echo=True)
    meta = MetaData()
    conn = engine.connect()
    print conn

    fh = open(options.filename)
    reader = csv.reader(fh)

    feed_table = sa.Table('feed', meta, autoload=True, autoload_with=engine)

    for line in reader:
        if len(line) != 3:
            raise DataFormatException
        title = line[0]
        weburl = line[1]
        url = line[2]
        insert = feed_table.insert().values(
            title=title,
            url=url,
            weburl=weburl)
        try:
            conn.execute(insert)
        except IntegrityError:
            # Most likely loading a duplicate feed row
            log.debug("Duplicate row, skipping this line...")
            continue

