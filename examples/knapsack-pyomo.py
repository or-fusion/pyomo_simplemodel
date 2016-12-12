#
# Knapsack Problem - Pyomo
#

from pyomo.environ import *

v = {'hammer':8, 'wrench':3, 'screwdriver':6, 'towel':11}
w = {'hammer':5, 'wrench':7, 'screwdriver':4, 'towel':3}
limit = 14
items = list(sorted(v.keys()))

# Create model
m = ConcreteModel()

# Variables
m.x = Var(items, within=Binary)

# Objective
m.value = Objective(expr=sum(v[i]*m.x[i] for i in items), sense=maximize)

# Constraint
m.weight = Constraint(expr=sum(w[i]*m.x[i] for i in items) <= limit)


# Optimize
solver = SolverFactory('glpk')
status = solver.solve(m)

# Print the status of the solved LP
print("Status = %s" % status.solver.termination_condition)

# Print the value of the variables at the optimum
for i in items:
    print("%s = %f" % (m.x[i], value(m.x[i])))

# Print the value of the objective
print("Objective = %f" % value(m.value))

