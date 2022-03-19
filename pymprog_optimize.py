# Installation (uncomment the line below)
# !pip install pymprog

# Import package
import pymprog as op

# Define environment
op.begin('MyOptProb')

# Define decision variables
x = op.var('x',bounds=(0,None),kind=int) 
y = op.var('y',bounds=(0,None)) 

# Add objective function to the environment
op.maximize(2 * x + 5 * y, 'objective')

# Add constraints to the environment
5*x + 3*y <= 10 
2*x + 7*y <= 9 

# Solve the problem
op.solve()

# To display optimal decision variables
print("x: ", x.primal)
print("y: ", y.primal)

# To display optimal value of objective function
print("Optimal Value of Objective Is = ", op.vobj())

op.end()
