"""Represents a Tag on an Entry"""                                                                                                       
import logging
import datetime
import math

from pylons import config
from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from abraxas.model import meta
from abraxas.model.meta import Session

log = logging.getLogger(__name__)

class Tag(object):

    @staticmethod
    def popular():
        """Returns the most popular recent tags"""
        log.info('*******popular method called in Tag class******')
        ntags = int(config.get('ntags', 20))
        hours = int(config.get('popular_tags_window', 72))
        s = text('''
            select lower, count(*) tagcount from tag
            where created > now() - interval :hours hour
            group by lower order by tagcount desc, lower 
            limit :limit
        ''')
        tags = Session.execute(s, dict(limit=ntags,hours=hours)).fetchall()
        return tags

