# newsvendor-pulp.py

from pulp import *

c=1.0
b=1.5
h=0.1
d = {1:15, 2:60, 3:72, 4:78, 5:82}

scenarios = range(1,6)

M = LpProblem("Newsvendor")

x = LpVariable('x', lowBound=0)
y = LpVariable.dicts('y', scenarios)

for i in scenarios:
  M += y[i] >= (c-b)*x + b*d[i]
  M += y[i] >= (c+h)*x - h*d[i]

M += sum(y[i] for i in scenarios)/5.0

M.solve()

print("Status = %s" % LpStatus[M.status])

print("%s = %f" % (x.name, value(x.varValue)))
for i in scenarios:
    print("%s = %f" % (y[i].name, y[i].varValue))
print("Objective = %f" % value(M.objective))

