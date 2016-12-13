===========================
Modeling Nonlinear Problems
===========================

----------------
Soda Can Example
----------------

Finding the optimal dimensions of a soda can is a simple nonlinear
optimization problem.  We consider an idealized soda can that is
represented as a cylinder with radius `r` and height `h`.  The
problem is to find the radius and height that minimizes the surface
area of the cylinder while keeping a fixed volume.  Here, the surface
area of the cylinder approximates the amount of aluminum needed for
a soda can, so this problem can be used to predict the miminum amount of aluminum
needed to hold a given volume.

The surface area of a cylinder is

.. math::

    2 \pi r (r+h)

A standard soda can is 12 oz or 355 ml.  Thus, we have the constraint

.. math::

    \pi r^2 h = 355

Thus, we have the following optimization representation for this problem:

.. math::
   :nowrap:

    \begin{eqnarray}
        \min & 2 \pi r (r+h)\\
        \textrm{s.t. } & \pi r^2 h = 355\\
        & r \geq 0\\
        & h \geq 0
    \end{eqnarray}

This is a nonlinear problem, so it cannot be formulated with PuLP.
The following sections illustrate how this optimization problem can
be formulated and solved with SimpleModel and Pyomo.

-----------------------
SimpleModel Formulation
-----------------------

The following script executes the following steps to create and solve the sodacan problem:

1. Import ``pyomo.contrib.simplemodel``
2. Construct a ``SimpleModel`` class
3. Declares variables, the objective and the constraint
4. Perform optimization
5. Summarize the optimal solution


.. literalinclude:: ../examples/sodacan.py
   :language: python
   :linenos:

In this example, the model object ``m`` is used to manage the problem
definition.  Decision variables are declared with the ``var()``
method, objectives and constraints are added with the ``+=`` operator,
and the ``solve()`` method is used to perform optimization.  After
optimization, the solution is stored in the variable objects, and
the objective value can be accessed with using the ``objective()``
method.


-----------------
Pyomo Formulation
-----------------

The following script executes the same steps as above to create and solve the soda cana problem using Pyomo:

.. literalinclude:: ../examples/sodacan-pyomo.py

This script is similar to the SimpleModel script, but
Pyomo models are created with an object-oriented design.  Thus,
elements of the optimization problem are declared with variable,
objective and constraint components, which are Pyomo objects.  As
a consequence, the objective and constraint expressions reference
variable components within the model (e.g. ``m.x``) instead of 
variable objects directly (e.g. ``x``).

