# Test for output of dual variables

from pyomo_simplemodel import *

# A new problem
prob = SimpleModel()

x = prob.var("x", bounds=(0, 4))

y = prob.var("y", bounds=(-1, 1))

z = prob.var("z", bounds=(0,None))

prob += x + 4*y + 9*z

prob += x + y <= 5
prob += x + z >= 10
prob += -y+ z == 7

# Declare suffixes returned by the solver
prob.suffix('dual')
prob.suffix('rc')

status = prob.solve("glpk")

print("Status: %s" % status.solver.termination_condition)

for v in (x,y,z):
	print("%s = %f\t Reduced Cost = %f" % (v, value(v), v.get_suffix_value('rc')))

print("objective= %f" % value(prob.objective()))

print("\nSensitivity Analysis\nConstraint                     Shadow Price\tSlack")
for c in prob.constraints():
    print("%s : %-20s\t\t%s\t%s" % (c, c.expr, str(c.get_suffix_value('dual')), str(c.slack())))
