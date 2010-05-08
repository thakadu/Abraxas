"""Represents a single item within a Feed (RSS/Atom or other)"""
import logging
import datetime
import math

from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from abraxas.model import meta
from abraxas.model.tag import Tag

from abraxas.model.meta import Session

log = logging.getLogger(__name__)

class Entry(object):

    def tag(self, tags):
        """Given a single tag or a list of tags adds them to the entry"""
        if isinstance(tags, str):
            tags = [tags]
        for tag in tags:
            tag_ = Tag()
            tag_.keyword = tag
            tag_.lower = tag.lower()
            tag_.entry_id = self.id
            Session.add(tag_)
        Session.commit()



