import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# Existing tables
entry_table = Table('entry', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('feed_id', VARCHAR(128), nullable=False),
    Column('title', VARCHAR(512), nullable=False),                   
    Column('url', VARCHAR(256), nullable=False),
    Column('pubtime', DATETIME),                 
    Column('summary', mysql.MSMediumText),
    Column('tags', VARCHAR(512))                  
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 2 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    

def upgrade():
    sql = "ALTER TABLE entry ADD COLUMN created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"
    migrate_engine.execute(sql);


def downgrade():
    sql = "ALTER TABLE entry DROP created;"
    migrate_engine.execute(sql);
    
