# Installation (Uncomment the Line Below)
#!pip install gekko

# Import Packages
from gekko import GEKKO

# Define Environment
prob = GEKKO(remote=False)

# Define Decision Variables
x = prob.Var(lb=0,ub=None,integer=True)
y = prob.Var(lb=0,ub=None)

# Add Objective Function to the Environment
prob.Obj(-(2*x+5*y)) # Objective

# Add Constraints to the Environment
prob.Equation(5*x+3*y<=10)
prob.Equation(2*x+7*y<=9)

# Solve the Problem (1: MINLP solver, 2,3: Other Solvers)
prob.options.SOLVER=1  
prob.solve(disp=False) 

# Display Results
print('Results')
print('x: ' + str(x.value))
print('y: ' + str(y.value))
print('Optimal Value of Objective Is = ' + str(-prob.options.objfcnval))
