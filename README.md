# sabracta
sabracta postgis and geodjango proof-of-concept project.

note: for documentation purposes only. not to be used in production.

note: this repository includes passwords and secrets by intention. don't use it
in production.


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

write database model:

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


resources
---------

 * [wiki.archlinux.org/postgresql](https://wiki.archlinux.org/index.php/postgresql)
 * [wiki.archlinux.org/phppgadmin](https://wiki.archlinux.org/index.php/phppgadmin)
 * [wiki.archlinux.org/postgis](https://wiki.archlinux.org/index.php/postgis)
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
