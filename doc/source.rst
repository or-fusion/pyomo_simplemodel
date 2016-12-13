====================
Source Documentation
====================

-----------
SimpleModel
-----------

.. py:currentmodule:: pyomocontrib_simplemodel

.. autoclass:: SimpleModel
    :members:

-------------------
Declaring Variables
-------------------

By default, model variables are assumed to be unbounded real values.
In practice, it is often necessary to specify a more limited set
of values.  For example, suppose a variable ``x`` assumes integer
values in the range 1 to 7.   Then the following declaration would be used::

    x = m.var('x', bounds=(1,7), within=Integers)

The ``bounds`` keyword specifies the lower and upper bounds for the
variable.  The ``within`` keyword indicates the feasible domain for
the variable: the set of feasible values that the variable may
assume.  A variety of objects are defined by Pyomo to specify
feasible domains, including:

Binary
    The set of boolean values

Boolean
    The set of boolean values

Integers
    The set of integer values

NegativeIntegers
    The set of negative integer values

NegativeReals
    The set of negative real values

NonNegativeIntegers
    The set of non-negative integer values

NonNegativeReals
    The set of non-negative real values

NonPositiveIntegers
    The set of non-positive integer values

NonPositiveReals
    The set of non-positive real values

PercentFraction
    The set of real values in the interval [0,1]

PositiveIntegers
    The set of positive integer values

PositiveReals
    The set of positive real values

Reals
    The set of real values

UnitInterval
    The set of real values in the interval [0,1]

