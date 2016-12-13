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
    modeling style supported by PuLP (https://github.com/coin-or/pulp).

    This class contains a Pyomo model, and it includes methods that
    support a simple API for declaring variables, adding objectives
    and constraints, and solving the model.  Optimization results are
    stored in the variable objects, which are returned to the user.

    For example, the following model minimizes the surface area of a 
    soda can while constraining its volume:

        from pyomo.aux.simplmodel import *
        from math import pi

        m = SimpleModel()

        r = m.var('r', bounds=(0,None))
        h = m.var('h', bounds=(0,None))

        m += 2*pi*r*(r + h)
        m += pi*h*r**2 == 355

    This model can be solved with the IPOPT solver:

        status = m.solve("ipopt")
        print("Status = %s" % status.solver.termination_condition)

    The optimum value and decision variables can be easily accesed:

        print("%s = %f" % (r, value(r)))
        print("%s = %f" % (h, value(h)))
        print("Objective = %f" % value(m.objective()))

    NOTE: Here is a comparison of features between PuLP and pyomo.aux.simplemodel:
    . LP/MILP:      PuLP=YES, Simple=YES
    . NLP/MILNP:    PuLP=NO,  Simple=YES
    . Column-wise:  PuLP=YES, Simple=NO
    . Solvers:
        CPLEX       PuLP=YES, Simple=YES
        Gurobi      PuLP=YES, Simple=YES
        XPRESS      PuLP=YES, Simple=YES
        GLPK        PuLP=YES, Simple=YES
        CBC         PuLP=YES, Simple=YES
        CoinMP      PuLP=YES, Simple=NO
        Ipopt       PuLP=NO,  Simple=YES
        ASL         PulP=NO,  Simple=YES

    NOTE:  This class illustrates the basic steps in formulating
    and solving an optimization problem, but it is not meant to
    serve as a replacement for Pyomo.  Pyomo models supports a much
    richer set of modeling components than simple objectives and
    constraints.  In particular, the Block component supports the
    expression of hierarchical models with nested structure.  The
    SimpleModel class only supports a simple, flat optimization
    problems.
    """

    def __init__(self, maximize=False):
        """Constructor"""
        import pyomo.environ
        self.model = ConcreteModel()
        self.model.o = ObjectiveList()
        self.model.c = ConstraintList()
        self._maximize = maximize

    def suffix(self, name):
        """Declare a suffix with the specified name."""
        setattr(self.model, name, Suffix(direction=Suffix.IMPORT))

    def var(self, *args, **kwds):
        """
        Declare a variable.

        The first argument is the name of the variable name used by Pyomo.
        The remaining arguments are assumed to be index sets for the model.

	    The keyword arguments are the same as the keyword arguments
	    supported by the Pyomo Var component.
        """
        _args = args[1:]
        name = args[0]
        # If the variable name is "x", then the following is equivalent to:
        #  self.model.x = Var(*_args, **kwds)
        _v = Var(*_args, **kwds)
        setattr(self.model, name, _v)
        return _v

    def __iadd__(self, expr):
        """Add an objective of constraint to the model."""
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
        """Return the i-th objective"""
        return self.model.o._data[i]

    def constraint(self, i=1):
        """Return the i-th constraint"""
        return self.model.c._data[i]

    def constraints(self):
        """Iterate through all constraints"""
        return six.itervalues(self.model.c)

