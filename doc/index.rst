.. pyomo_simplemodel documentation master file, created by
   sphinx-quickstart on Mon Dec 12 16:08:36 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==============================================
Getting Started with pyomo_simplemodel
==============================================

The **pyomo_simplemodel** package is software for modeling
and solving optimization problems. This package is derived from
`Pyomo <http://www.pyomo.org>`_, and it defines the class **SimpleModel**
that illustrates how Pyomo can be used in a simple, less object-oriented
manner. Specifically, this class mimics the modeling style supported
by `PuLP <https://github.com/coin-or/pulp>`_:

============ ===== ============
Feature      PuLP  SimpleModel
============ ===== ============
LP/MILP       YES          YES
NLP/MINLP      NO          YES
Column-wise   YES           NO
============ ===== ============

.. sidebar:: SimpleModel vs Pyomo

    SimpleModel is not meant to serve as a replacement for Pyomo. While SimpleModel only represents problems with a simple, unstructured representation, Pyomo's modeling components support structured, hierarchical models that are suitable for complex applications.

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

Acknowledgements
----------------
This software was supported in part by Sandia National Laboratories.
Sandia National Laboratories is a multi-program laboratory
managed and operated by Sandia Corporation, a wholly owned subsidiary
of Lockheed Martin Corporation, for the U.S. Department of Energy's
National Nuclear Security Administration under contract DE-AC04-94AL85000.

