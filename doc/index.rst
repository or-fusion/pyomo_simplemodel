.. pyomocontrib_simplemodel documentation master file, created by
   sphinx-quickstart on Mon Dec 12 16:08:36 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==============================================
Getting Started with pyomo.contrib.simplemodel
==============================================

The **pyomo.contrib.simplemodel** package is software for modeling
and solving optimization problems. This package is derived from
`Pyomo <http://www.pyomo.org>`_, and it defines the class **SimpleModel**
that illustrates how Pyomo can be used in a simple, less object-oriented
manner. Specifically, this class mimics the modeling style supported
by `PuLP <https://github.com/coin-or/pulp>`_:

.. sidebar:: SimpleModel vs Pyomo

    SimpleModel is not meant to serve as a replacement for Pyomo, which supports a much richer set of modeling components than simple objectives and constraints. In particular, Pyomo's **Block** component supports the expression of hierarchical models with nested structure, while SimpleModel only supports a simple, non-hierarchical optimization problems.


============ ===== ============
Feature      PuLP  SimpleModel
============ ===== ============
LP/MILP       YES          YES
NLP/MINLP      NO          YES
Column-wise   YES           NO
============ ===== ============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   knapsack
   sodacan
   newsvendor
   gettingstarted


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
