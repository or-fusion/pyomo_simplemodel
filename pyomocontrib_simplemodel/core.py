__all__ = ['SimpleModel']

import six
from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.var import Var
from pyomo.core.base.objective import ObjectiveList, maximize
from pyomo.core.base.suffix import Suffix
from pyomo.core.base.constraint import ConstraintList
from pyomo.opt.base.solvers import SolverFactory


class SimpleModel(object):
    """
    This class illustrates how Pyomo can be used in a simple, less
    object-oriented manner.  Specifically, this class mimics the
    modeling style supported by `PuLP <https://github.com/coin-or/pulp>`_.

    This class contains a Pyomo model, and it includes methods that
    support a simple API for declaring variables, adding objectives
    and constraints, and solving the model.  Optimization results
    are stored in the variable objects, which are returned to the
    user.

    For example, the following model minimizes the surface area of
    a soda can while constraining its volume::

        from pyomo.contrib.simplmodel import *
        from math import pi

        m = SimpleModel()

        r = m.var('r', bounds=(0,None))
        h = m.var('h', bounds=(0,None))

        m += 2*pi*r*(r + h)
        m += pi*h*r**2 == 355

    This model can be solved with the IPOPT solver::

        status = m.solve("ipopt")
        print("Status = %s" % status.solver.termination_condition)

    The optimum value and decision variables can be easily accesed::

        print("%s = %f" % (r, value(r)))
        print("%s = %f" % (h, value(h)))
        print("Objective = %f" % value(m.objective()))

    Notes
    -----
    This class illustrates the basic steps in formulating
    and solving an optimization problem, but it is not meant to
    serve as a replacement for Pyomo.  Pyomo models supports a much
    richer set of modeling components than simple objectives and
    constraints.  In particular, Pyomo's Block component supports
    the expression of hierarchical models with nested structure.
    This class only supports a simple, flat optimization problems.
    """

    def __init__(self, maximize=False):
        """
        Parameters
        __________
        maximize : Optional[bool]
            If True, then the objective sense is maximization.
        """
        import pyomo.environ
        self.model = ConcreteModel()
        self.model.o = ObjectiveList()
        self.model.c = ConstraintList()
        self._maximize = maximize

    def suffix(self, name):
        """
        Declare a suffix with the specified name.  Suffixes are values 
        returned by the solver, which are typically associated constraints.

        Parameters
        __________
        suffix : str
            The suffix that is returned from the solver.
        """
        setattr(self.model, name, Suffix(direction=Suffix.IMPORT))

    def var(self, *args, **kwds):
        """
        Declare a variable.

        Parameters
        ----------
        \*args 
            The first argument is a string for the variable name used by Pyomo.
            The remaining arguments are assumed to be index sets for the 
            variable.
        \**kwargs
            The keyword arguments are the same as the keyword arguments
            supported by the Pyomo Var component.

        Returns
        -------
        Variable object
            If the variable is not indexed, then the return type
            is a single Pyomo variable object.  If the variable is
            indexed, then the return type is a dictionary of Pyomo
            variable objects.
        """
        _args = args[1:]
        name = args[0]
        # If the variable name is "x", then the following is equivalent to:
        #  self.model.x = Var(*_args, **kwds)
        _v = Var(*_args, **kwds)
        setattr(self.model, name, _v)
        return _v

    def __iadd__(self, expr):
        """
        Add an objective or constraint to the model.

        Parameters
        ----------
        expr : Pyomo expression
            An expression that represents an objective or constraint for the model.

        Note
        -----
        Pyomo supports the formulation of general nonlinear algebraic expressions.
        Constraint expressions include equalities or inequalites, for example::

            1 <= x + 3y
            1 == x + 3y
            3y >= 2x
            0 <= tan(x) <= 1
       
        Objective expressions are not equations or inequalities, for example::

            x + 2y
            cos(x)**2

        A variety of standard mathematical functions are supported
        in Pyomo expressions, including cos(), sin(), tan(),
        cosh(), sinh(), tanh(), and abs().  See the Pyomo documentation for a
        complete list.

        """
        if expr is True:
            self
        elif expr.is_relational():
            self.model.c.add( expr )
        else:
            self.model.o.add( expr )
            # Annotate the objective if the user specifies that this is
            # a maximization problem.
            if self._maximize:
                n = len(self.model.o)
                self.model.o._data[n].sense = maximize
        return self

    def solve(self, name, *args, **kwargs):
        """
        Optimize the model using the named solver.

        Parameters
        ----------
        name : str
            The solver name
        \*args 
            A variable list of arguments.
        \**kwargs
            A variable list of keyword arguments.
        
        Notes
        -----
        The arguments and keyword arguments are the same as supported by Pyomo
        solver objects.
        """
        solver = SolverFactory(name)
        return solver.solve(self.model, *args, **kwargs)
   
    def pprint(self):
        """Print the equations in the model"""
        self.model.pprint()

    def display(self):
        """Display the values in the model"""
        self.model.display()
 
    def objective(self, i=1):
        """
        Return the i-th objective

        Parameters
        ----------
        i : int
            The objective index, which defaults to 1.

        Returns
        -------
        Pyomo objective object
            An object that defines an objective
        """
        return self.model.o._data[i]

    def constraint(self, i=1):
        """
        Return the i-th constraint

        Parameters
        ----------
        i : int
            The constraint index, which defaults to 1.

        Returns
        -------
        Pyomo constraint object
            An object that defines a constraint
        """
        return self.model.c._data[i]

    def constraints(self):
        """
        A generator that iterates through all constraints in the model.

        Yields
        ------
        Pyomo constraint object
            An object that defines a constraint
        """
        return six.itervalues(self.model.c)

