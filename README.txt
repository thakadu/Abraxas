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

1) Create a Python Virtual environment from which to run Abraxas

Note that this step is optional but higly recommended.

run virtualenv name_of_environment for example:
$ virtualenv abraxas_env
me@myserver:~/webapps$ virtualenv abraxas_env
New python executable in abraxas_env/bin/python
Installing setuptools............done.


    (If virtualenv is not installed then on Ubuntu the easiest way is
     to use easy_install to install it. If easy_install itself is not 
     installed then first:

     $ sudo apt-get install python-setuptools
     then:
     $ sudo easy_install virtualenv)

This will create a new virtual Python environment for you.
Now activate your new environment:

$ source abraxas_env/bin/activate

This should change your prompt into something similar to:

(abraxas_env)me@myserver:~/webapps$ 

Issuing a 'which python' command should confirm that the virtualenv is now
activated:

(abraxas_env)me@myserver:~/webapps$ which python
/home/me/webapps/abraxas_env/bin/python

2) Now checkout a copy of the Abraxas source code:

(abraxas_env)me@myserver:~/webapps$ git clone git://github.com/thakadu/Abraxas.git

3) Within the Abraxas directory (created as a result of step 2 above):


(abraxas_env)me@myserver:~/webapps$ cd Abraxas
(abraxas_env)me@myserver:~/webapps/abraxas$ python setup.py install

This will install all of the dependancies into the
Virtual Python enviroment created in step 1.

4) Create the database for Abraxas to use. If using MySQL:

5) Create the database. If using MySQL:

$ mysql -u root -p

Once in the mysql environment:

>>> create database abraxas default charset utf8;
>>> grant all on abraxas.* to abraxas@localhost identified by 'password';

Now exit the MySQL enviroment by hitting Ctrl-D

6) Set the SQLAlchemy url in the prod.ini and/or the development.ini files.

Fine the line that reads:
sqlalchemy.url = mysql://abraxas:abraxas@tom:3306/abraxas
and make sure it matches the database name, user name and password
you used in step 5.

7) Initialize the database:

We are going to use the supplied SQLAlchemy-migrate
scripts to generate the initial tables and indexes.
In order to do this, we first place the database
under version control:

$ python db_repository/manage.py version_control mysql://abraxas:password@localhost:3306/abraxas

Make sure to use the correct url for the database you created
in step 6.

This will create the migrate_version table in your database and set the
initial version to 0. 

Now create a custom manage.py script by running the following command:

$ migrate manage manage.py --repository=db_repository --url=mysql://abraxas:password@localhost:3306/abraxas

This will create a new manage.py file in the current directory.

Now 'upgrade' the database which will create all the initial tables
and indexes.

$ python manage.py upgrade

You should see output similar to this:
(abraxas_env)me@myserver:~/webapps/Abraxas$ python manage.py upgrade
0 -> 1... 
done
1 -> 2... 
done
...
...
7 -> 8... 
done



8) Load your initial feeds that you want to include in your
Abraxas deployment. There is a loader script in the scripts
directory called scripts/load_feeds.py
It loads Feeds from a .csv file. Inside the data directory
there are a couple of example .csv files. Create your
own file from these, there are three fields, from 
left to right these are:

a) Name of Feed
b) Web Url (not the url of the feed but rather the website itself)
c) Feed Url

The data directory contains a few small example .csv files with some.

The load_feeds.py script takes two parameters, the .ini file to 
use, which tells the script which database to load to and the
.csv file which is where it loads the feeds from. By now your
.ini file should already contain the correct database url you
set in step 6.

$ python scripts/load_feeds.py --ini=development.ini --filename=data/african_feeds.csv

You can confirm that the feeds loaded by starting the mysql client
and enterting the following query:

$ mysql -u abraxas -p abraxas
>>> select * from feed;

If all went well you should see a list of the feeds from your .csv file.

9) Fetch the items from your feeds.
As with the load_feeds script the fetch_feeds script also
takes the .ini filename as a parameter. In all cases
the default value is development.ini so you might want
to make sure you have the correct database set in your
development.ini file. 

$ python scripts/fetch_feeds.py --ini=development.ini 

This should download feeds from the feed urls supplied 
for each feed and store each entry in the database.

10) Tags the downloaded entries.

Run the script scripts/tag_entries.py

Again this takes the .ini file as a parameter:

$ python scripts/tag_entries.py --ini=development.ini


11) Now start your server:

$ paster serve development.ini --daemon



 





 

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
