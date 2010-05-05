import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)
"""
mysql> desc feeds;
+-----------------+--------------+------+-----+------------------------------------------+----------------+
| Field           | Type         | Null | Key | Default                                  | Extra          |
+-----------------+--------------+------+-----+------------------------------------------+----------------+
| id              | mediumint(9) | NO   | PRI | NULL                                     | auto_increment | 
| title           | varchar(128) | NO   | MUL | NULL                                     |                | 
| created         | timestamp    | NO   |     | CURRENT_TIMESTAMP                        |                | 
| url             | varchar(256) | NO   |     | NULL                                     |                | 
| active          | tinyint(4)   | NO   |     | 1                                        |                | 
| country         | varchar(50)  | YES  |     | NULL                                     |                | 
| last_fetched_at | datetime     | YES  |     | NULL                                     |                | 
| items           | mediumint(9) | YES  |     | NULL                                     |                | 
| author          | varchar(50)  | YES  |     | NULL                                     |                | 
| category        | varchar(20)  | YES  |     | NULL                                     |                | 
| weburl          | varchar(128) | YES  |     | NULL                                     |                | 
| icon            | varchar(50)  | YES  |     | http://static.memamatic.com/rss_icon.png |                | 
| logo            | varchar(50)  | YES  |     | NULL                                     |                | 
| family          | varchar(25)  | YES  |     | NULL                                     |                | 
| family_url      | varchar(128) | YES  |     | NULL                                     |                | 
| family_icon     | varchar(50)  | YES  |     | http://static.memamatic.com/rss_icon.png |                | 
+-----------------+--------------+------+-----+------------------------------------------+----------------+
"""

# New tables
feeds_table = Table('feeds', metadata,
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
    feeds_table.create()

def downgrade():
    feeds_table.drop()

