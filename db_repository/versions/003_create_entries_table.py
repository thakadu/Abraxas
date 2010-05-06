import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

"""
+---------------+--------------+------+-----+-------------------+----------------+
| Field         | Type         | Null | Key | Default           | Extra          |
+---------------+--------------+------+-----+-------------------+----------------+
| id            | bigint(20)   | NO   | PRI | NULL              | auto_increment | 
| feed_id       | mediumint(9) | NO   |     | NULL              |                | 
| title         | varchar(512) | NO   | MUL | NULL              |                | 
| url           | varchar(256) | YES  |     | NULL              |                | 
| created       | timestamp    | NO   |     | CURRENT_TIMESTAMP |                | 
| pubtime       | datetime     | YES  | MUL | NULL              |                | 
| summary       | mediumtext   | YES  |     | NULL              |                | 
| short_summary | mediumtext   | YES  |     | NULL              |                | 
| leader_id     | mediumint(9) | YES  |     | NULL              |                | 
+---------------+--------------+------+-----+-------------------+----------------+
"""
# New tables
entries_table = Table('entries', metadata,
    Column('id', mysql.MSInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('feed_id', VARCHAR(128), nullable=False),
    Column('title', VARCHAR(512), nullable=False),                   
    Column('url', VARCHAR(256), nullable=False),
    Column('pubtime', DATETIME),                 
    Column('summary', mysql.MSMediumText),
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 2 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    

def upgrade():
    entries_table.create()

def downgrade():
    entries_table.drop()

