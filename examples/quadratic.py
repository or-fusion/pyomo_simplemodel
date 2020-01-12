# A simple quadratic function of two variables,
# adapted from the CPLEX file format reference manual.
# Optimal objective function value is 60. solution is x=10, y=0.

from pyomo_simplemodel import *

m = SimpleModel()

x = m.var('x', within=NonNegativeReals)
y = m.var('y', within=NonNegativeReals)
    
m += x + y >= 10

m += x + y + 0.5 * (x * x + 4 * x * y + 7 * y * y)

status = m.solve("ipopt")

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (x, value(x)))
print("%s = %f" % (y, value(y)))
print("Objective = %f" % value(m.objective()))

