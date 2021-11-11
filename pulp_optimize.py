# Installation (Uncomment the Line Below)
# !pip install pulp

# Import Package
import pulp as op

# Define Environment & Direction of Optimization
prob = op.LpProblem("MyOptProblem", op.LpMaximize)

# Define Decision Variables
x = op.LpVariable("x", lowBound = 0, upBound = None, cat='Continuous')
y = op.LpVariable("y", lowBound = 0, upBound = None, cat='Integer')

# Add Objective Function to the Environment
prob += 2*x+5*y, "Objective"

# Add Constraints to the Environment
prob += 5*x+3*y<=10, "Constraint1"
prob += 2*x+7*y<=9,  "Constraint2"

# Solve the Problem (Other Solvers: prob.solve(SOLVERNAME()))
prob.solve()

# The Status of the Solution
print("Status:", op.LpStatus[prob.status])

# To Display Optimal Decision Variables
for variables in prob.variables():
    print(variables.name, "=", variables.varValue)

# To Display Optimal Value of Objective Function
print("Optimal Value of Objective Is = ", op.value(prob.objective))
