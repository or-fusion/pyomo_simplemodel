# newsvendor-pyomo.py

from pyomo.environ import *

c=1.0
b=1.5
h=0.1
d = {1:15, 2:60, 3:72, 4:78, 5:82}

scenarios = range(1,6)

M = ConcreteModel()
M.x = Var(within=NonNegativeReals)
M.y = Var(scenarios)

def greater_rule(M, i):
  return M.y[i] >= (c+h)*M.x + h*d[i]
M.greater = Constraint(scenarios, rule=greater_rule)

def less_rule(M, i):
  return M.y[i] >= (c-b)*M.x + b*d[i]
M.less = Constraint(scenarios, rule=less_rule)

def o_rule(M):
    return sum(M.y[i] for i in scenarios)/5.0
M.o = Objective(rule=o_rule)

solver = SolverFactory('glpk')
status = solver.solve(M)

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (M.x, value(M.x)))
for i in scenarios:
    print("%s = %f" % (M.y[i], value(M.y[i])))
print("Objective = %f" % value(M.o))

