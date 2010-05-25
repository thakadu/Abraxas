"""Represents a Feed (RSS/Atom or other)"""                                                                                                       
import logging
import datetime
import math

import sqlalchemy as sa
from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from abraxas.model import meta

log = logging.getLogger(__name__)

class Feed(object):

    @staticmethod
    def active_feeds():
        """Returns the a list of active feeds"""
        feed_table = sa.Table('feed', meta.metadata, autoload=True)
        query = meta.Session.execute(
            select([feed_table.c.title, 
                    feed_table.c.weburl],
                   order_by=feed_table.c.title.asc()))
        return query.fetchall()



