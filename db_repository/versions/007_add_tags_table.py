import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)


# New tables
tag_table = Table('tag', metadata,
    Column('id', mysql.MSBigInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('entry_id', mysql.MSBigInteger(unsigned=True), nullable=False),
    Column('keyword', VARCHAR(64), server_default="", nullable=False),                   
    # The following column is the lowercased version of the tag              
    Column('lower', VARCHAR(64), server_default="", nullable=False)              
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 8 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    
                                                                                                                    

def upgrade():
    tag_table.create()

def downgrade():
    tag_table.drop()

