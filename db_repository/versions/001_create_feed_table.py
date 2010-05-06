import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# New tables
feed_table = Table('feed', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('title', VARCHAR(128), nullable=False),
    Column('url', VARCHAR(256), nullable=False),
    Column('active', mysql.MSTinyInteger(unsigned=True)),
    Column('last_fetched_at', DATETIME),                 
    Column('items', mysql.MSInteger),
    Column('author', VARCHAR(50)),                 
    Column('weburl', VARCHAR(256)),
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 2 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    

def upgrade():
    feed_table.create()

def downgrade():
    feed_table.drop()

