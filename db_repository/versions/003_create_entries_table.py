import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# New tables
entries_table = Table('entries', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('feed_id', VARCHAR(128), nullable=False),
    Column('title', VARCHAR(512), nullable=False),                   
    Column('url', VARCHAR(256), nullable=False),
    Column('pubtime', DATETIME),                 
    Column('tags', VARCHAR(512), server_default="", nullable=False),                   
    Column('summary', mysql.MSMediumText),
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 4 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    

def upgrade():
    entries_table.create()

def downgrade():
    entries_table.drop()

