Abraxas
=======

Abraxas is a very simple Feed Aggregator intended to
showcase the SiLCC tagging api.
One or more Feeds is aggregated, item titles are passed
into the SiLCC tagging api to extract tags. Items are then
displayed on a simple page with tags made clickable 
and cross referenced.


Installation and Setup
======================

Install ``abraxas`` using easy_install::

    easy_install abraxas

Make a config file as follows::

    paster make-config abraxas config.ini

Tweak the config file as appropriate and then setup the application::

    paster setup-app config.ini

Then you are ready to go.


To generate the database schema follow these steps:

1) First install sqlalchemy-migrate (if its not installed in your environment already):

$ easy_install sqlalchemy-migrate

2) For new installations create the db_repository, if you already have
the db_repository directory then skip this step.
 
$ migrate create db_repository "Abraxas DB Version Control"


3) Now create a custome manage.py script unless you want to use the one
from the main Abraxas repo.

$ migrate manage manage.py --repository=db_repository --url=mysql://abraxas:abraxas@localhost:3306/abraxas

4) now place your database under version control with:

$ python db_repository/manage.py version_control  mysql://abraxas:abraxas@localhost:3306/abraxas

or using the above manage.py:

$ python manage.py version_control

This will create the migrate_version table in your database and set the
initial version to 0.

After that you may run any schema upgrade scripts including the
first one which will create the necessary tables.

5) Now run a db update to generate the initial schema:

$ python manage.py update
