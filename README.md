# sabracta
sabracta postgis and geodjango proof-of-concept project. this uses python
whereever possible, including database queries (plpythonu).

**note**: for documentation purposes only. not to be used in production.

**note**: this repository includes passwords and secrets by intention. don't use
it in production.


contents
--------

 * `sabracta/` - the django core module.
 * `aptroomat/` - the geodjango app module.
 * `aptroomat/data/` - custom geodatasets.


dependencies
------------

the following setup was used for this project:

 * linux       3.18.6  (archlinux)
 * python      3.4.3
 * python2     2.7.9   (optional for plpython2u)
 * postgresql  9.4.1
 * phppgadmin  5.1.0   (optional for database administration)
 * pgadmin iii 1.20.0  (optional for database administration)
 * postgis     2.1.5
 * django      1.7.4
 * psycopg2    2.6.0
 * gdal        1.11.2
 * geos        3.4.2
 * proj        4.8.0


setup
-----

adjust `sabracta/settings.py` for your needs. using a postgis backend is
strongly recommended, if not mandatory for this implementation.

make sure all postgis extensions and full python language support are installed
in the used postgresql database. refer to the postgis documentation, used in
this project:

    CREATE EXTENSION postgis;
    CREATE EXTENSION postgis_topology;
    CREATE EXTENSION postgis_tiger_geocoder;
    CREATE EXTENSION fuzzystrmatch;
    CREATE EXTENSION plpythonu;

write aptroomat database model:

    $ python manage.py makemigrations
    $ python manage.py sqlmigrate aptroomat 0001
    $ python manage.py migrate

write world borders to database:

    $ python manage.py shell
    >>> from aptroomat import load
    >>> load.run()

create a superuser by your own needs, refer to the django documentation.

run development server and verify admin settings:

    $ python manage.py runserver --ipv6

navigate to localhost admin panel:

 * [[::1]:8000/admin](http://[::1]:8000/admin/)

explore the geodjango app:

 * [[::1]:8000/aptroomat](http://[::1]:8000/aptroomat/)
 * [[::1]:8000/aptroomat/explore](http://[::1]:8000/aptroomat/explore/)
 * [[::1]:8000/aptroomat/api](http://[::1]:8000/aptroomat/api/)


resources
---------

 * [wiki.archlinux.org/postgresql](https://wiki.archlinux.org/index.php/PostgreSQL)
 * [wiki.archlinux.org/phppgadmin](https://wiki.archlinux.org/index.php/PhpPgAdmin)
 * [wiki.archlinux.org/postgis](https://wiki.archlinux.org/index.php/PostGIS)
 * [docs.djangoproject.com/intro/install/](https://docs.djangoproject.com/en/dev/intro/install/)
 * [docs.djangoproject.com/ref/contrib/gis/tutorial/](https://docs.djangoproject.com/en/dev/ref/contrib/gis/tutorial/)
 * [thematicmapping.org/world_borders](http://thematicmapping.org/downloads/world_borders.php)


credits
-------

copyright (c) 2015 alexander schoedon <schoedon@uni-potsdam.de>

all custom code licensed under gplv3.

this repository includes geographic datasets from
[thematicmapping.org](http://thematicmapping.org/downloads/world_borders.php)
which is licensed under
[creative commons attribution-share alike license 3.0](http://creativecommons.org/licenses/by-sa/3.0/).

if you ever author geographic datasets, don't use creative commons as they don't
cover data, datasets and databases.
[read more why](http://opendatacommons.org/faq/licenses/#Why_Not_Use_a_Creative_Commons_or_FreeOpen_Source_Software_License_for_Databases).
use an [open data commons license](http://opendatacommons.org/licenses/) type.
