import numpy as np
from scipy import sparse
import scipy as sp
import utils.codegen_utils as cu

# Set numpy seed for reproducibility
np.random.seed(2)

n = 50
m = 150

# Generate random Matrices
Pt = sparse.random(n, n)
P = Pt.T.dot(Pt) + sparse.eye(n)
P = sparse.triu(P, format='csc')
q = sp.randn(n)
A = sparse.random(m, n).tolil()  # Lil for efficiency
u = 3 + sp.randn(m)
l = -3 + sp.randn(m)

# Make random problem primal infeasible
A[int(n/2), :] = A[int(n/2)+1, :]
l[int(n/2)] = u[int(n/2)+1] + 10 * sp.rand()
u[int(n/2)] = l[int(n/2)] + 0.5

# Convert A to csc
A = A.tocsc()

# Generate problem solutions
sols_data = {'status_test': 'primal_infeasible'}


# Generate problem data
cu.generate_problem_data(P, q, A, l, u, 'primal_infeasibility', sols_data)
