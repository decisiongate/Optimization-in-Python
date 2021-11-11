# Installation (Uncomment the Line Below)
# !pip install ortools

# Import Package
from ortools.linear_solver import pywraplp

# Define Environment
def prob():

#(Other Solvers: pywraplp.Solver.CreateSolver('SOLVERNAME'))
    op = pywraplp.Solver.CreateSolver('SCIP')
 
# Define Decision Variables   
    x = op.NumVar(0.0, op.infinity(), 'x')
    y = op.IntVar(0.0, op.infinity(), 'y')

# Add Objective Function to the Environment
    op.Maximize(2*x+5*y)

# Add Constraints to the Environment
    op.Add(5*x+3*y<=10)
    op.Add(2*x+7*y<=9)

# Solve the Problem 
    status = op.Solve()

# The Status of the Solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', op.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())
    else:
        print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    prob()
