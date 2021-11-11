# Installation (Uncomment the Line Below)
#!pip install mip

# Import Package
import mip as op

# Define Environment
prob = op.Model("MyOptProblem")

# Define Decision Variables
x = [prob.add_var(var_type=op.INTEGER) for i in range(1)]
y = [prob.add_var() for i in range(1)]

# Add Objective Function to the Environment
prob.objective = op.maximize(2*x[0]+5*y[0])

# Add Constraints to the Environment
prob += 5*x[0]+3*y[0]<=10
prob += 2*x[0]+7*y[0]<=9

# The Status of the Solution
print(prob.optimize())

# To Display Optimal Decision Variables
print('x: ',  x[0].x)
print('y: ',  y[0].x)

# To Display Optimal Value of Objective Function
print("Optimal Value of Objective Is = ",prob.objective_value)
