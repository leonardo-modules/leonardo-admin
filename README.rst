
=============================
Django Admin for Leonardo CMS
=============================

Django Admin bundled as pluggable module for Leonardo CMS.

Everything in Leonardo is pluggable.

.. contents::
    :local:

Disable admin
-------------

.. code-block:: bash

    pip uninstall leonardo-admin

Installation
------------

.. code-block:: bash

    pip install leonardo-admin

.. code-block:: bash

    pip install leonardo-admin

or as leonardo bundle

.. code-block:: bash

    pip install django-leoanrdo[admin]

Add ``leonardo_admin`` to APPS list, in the ``local_settings.py``::

    APPS = [
        ...
        'leonardo_admin'
        ...
    ]

Configuration
-------------

One improtant option is there::

    ADMIN_URL = "admin/"

Works well with leonardo-admin-honeypot.

Read More
---------

* https://github.com/django-leonardo/django-leonardo
* http://leonardo.robotice.org
