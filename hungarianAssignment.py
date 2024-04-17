import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_assignment(cost_matrix):
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    total_cost = cost_matrix[row_ind, col_ind].sum()
    return total_cost, row_ind, col_ind

# Example usage
cost_matrix = np.array([
    [4, 1, 3],
    [2, 0, 5],
    [3, 2, 2]
])

optimal_cost, row_indices, col_indices = hungarian_assignment(cost_matrix)

print("Optimal Cost:", optimal_cost)
print("Optimal Assignments (row, column):")
for row, col in zip(row_indices, col_indices):
    print(f"Worker {row + 1} assigned to Task {col + 1}") 
