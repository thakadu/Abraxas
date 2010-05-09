"""Represents a Tag on an Entry"""                                                                                                       
import logging
import datetime
import math

from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from abraxas.model import meta
from abraxas.model.meta import Session

log = logging.getLogger(__name__)

class Tag(object):

    @staticmethod
    def popular():
        """Returns the most popular recent tags"""
        s = text('''
            select lower, count(*) tagcount from tag
            where unix_timestamp(now())-unix_timestamp(created)<604800
            group by lower order by tagcount desc, lower 
            limit 30
        ''')
        tags = Session.execute(s).fetchall()
        return tags

