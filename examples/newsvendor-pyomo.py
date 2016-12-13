# newsvendor-pyomo.py

from pyomo.environ import *

c=1.0
b=1.5
h=0.1
d = {1:15, 2:60, 3:72, 4:78, 5:82}

scenarios = range(1,6)

M = ConcreteModel()
M.x = Var(within=NonNegativeReals)

def b_rule(B, i):
  B.y = Var()
  B.l = Constraint(expr=B.y >= (c-b)*M.x + b*d[i])
  B.u = Constraint(expr=B.y >= (c+h)*M.x + h*d[i])
  return B
M.b = Block(scenarios, rule=b_rule)

def o_rule(M):
    return sum(M.b[i].y for i in scenarios)/5.0
M.o = Objective(rule=o_rule)

solver = SolverFactory('glpk')
status = solver.solve(M)

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (M.x, value(M.x)))
for i in scenarios:
    print("%s = %f" % (M.b[i].y, value(M.b[i].y)))
print("Objective = %f" % value(M.o))

