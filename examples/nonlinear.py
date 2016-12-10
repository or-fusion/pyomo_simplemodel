# Adapted from the Pyomo examples/core/simple.py problem

from pyomo.aux.simplemodel import *

m = SimpleModel()
x1 = m.var('x1')
x2 = m.var('x2', bounds=(-1,1))
x3 = m.var('x3', bounds=(1,2))

m += x1**2 + (x2*x3)**4 + x1*x3 +  x2*sin(x1+x3) + x2

status = m.solve("ipopt")

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (x1, value(x1)))
print("%s = %f" % (x2, value(x2)))
print("%s = %f" % (x3, value(x3)))
print("Objective = %f" % value(m.objective()))

