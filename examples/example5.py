# Adapted from PuLP test5.py
#
# Market splitting problems from:
# G. Cornuejols, M. Dawande, A class of hard small 0-1 programs, 1998.
# With m>=4, these problems are often *very* difficult.

from pyomo.aux.simplemodel import *
from random import *

seed(127398270)

# A new problem
prob = SimpleModel()

# Parameters
# Number of constraints
m = 3
# Size of the integers involved
D = 100

# Number of variables
n = 10*(m-1)

# A vector of n binary variables
x = prob.var("x", list(range(n)), within=Binary)

# Slacks
s = prob.var("s", list(range(m)), bounds=(0,None))
w = prob.var("w", list(range(m)), bounds=(0,None))

# Objective
prob += summation(s) + summation(w)

# Constraints
d = [[randint(0,D) for i in range(n)] for j in range(m)]
for j in range(m):
	prob += summation(d[j],x) + s[j] - w[j] == sum(d[j])/2

# Solve
status = prob.solve("glpk")

# Print the status of the solved LP
print("Status: %s" % status.solver.termination_condition)

# Print the value of the variables at the optimum
for v in (x,s,w):
    for i in v:
	    print("%s = %f" % (v[i], value(v[i])))

# Print the value of the objective
print("objective= %f" % value(prob.objective()))
