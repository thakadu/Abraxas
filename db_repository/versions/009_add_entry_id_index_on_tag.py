import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# Existing tables
tag_table = Table('tag', metadata,
    Column('id', mysql.MSBigInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('entry_id', mysql.MSBigInteger(unsigned=True), nullable=False),
    Column('keyword', VARCHAR(64), server_default="", nullable=False),                   
    # The following column is the lowercased version of the tag              
    Column('lower', VARCHAR(64), server_default="", nullable=False),              
    Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    

def upgrade():
    sql = "CREATE INDEX ix_entry_id ON tag (entry_id);"
    migrate_engine.execute(sql);


def downgrade():
    sql = "DROP INDEX ix_entry_id ON tag;"
    migrate_engine.execute(sql);
