# Installation (uncomment the line below)
# !pip install cvxopt
# !pip install cvxpy

# Import package
import cvxpy as op

# Define decision variables
x = op.Variable(1,integer=True)
y = op.Variable(1)

bound_x = [0 <= x]
bound_y = [0 <= y]

# Add objective function to the environment
objective = op.Maximize(2*x+5*y)

# Add constraints to the environment
cons1 = [5*x+3*y<=10]
cons2 = [2*x+7*y<=9]

# Define environment
prob = op.Problem(objective, cons1+cons2+bound_x+bound_y)

# Solve the problem
prob.solve(solver='GLPK_MI')

# To display results
print('x: ',  x.value)
print('y: ',  y.value)
print("Optimal Value of Objective Is = ", objective.value)
