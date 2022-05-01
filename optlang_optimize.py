# Installation (uncomment the line below)
#!pip install optlang 

from __future__ import print_function
import optlang as op 

# Define environment
prob = op.Model(name='Simple model')

# Define decision variables
x = op.Variable('x', lb=0, type="integer")
y = op.Variable('y', lb=0)

# Add constraints to the environment
c1 = op.Constraint(5*x+3*y, ub=10)
c2 = op.Constraint(2*x+7*y, ub=9)
prob.add([c1, c2])

# Add objective function to the environment
obj = op.Objective(2*x+5*y, direction='max')
prob.objective = obj

# Solve the problem and report status
status = prob.optimize()
print("status:", prob.status)

# To display optimal decision variables
for var_name, var in prob.variables.iteritems():
    print(var_name, "=", var.primal)

# To display optimal value of objective function
print("Optimal Value of Objective Is = ", prob.objective.value)
