.. _tests:

Tests
*****

`Continuous integration test results <https://travis-ci.org/richardcornish/django-itunespodcast>`_ are available online.

However, you can also test the source code. Note that because the app stores media files, you will have to change to the directory above the source code directory before testing, typically ``site-packages`` after installing with pip.

.. code-block:: bash

   $ workon myvenv
   $ cdsitepackages
   $ django-admin test podcast.tests --settings="podcast.tests.settings"
   
   Creating test database for alias 'default'...
   ..........
   ----------------------------------------------------------------------
   Ran 1 test in 0.119s
   
   OK
   Destroying test database for alias 'default'...

A bundled settings file allows you to test the code without even creating a Django project.
