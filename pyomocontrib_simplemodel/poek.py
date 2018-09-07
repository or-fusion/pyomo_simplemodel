__all__ = ['SimpleModel']

from core import SimpleModel
import poek


class PoekModel(SimpleModel):
    """
    This class illustrates how Peak can be used to define a optimization
    models that conform to the SimpleModel API.

    This class constructs a Peak model, and it includes methods that
    support a simple API for declaring variables, adding objectives
    and constraints, and solving the model.  Optimization results
    are stored in the variable objects, which are returned to the
    user.

    For example, the following model minimizes the surface area of
    a soda can while constraining its volume::

        from pyomo.contrib.simplmodel import *
        from math import pi

        m = PeakModel()

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
    """

    def __init__(self, maximize=False):
        """
        Parameters
        __________
        maximize : Optional[bool]
            If True, then the objective sense is maximization.
        """
        self.model = poek.create_model()
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
        raise RuntimeError
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
        _v = poek.create_variable(self.model, name, *_args, **kwds)
        return _v

    def __iadd__(self, expr):
        """
        Add an objective or constraint to the model.

        Parameters
        ----------
        expr : Peak expression
            An expression that represents an objective or constraint for the model.

        Note
        -----
        PeakPyomo supports the formulation of general nonlinear algebraic expressions.
        Constraint expressions include equalities or inequalites, for example::

            1 <= x + 3y
            1 == x + 3y
            3y >= 2x
            inequality(0, tan(x), 1)
       
        Objective expressions are not equations or inequalities, for example::

            x + 2y
            cos(x)**2

        A variety of standard mathematical functions are supported
        in Peak expressions, including cos(), sin(), tan(),
        cosh(), sinh(), tanh(), and abs().
        """
        if expr is True:
            self
        elif expr.is_relational():
            poek.add_constraint(model, None, expr)
        else:
            poek.add_objective(model, None, expr, self._maximize)
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
        solver = poek.SolverFactory(name)
        return solver.solve(self.model, *args, **kwargs)
   
    def pprint(self):
        """Print the equations in the model"""
        poek.print_model(self.model)

    def display(self):
        """Display the values in the model"""
        poek.display_model(self.model)
 
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
        raise RuntimeError
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
        raise RuntimeError
        return self.model.c._data[i]

    def constraints(self):
        """
        A generator that iterates through all constraints in the model.

        Yields
        ------
        Pyomo constraint object
            An object that defines a constraint
        """
        raise RuntimeError
        return six.itervalues(self.model.c)

