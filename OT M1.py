#!/usr/bin/env python
# coding: utf-8

# A company has 5 jobs to be done. The following matrix shows the return in terms of rupees on assigning ith ( i = 1, 2, 3, 4, 5 ) machine to the jth job ( j = A, B, C, D, E ). Assign the five jobs to the five machines so as to maximize the total expected profit.
# 
# Write a Java/MATLAB/ Python programming or Excel to find the optimal solution of the given problem.
# 
# Jobs
#         Machines
#       A  B  C  D E
#     1 5 11 10 12 4
#     2 2  4  6  3 5
#     3 3 12  5 14 6
#     4 6 14  4 11 7
#     5 7  9  8 12 5
# 
# 

# In[5]:


from scipy.optimize import linear_sum_assignment

profits = [    [5, 11, 10, 12, 4],
    [2, 4, 6, 3, 5],
    [3, 12, 5, 14, 6],
    [6, 14, 4, 11, 7],
    [7, 9, 8, 12, 5]
]

row_ind, col_ind = linear_sum_assignment(profits)

optimal_assignment = [(i+1, col_ind[i]+1) for i in range(len(row_ind))]
total_profit = sum([profits[row_ind[i]][col_ind[i]] for i in range(len(row_ind))])

print("Optimal Assignment:", optimal_assignment)
print("Total Profit:", total_profit)


# In[1]:


import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the matrix of returns
returns = np.array([
    [1, 5, 11, 10, 12, 4],
    [2, 2, 4, 6, 3, 5],
    [3, 3, 12, 5, 14, 6],
    [4, 6, 14, 4, 11, 7],
    [5, 7, 9, 8, 12, 5]
])

# Subtract the minimum value from each row to make all values non-negative
returns -= returns.min(axis=1, keepdims=True)

# Subtract the minimum value from each column to make all values non-negative
returns -= returns.min(axis=0)

# Use the Hungarian algorithm to find the optimal assignment
row_indices, col_indices = linear_sum_assignment(-returns)

# Print the optimal assignment and total expected profit
for row, col in zip(row_indices, col_indices):
    print(f"Job {chr(col+65)} assigned to Machine {row+1}")
total_profit = -returns[row_indices, col_indices].sum()
print(f"Total expected profit: {total_profit}")


# In[2]:


import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the matrix of returns
returns = np.array([
    [5, 11, 10, 12, 4],
    [2, 4, 6, 3, 5],
    [3, 12, 5, 14, 6],
    [6, 14, 4, 11, 7],
    [7, 9, 8, 12, 5],
])

# Use the Hungarian algorithm to find the optimal assignment
row_ind, col_ind = linear_sum_assignment(-returns)

# Print the optimal assignment and the total profit
print('Optimal assignment:')
for i, j in zip(row_ind, col_ind):
    print(f'Machine {i+1} -> Job {chr(ord("A")+j)}')
total_profit = -returns[row_ind, col_ind].sum()
print(f'Total profit: {total_profit} rupees')


# In[2]:


import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the matrix of profits
profits = np.array([
    [5, 11, 10, 12, 4],
    [2, 4, 6, 3, 5],
    [3, 12, 5, 14, 6],
    [6, 14, 4, 11, 7],
    [7, 9, 8, 12, 5]
])

# Find the optimal assignment using the Hungarian algorithm
row_ind, col_ind = linear_sum_assignment(-profits)

# Print the optimal assignment and the total expected profit
print("Optimal assignment:")
for i in range(len(row_ind)):
    print(f"Machine {col_ind[i]+1} is assigned to job {row_ind[i]+1}")
optimal_profit = -profits[row_ind, col_ind].sum()
print(f"Total expected profit: {optimal_profit}")


# In[4]:


from scipy.optimize import linear_sum_assignment

profits = [[5, 11, 10, 12, 4],
    [2, 4, 6, 3, 5],
    [3, 12, 5, 14, 6],
    [6, 14, 4, 11, 7],
    [7, 9, 8, 12, 5]
]

row_ind, col_ind = linear_sum_assignment(profits, True)

optimal_assignment = [(i+1, col_ind[i]+1) for i in range(len(row_ind))]
total_profit = profits[row_ind, col_ind].sum()

print("Optimal Assignment:", optimal_assignment)
print("Total Profit:", total_profit)


# In[ ]:




