Development
===========

Our development process is focused on high quality and development comfort.
We use tools that are proven to be the best in class.

Local development is much easier and much faster.
You can choose it if you don't have too many infrastructure dependencies.
That's a default option for the new projects.

Dependencies
------------

We use ``poetry`` to manage dependencies.
So, please do not use ``virtualenv`` or ``pip`` directly.
Before going any further, please,
take a moment to read the `official documentation <https://poetry.eustace.io/>`_
about ``poetry`` to know some basics.

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Please, note that ``poetry`` will automatically create a ``virtualenv`` for
this project. It will use your current ``python`` version.
To install all existing dependencies run:

.. code:: bash

  poetry install

To install dependencies for production use, you will need to run:

.. code:: bash

  poetry install --no-dev

And to activate ``virtualenv`` created by ``poetry`` run:

.. code:: bash

  poetry shell

Adding new dependencies
~~~~~~~~~~~~~~~~~~~~~~~

To add a new dependency you can run:

- ``poetry add django`` to install ``django`` as a production dependency
- ``poetry add --dev pytest`` to install ``pytest``
  as a development dependency

Updating poetry version
~~~~~~~~~~~~~~~~~~~~~~~

Package managers should also be pinned very strictly.
We had a lot of problems in production
because we were not pinning package manager versions.

This can result in broken ``lock`` files, inconsistent installation process,
bizarre bugs, and missing packages. You do not want to experience that!

How can we have the same ``poetry`` version for all users in a project?
That's where ``[build-system]`` tag shines. It specifies the exact version of
your ``poetry`` installation that must be used for the project.
Version mismatch will fail your build.

When you want to update ``poetry``, you have to bump it in `pyproject.toml`.

Local development
-----------------

When cloning a project for the first time you may
need to configure it properly,
see :ref:`django` section for more information.

**Note**, that you will need to activate ``virtualenv`` created
by ``poetry`` before running any of these commands.
**Note**, that you only need to run these commands once per project.

Local database
~~~~~~~~~~~~~~

When using local development environment, you will need an SQLite database.
To create the database and run migrations:

.. code:: bash

  python manage.py migrate

Running project
~~~~~~~~~~~~~~~

If you have reached this point, you should be able to run the project.

.. code:: bash

  python manage.py runserver
