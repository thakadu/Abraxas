"""Represents a fetch/download of an RSS feed"""                                                                                                       
import logging
import datetime
import math

from sqlalchemy import and_, desc, func, or_, select, types
from sqlalchemy.sql import text

from abraxas.model import meta

log = logging.getLogger(__name__)

class Fetch(object):
    pass

