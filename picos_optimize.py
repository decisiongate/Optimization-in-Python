# Installation (uncomment the line below)
# !pip install picos

# Import package
import picos as op

# Define environment
prob = op.Problem("MyOptProblem")

# Define decision variables
x = op.RealVariable("x", lower = 0)
y = op.IntegerVariable("y", lower = 0)

# Add objective function to the environment
prob.set_objective('max', 2*x+5*y)

# Add constraints to the environment
prob += 5*x+3*y<=10
prob += 2*x+7*y<=9

# Solve the problem
prob.solve(solver='glpk')

# To display results
print('x: ',  x.value)
print('y: ',  y.value)
print("Optimal Value of Objective Is = ", prob.obj_value())
