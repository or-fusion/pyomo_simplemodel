================================
Flat vs Block Model Formulations
================================

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

    \begin{array}{lll}
        \min_{x,y_1,\ldots,y_k} & p_k y_k & \\
        \textrm{s.t.} & y_k \geq (c-b)x + b d_k & k = 1,\ldots,K\\
                      & y_k \geq (c+h)x - h d_k & k = 1,\ldots,K\\
                      & x \geq 0
    \end{array}

This is a linear integer problem, so it can be formulated with
SimpleModel, PuLP and Pyomo.  Below, we show formulations for
SimpleModel and Pyomo.  In particular, the Pyomo formulation
illustrates the use of the **Block** component to structure the
model representation in a modular manner.

-----------------------
SimpleModel Formulation
-----------------------

The following script creates and solves an integer program for the newsvendor problem using SimpleModel:

.. literalinclude:: ../examples/newsvendor.py
   :language: python
   :linenos:

There are two key things to note about this model.  First, it is
`flat`: the model simply consists of a list of constraints.  Second,
the ``y`` variable is indexed to represent the total cost for the
different scenarios.


-----------------
Pyomo Formulation
-----------------

The following script creates and solves an integer program for the newsvendor problem using SimpleModel:

.. literalinclude:: ../examples/newsvendor-pyomo.py

This script uses the ``Block`` component to create a hierarchical
model representation.  A block is added for each index :math:`k =
1,\ldots,K`, and each block contains a variable ``y``, and the
corresponding constraints that define the value of ``y``.

Note that the ``Block`` component is indexed in this formulation
while the ``y`` variable is indexed in the SimpleModel formulation.
Block components allow Pyomo to support a modular modeling framework,
where the data, variables and constraints in the block can be
represented simply, and where the block itself is indexed.  There
are several advantages of this approach:

* This model structure is explicit, and it can be exploited by decomposition-based optimization solvers (e.g. the progressive hedging solver in Pyomo).

* Extending and refining block models is simpler.  For example, if a multi-dimensional index was needed for this model, then ``y`` would need to be modified to reflect that.  In complex application with many variables and other components, the block structure helps coordinate and simplify this type of change.



.. [ShaPhi] A. Shapiro and A. Philpott.  *A Tutorial on Stochastic Programming*.  2007. `(weblink) <http://www2.isye.gatech.edu/people/faculty/Alex_Shapiro/TutorialSP.pdf>`_

