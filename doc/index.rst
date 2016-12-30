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

    SimpleModel is not meant to serve as a replacement for Pyomo, which supports a much richer set of modeling components than simple objectives and constraints. In particular, Pyomo's **Block** component supports the expression of structured and hierarchical models, while SimpleModel only supports simple, unstructured optimization problems.


============ ===== ============
Feature      PuLP  SimpleModel
============ ===== ============
LP/MILP       YES          YES
NLP/MINLP      NO          YES
Column-wise   YES           NO
============ ===== ============

The following sections illustrate similarities and differences
between SimpleModel, PuLP and regular Pyomo models.  First, the
knapsack problem is used to illustrate that these packages can be
used in a similar manner on simple applications.  Next, the soda
can problem illustrates that SimpleModel can represent nonlinear
problems that cannot be modeled with PuLP.  Finally, the newvendor
problem is used to illustrate three different modeling representations:
unstructured models, structured models and hierarchical models.
SimpleModel and PuLP have unstructured models, while Pyomo supports
all three modeling representations.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   knapsack
   sodacan
   newsvendor
   gettingstarted
   source


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
