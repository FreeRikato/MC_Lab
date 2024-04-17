import lippy as lp
c_vec = [6, 6, 6]
a_matrix = [
    [4, 1, 1],
    [1, 2, 0],
    [0, 0.5, 4]
]
b_vec = [5, 3, 8]

c_vec, a_matrix, b_vec = lp.primal_to_dual_lp(c_vec, a_matrix, b_vec)
simplex = lp.SimplexMethod(c_vec, a_matrix, b_vec)
solution, func_value = simplex.solve()
print(solution, func_value)