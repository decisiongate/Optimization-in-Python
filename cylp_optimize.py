# Installation (Uncomment the Line Below)
#!pip install cylp

# Import package
from cylp.cy import CyClpSimplex
import cylp as op 

# Define environment
prob = op.py.modeling.CyLPModel()

# Add variables
x = prob.addVariable('x', 1, isInt=True)
y = prob.addVariable('y', 1)

# Add constraints
prob += 5*x[0]+3*y[0]<=10
prob += 2*x[0]+7*y[0]<=9
prob += y[0] >= 0
prob += x[0] >= 0

# Add constraints to the environment
prob.objective = -1*(2*x[0]+5*y[0])

# The status of the solution
cbcModel = op.cy.CyClpSimplex(prob).getCbcModel()
print(cbcModel.solve())
print (cbcModel.status)

# To display optimal decision variables
print("x: ", cbcModel.primalVariableSolution['x'][0])
print("y: ", cbcModel.primalVariableSolution['x'][0])


# To display optimal value of objective function
print("Optimal Value of Objective Is = ", -cbcModel.objectiveValue)
