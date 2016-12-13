# sodacan-pyomo.py

from pyomo.environ import *
from math import pi

m = ConcreteModel()

m.r = Var(bounds=(0,None))
m.h = Var(bounds=(0,None))

m.o = Objective(expr=2*pi*m.r*(m.r + m.h))
m.c = Constraint(expr=pi*m.h*m.r**2 == 355)

solver = SolverFactory('ipopt')
status = solver.solve(m)

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (m.r, value(m.r)))
print("%s = %f" % (m.h, value(m.h)))
print("Objective = %f" % value(m.o))

