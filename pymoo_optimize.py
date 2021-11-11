# Installation (Uncomment the Line Below)
#!pip install pymoo

# Import Packages
import numpy as np
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_termination
from pymoo.optimize import minimize

termination = get_termination("n_gen", 40)

# Solver of the Problem
algorithm = NSGA2(
    pop_size=400,
    n_offsprings=10,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)

# Define Environment
class MyOptProblem(Problem):
    def __init__(self):

# Define Decision Variables
        largenumber = 10^10
        super().__init__(n_var=2,
                         n_obj=1,
                         n_constr=2,
                         xl=np.array([0,0]),
                         xu=np.array([largenumber,largenumber]))

    def _evaluate(self, x, out, *args, **kwargs):
        
# Add Objective Function to the Environment
        f1 = -2*x[:,0] + -5*np.round(x[:,1])
        out["F"] = np.column_stack([f1])
        
# Add Constraints to the Environment
        g1 = 5*x[:,0] + 3*np.round(x[:,1]) - 10
        g2 = 2*x[:,0] + 7*np.round(x[:,1]) - 9
        out["G"] = np.column_stack([g1, g2])
       
prob = MyOptProblem()

# Solve the Problem 
res = minimize(prob,
               algorithm,
               termination,
               seed=2,
               save_history=True,
               verbose=False)

# Display Results
print("Optimal Value of Objective Is = ", -res.F[0])
