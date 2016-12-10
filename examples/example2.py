# This example is adapted from the PuLP version of the todd.mod 
# problem included in the GLPK # 4.4 distribution. 
# It's a hard knapsack problem.

from pyomo.aux.simplemodel import *
from math import *

# A new problem
prob = SimpleModel(maximize=True)

# Parameters
# Size of the problem
n = 15
k = floor(log(n)/log(2));

# A vector of n binary variables
x = prob.var("x", list(range(n)), bounds=(0,1), within=Integers)

# A vector of weights
a = [pow(2,k + n + 1) + pow(2,k + n + 1 - j) + 1 for j in range(1,n+1)]
# The maximum weight
b = 0.5 * floor(sum(a))

# The total weight
weight = summation(a, x)

# Objective
prob += weight
# Constraint
prob += weight <= b

# Optimize
status = prob.solve("glpk")

# Print the status of the solved LP
print("Status: %s" % status.solver.termination_condition)

# Print the value of the variables at the optimum
for i in x:
    print("%s = %f" % (x[i], value(x[i])))

# Print the value of the objective
print("objective = %f" % value(prob.objective()))

