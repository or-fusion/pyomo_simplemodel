# A two stage stochastic planification problem adapted from PuLP
#
# Example taken from:
# "On Optimal Allocation of Indivisibles under Incertainty"
# Vladimir I. Norkin, Yuri M. Ermoliev, Andrzej Ruszczynski
# IIASA, WP-94-021, April 1994 (revised October 1995).

from pyomo.contrib.simplemodel import *
from random import *

seed(187034987)

C = 50
B = 500 # Resources available for the two years
s = 20 # Number of scenarios
n = 10 # Number of projects

N = list(range(n))
S = list(range(s))

# First year costs
c = [randint(0,C) for i in N]
# First year resources
d = [randint(0,C) for i in N]
# a=debut, b=taille
interval = [[(randint(0,C), randint(0,C)) for i in N] for j in S]
# Final earnings
q = [[randint(ai, ai+bi) for ai,bi in ab] for ab in interval]
# Second year resources
delta = [[randint(ai, ai+bi) for ai,bi in ab] for ab in interval]

# Problem
lp = SimpleModel()

# Variables
# x : Whether or not to start a project
x = lp.var("x", N, within=Binary)
# y : Whether or not to finish it, in each scenario
y = lp.var("y", S, N, within=Binary)

# Objective: expected earnings
lp += dot_product(c, x) - sum(q[j][i]*y[j,i] for i in N for j in S)/float(s)

# Resources constraints for each scenario
for j in S:
    lp += dot_product(d, x) + sum(delta[j][i]*y[j,i] for i in N) <= B

# We can only finish a project that was started
for i in N:
    for j in S:
        lp += y[j,i] <= x[i]

# Solve
lp.solve("glpk")

# Solution printing
for i in N:
    print("%s = %f" % (x[i], value(x[i])))

print("objective = %f" % value(lp.objective()))
