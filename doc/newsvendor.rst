===============================================
Unstructured, Structured and Block Formulations
===============================================

This section illustrates differences between SimpleModel, PuLP and
regular Pyomo models on a problem with more complex structure.  The
**newsvendor problem** is used to illustrate three different modeling
representations that are supported by these modeling tools:

unstructured
  The model stores a *list* of objectives and constraints expressions.

structured
  The model stores named objectives and constraints. Each of these named
  components *map* index values to expressions.

hierarchical
  The model stores named *block* components, each of which stores
  named components, including variables, objectives and constraints.

-------------------
Newsvendor Example
-------------------

The `Newsvendor Problem <https://en.wikipedia.org/wiki/Newsvendor_model>`_ 
considers the problem of determining optimal inventory levels.  
Given fixed prices and an uncertain demand, the problem is to determine
inventory levels that maximize the expected profit for the newsvendor.

The following formulation is adapted from Shapiro and Philpott [ShaPhi]_.  A
company has decided to order a quantity `x` of a product to satisfy
demand `d`.  The per-unit cost of ordering is `c`, and if demand `d` is
greater than `x`, `d>x`, then the back-order penalty is `b` per unit.  If
demand is less than production, `d<x`, then a holding cost `h` is
incurred for unused product.

The objective is to minimize the `total cost`: :math:`\max\left\{
(c-b)x+bd, (c+h)x-hd\right\}`.  For example, suppose we have
:math:`c=1`, :math:`b=1.5`, :math:`h=0.1`, and :math:`d=50`.
Then the total following figure illustrates the total cost:

.. image: figs/newsvendor_totalcost.png

In general, the ordering decision is made before a realization of
the demand is known.  The deterministic formulation corresponds to
a single scenario taken with probability one:

.. math::
   :nowrap:

    \begin{array}{ll}
        \min_{x,y} & y\\
        \textrm{s.t.} & y \geq (c-b)x + b d\\
                      & y \geq (c+h)x - h d\\
                      & x \geq 0
    \end{array}

Now suppose we model the distribution of possible demands with
scenarios :math:`d_1, \ldots, d_K` each with equal probability (:math:`p_k = 0.2`).
Then the following formulation minimizes the expected value of the
total cost over these scenarios:

.. math::
   :nowrap:

    \begin{array}{llll}
        \min_{x,y_1,\ldots,y_K} & p_k y_k & & \\
        \textrm{s.t.} & y_k \geq (c-b)x + b d_k & k = 1,\ldots,K & \textit{# demand is greater}\\
                      & y_k \geq (c+h)x - h d_k & k = 1,\ldots,K & \textit{# demand is less}\\
                      & x \geq 0
    \end{array}

This is a linear problem, so it can be formulated with
SimpleModel, PuLP and Pyomo.

Since the two constraints are indexed from :math:`1, \ldots, K`, we can
group them together into a single block, which itself is indexed
from :math:`1, \ldots, K`.

.. math::
   :nowrap:

    \begin{array}{lll}
        \min_{x,y_1,\ldots,y_K} & p_k y_k & \\
        \textrm{s.t.} & \left\{\begin{array}{l}
                        y_k \geq (c-b)x + b d_k\\
                        y_k \geq (c+h)x - h d_k\\
                        \end{array}\right\} & k = 1,\ldots,K\\
                      & x \geq 0
    \end{array}

Below, we show formulations for SimpleModel, PuLP, and Pyomo.  The
SimpleModel and PuLP models illustrate *unstructured* representations.
The first Pyomo formulation illustrates an *unstructured* representation,
where constraints are stored in a list.  The second Pyomo formulation
illustrates a *structured* representation, which corresponds to the
first formulation above.  The final Pyomo formulation illustrates
a *hierarchical* representation, using the **Block** component to
structure the model representation in a modular manner.

-----------------------
SimpleModel Formulation
-----------------------

The following script creates and solves a linear program for the newsvendor problem using SimpleModel:

.. literalinclude:: ../examples/newsvendor.py
   :language: python
   :linenos:

There are two key things to note about this model.  First, the model
simply consists of a list of constraints.  Second, the ``y`` variable
is indexed to represent the total cost for the different scenarios.

----------------
PuLP Formulation
----------------

The following script creates and solves a linear program for the newsvendor problem using PuLP:

.. literalinclude:: ../examples/newsvendor-pulp.py
   :language: python
   :linenos:

As with the SimpleModel formulation, the model consists of a list
of constraints, and the ``y`` variable is indexed.


------------------
Pyomo Formulations
------------------

The following script creates and solves a linear program for the
newsvendor problem using Pyomo:

.. literalinclude:: ../examples/newsvendor-pyomo1.py

This model uses the ``ConstraintList`` component to store a list of constraints, and the ``y`` variable
is indexed.  Thus, this model provides an *unstructured* representation that is similar to models generated with SimpleModel and PuLP.

The following script uses Pyomo to create and solve the newsvendor problem, using a *structured* representation:

.. literalinclude:: ../examples/newsvendor-pyomo2.py

The named constraint components ``greater`` and ``less`` define
two groups of constraints for the model, each of which has the same
mathematical form.  These named components provide a structured
representation for these constraints.

Finally, the following script uses Pyomo to create and solve this problem, using a *hierarchical* representation:

.. literalinclude:: ../examples/newsvendor-pyomo3.py

A block is added for each index :math:`k =
1,\ldots,K`. Each block contains a variable ``y``, and the
corresponding constraints that define the value of ``y``.

Note that the block component ``b`` is indexed in this formulation
while the ``y`` variable is indexed in the other formulations above.
Block components allow Pyomo to support a modular modeling framework
where data, variables and constraints can be
represented together for each index value.  There
are several advantages of this approach:

* This model structure is explicit, and it can be exploited by decomposition-based optimization solvers (e.g. the progressive hedging solver in Pyomo).

* Extending and refining models is simpler with blocks.  For example, if a multi-dimensional index was needed for this problem, then only the block ``b`` would need to be modified to reflect that.


----------
References
----------

.. [ShaPhi] A. Shapiro and A. Philpott.  *A Tutorial on Stochastic Programming*.  2007. `(weblink) <http://www2.isye.gatech.edu/people/faculty/Alex_Shapiro/TutorialSP.pdf>`_

