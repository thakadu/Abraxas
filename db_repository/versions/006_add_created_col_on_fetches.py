import datetime

from sqlalchemy import *
from migrate import *

from sqlalchemy.databases import mysql

metadata = MetaData(migrate_engine)

# Existing tables
fetches_table = Table('fetches', metadata,
    Column('id', mysql.MSBigInteger(unsigned=True), autoincrement=True, primary_key=True, nullable=False),
    Column('feed_id', mysql.MSBigInteger(unsigned=True), nullable=False),
    Column('result', VARCHAR(512), server_default="", nullable=False),                   
    # Note: SQLAlchemy doesnt seem to have a way to create a current_timestamp col
    # So see upgrade script 6 where we do it with raw sql.
    #Column('created', TIMESTAMP, default='current_timestamp')
)                                                                                                                    

def upgrade():
    sql = "ALTER TABLE fetches ADD COLUMN created TIMESTAMP DEFAULT CURRENT_TIMESTAMP;"
    migrate_engine.execute(sql);


def downgrade():
    sql = "ALTER TABLE fetches DROP created;"
    migrate_engine.execute(sql);
