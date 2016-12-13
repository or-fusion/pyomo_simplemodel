================
Knapsack Example
================

The `Knapsack Problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_
considers the problem of selecting a set of items whose weight is
not greater than a specified limit while maximizing the total value
of the selected items.  This problem is inspired by the challenge
of filling a knapsack (or rucksack) with the most valuable items
that can be carried.

A common version of this problem is the **0-1 knapsack problem**,
where each item is distinct and can be selected once.  Suppose there
are :math:`n` items with positive values :math:`v_1, \ldots, v_n`
and weights :math:`w_1, \ldots, w_n`.  Let :math:`x_1, \ldots, x_n`
be decision variables that can take values 0 or 1.  Let `W` be the
weight capacity of the knapsack.

The following optimization formulation represents this problem as
an integer program:

.. math::
   :nowrap:

   \begin{eqnarray}
      \max & \sum _{i=1}^{n} v_{i} x_{i} \\
      \textrm{s.t.} & \sum _{i=1}^{n} w_{i} x_{i}\leq W \\
      \textrm{s.t.} & x_{i}\in \{0,1\} 
   \end{eqnarray}

The following sections illustrate how this optimization problem can be
formulated with (1) SimpleModel, (2) PuLP, and (3) Pyomo.

-----------------------
SimpleModel Formulation
-----------------------

The following script executes the following steps to create and solve a knapsack problem:

1. Import ``pyomo.contrib.simplemodel``
2. Construct a ``SimpleModel`` class
3. Declares variables, the objective and the constraint
4. Perform optimization
5. Summarize the optimal solution


.. literalinclude:: ../examples/knapsack.py
   :language: python
   :linenos:

In this example, the model object ``m`` is used to manage the problem
definition.  Decision variables are declared with the ``var()``
method, objectives and constraints are added with the ``+=`` operator,
and the ``solve()`` method is used to perform optimization.  After
optimization, the solution is stored in the variable objects, and
the objective value can be accessed with using the ``objective()``
method.


----------------
PuLP Formulation
----------------

The following script executes the same steps as above to create and solve a knapsack problem using PuLP:

.. literalinclude:: ../examples/knapsack-pulp.py

This script is *very* similar to the SimpleModel script.  Both
scripts declare a problem class that is used to declare variables,
the objective and constraint, and to perform optimization.


-----------------
Pyomo Formulation
-----------------

The following script executes the same steps as above to create and solve a knapsack problem using Pyomo:

.. literalinclude:: ../examples/knapsack-pyomo.py

This script is similar to the SimpleModel and PuLP scripts, but
Pyomo models are created with an object-oriented design.  Thus,
elements of the optimization problem are declared with variable,
objective and constraint components, which are Pyomo objects.  As
a consequence, the objective and constraint expressions reference
variable components within the model (e.g. ``m.x``) instead of 
variable objects directly (e.g. ``x``).  Thus, modeling 
in Pyomo is more verbose (especially when long model names are
used).

