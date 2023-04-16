.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

.. image:: https://github.com/garnik-arut/ga_scaffold/actions/workflows/ci.yml/badge.svg
    :alt: CI workflow
    :target: https://github.com/garnik-arut/ga_scaffold/actions/workflows/ci.yml/badge.svg

===========
ga_scaffold
===========


    Scaffold python project based on PyScaffold 4.4

| Good starting point for new projects: base for logging, tests, linting, basic CI/CD with Github Actions etc is already there.

Description
=============================

| Demo contains Fast inverse square root algorithm based on interpreting 32-bit float as integer (yes, it works in python too, yes, its the same algorithm from Quake III Arena). https://en.wikipedia.org/wiki/Fast_inverse_square_root


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd ga_scaffold
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.
