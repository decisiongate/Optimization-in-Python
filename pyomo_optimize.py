# Installation (Uncomment the Line Below)
# !pip install pyomo

# Import Package
import pyomo.environ as op

# Define Environment
prob = op.ConcreteModel("MyOptProblem")

# Define Decision Variables
prob.x = op.Var([1],domain=op.NonNegativeReals)
prob.y = op.Var([1],domain=op.PositiveIntegers)

# Add Objective Function to the Environment
prob.OBJ = op.Objective(expr=2*prob.x[1]+5*prob.y[1])

# Add Constraints to the Environment
prob.Constraint1 = op.Constraint(expr=5*prob.x[1]+3*prob.y[1]<=10)
prob.Constraint2 = op.Constraint(expr=2*prob.x[1]+7*prob.y[1]<=9)

# Solve the Problem
solver = op.SolverFactory('SOLVERNAME')
results = solver.solve(prob)

# To Display Results
print(results)
