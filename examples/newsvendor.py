# newsvendor.py

from pyomo.contrib.simplemodel import *

c=1.0
b=1.5
h=0.1
d = {1:15, 2:60, 3:72, 4:78, 5:82}

scenarios = range(1,6)

m = SimpleModel()
x = m.var('x', within=NonNegativeReals)
y = m.var('y', scenarios, within=NonNegativeReals)

for i in scenarios:
  m += y[i] >= (c-b)*x + b*d[i]
  m += y[i] >= (c+h)*x + h*d[i]

m += sum(y[i] for i in scenarios)/5.0

status = m.solve("glpk")

print("Status = %s" % status.solver.termination_condition)

print("%s = %f" % (x, value(x)))
for i in y:
    print("%s = %f" % (y[i], value(y[i])))
print("Objective = %f" % value(m.objective()))

