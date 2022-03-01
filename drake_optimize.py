# Installation (Uncomment the Line Below)
#!pip install drake

# Import package
import pydrake as op
from pydrake.solvers.gurobi import GurobiSolver

# Define environment
prob = op.solvers.mathematicalprogram.MathematicalProgram()

# Define decision variables
x = prob.NewBinaryVariables(4)
y = prob.NewContinuousVariables(1)

# Add objective function to the environment
prob.AddCost(2*(x[0]+2*x[1]+4*x[2]+6*x[3])+5*y[0])

# Add constraints to the environment
prob.AddConstraint(5*(x[0]+2*x[1]+4*x[2]+6*x[3])+3*y[0]<=10)
prob.AddConstraint(2*(x[0]+2*x[1]+4*x[2]+6*x[3])+7*y[0]<=9)

# The status of the solution
result = GurobiSolver().Solve(prog)
print(result.is_success())

# To display optimal decision variables
print('x: ', result.GetSolution(x))
print('y: ', result.GetSolution(y))

# To display optimal value of objective function
print("Optimal Value of Objective Is = ", result.get_optimal_cost())
