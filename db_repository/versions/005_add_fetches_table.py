import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

"""
+---------+--------------+------+-----+-------------------+----------------+
| Field   | Type         | Null | Key | Default           | Extra          |
+---------+--------------+------+-----+-------------------+----------------+
| id      | mediumint(9) | NO   | PRI | NULL              | auto_increment | 
| feed_id | mediumint(9) | NO   | MUL | NULL              |                | 
| created | timestamp    | NO   |     | CURRENT_TIMESTAMP |                | 
| result  | varchar(128) | YES  |     | NULL              |                | 
+---------+--------------+------+-----+-------------------+----------------+
"""

# New tables
fetches_table = Table('fetches', metadata,
    Column('id', mysql.MSBigInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('feed_id', mysql.MSBigInteger(unsigned=True), nullable=False),
    Column('result', VARCHAR(512), server_default="", nullable=False),                   
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 6 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    

def upgrade():
    fetches_table.create()

def downgrade():
    fetches_table.drop()

