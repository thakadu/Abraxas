import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# New tables
entry_table = Table('entry', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('feed_id', VARCHAR(128), nullable=False),
    Column('title', VARCHAR(512), nullable=False),                   
    Column('url', VARCHAR(256), nullable=False, unique=True, index=True),
    Column('pubtime', DATETIME),                 
    Column('tags', VARCHAR(512), nullable=True),                   
    Column('summary', mysql.MSMediumText),
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 4 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    

def upgrade():
    entry_table.create()

def downgrade():
    entry_table.drop()

