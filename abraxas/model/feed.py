"""Represents a Feed (RSS/Atom or other)"""                                                                                                       
import logging
import datetime
import math

from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from abraxas.model import meta

log = logging.getLogger(__name__)

class Feed(object):
    pass

