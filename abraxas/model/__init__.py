"""The application's model objects"""
from abraxas.model.meta import Session, Base

import sqlalchemy as sa
from sqlalchemy import orm

from abraxas.model import meta
from abraxas.model.fetch import Fetch
from abraxas.model.feed import Feed


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

    fetch_table = sa.Table('fetch', meta.metadata, autoload=True, autoload_with=engine)
    Fetch.table = fetch_table
    orm.mapper(Fetch, Fetch.table)

    feed_table = sa.Table('feed', meta.metadata, autoload=True, autoload_with=engine)
    Feed.table = feed_table
    orm.mapper(Feed, Feed.table)
