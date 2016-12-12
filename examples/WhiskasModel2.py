# The Full Whiskas Model Python Formulation adapted from PuLP
# Authors: Antony Phillips, Dr Stuart Mitchell  2007

from pyomo_simplemodel import *

# Creates a list of the Ingredients
Ingredients = ['CHICKEN', 'BEEF', 'MUTTON', 'RICE', 'WHEAT', 'GEL']

# A dictionary of the costs of each of the Ingredients is created
costs = {'CHICKEN': 0.013, 
         'BEEF': 0.008, 
         'MUTTON': 0.010, 
         'RICE': 0.002, 
         'WHEAT': 0.005, 
         'GEL': 0.001}

# A dictionary of the protein percent in each of the Ingredients is created
proteinPercent = {'CHICKEN': 0.100, 
                  'BEEF': 0.200, 
                  'MUTTON': 0.150, 
                  'RICE': 0.000, 
                  'WHEAT': 0.040, 
                  'GEL': 0.000}

# A dictionary of the fat percent in each of the Ingredients is created
fatPercent = {'CHICKEN': 0.080, 
              'BEEF': 0.100, 
              'MUTTON': 0.110, 
              'RICE': 0.010, 
              'WHEAT': 0.010, 
              'GEL': 0.000}

# A dictionary of the fibre percent in each of the Ingredients is created
fibrePercent = {'CHICKEN': 0.001, 
                'BEEF': 0.005, 
                'MUTTON': 0.003, 
                'RICE': 0.100, 
                'WHEAT': 0.150, 
                'GEL': 0.000}

# A dictionary of the salt percent in each of the Ingredients is created
saltPercent = {'CHICKEN': 0.002, 
               'BEEF': 0.005, 
               'MUTTON': 0.007, 
               'RICE': 0.002, 
               'WHEAT': 0.008, 
               'GEL': 0.000}

# Create the 'prob' variable to contain the problem data
prob = SimpleModel()

# A dictionary called 'ingredient_vars' is created to contain the referenced Variables
ingredient_vars = prob.var("Ingr",Ingredients, bounds=(0,None))

# Adding the objective function to 'prob'
prob += sum(costs[i]*ingredient_vars[i] for i in Ingredients) # "Total Cost of Ingredients per can"

# Adding five constraints to 'prob'
prob += sum(ingredient_vars[i] for i in Ingredients) == 100  # "PercentagesSum"
prob += sum(proteinPercent[i] * ingredient_vars[i] for i in Ingredients) >= 8.0 # "ProteinRequirement"
prob += sum(fatPercent[i] * ingredient_vars[i] for i in Ingredients) >= 6.0 # "FatRequirement"
prob += sum(fibrePercent[i] * ingredient_vars[i] for i in Ingredients) <= 2.0 # "FibreRequirement"
prob += sum(saltPercent[i] * ingredient_vars[i] for i in Ingredients) <= 0.4 # "SaltRequirement"

# Solve
status = prob.solve("glpk")

# Print the status of the solution
print("Status: %s" %  status.solver.termination_condition)

# Print the optimum
for v in ingredient_vars:
    print("%s = %f" % (ingredient_vars[v], value(ingredient_vars[v])))

# Print the optimized objective function value
print("Total Cost of Ingredients per can = %f " % value(prob.objective()))
