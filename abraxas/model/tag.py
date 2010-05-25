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
        ntags = int(config.get('ntags', 20))
        s = text('''
            select lower, count(*) tagcount from tag
            where unix_timestamp(now())-unix_timestamp(created)<604800
            group by lower order by tagcount desc, lower 
            limit :limit
        ''')
        tags = Session.execute(s, dict(limit=ntags)).fetchall()
        return tags

