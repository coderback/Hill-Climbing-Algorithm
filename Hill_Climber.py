import random
import matplotlib.pyplot as plt

d = 20
N = d + 1  # Number of genes in an individual
iterations = 250000 # Number of iterations for hill climbing


class Solution:
    def __init__(self):
        self.variable = [0] * N
        self.utility = 0


def test_function(ind):
    n = len(ind.variable)
    sum_part = sum(i * (2 * ind.variable[i] ** 2 - ind.variable[i - 1]) ** 2 for i in range(2, n))
    return (ind.variable[0] - 1) ** 2 + sum_part


def clip(value, lower, upper):
    """Clip the value to be within the specified range."""
    return max(lower, min(value, upper))

# Initial solution
initial_solution = Solution()
for j in range(N):
    initial_solution.variable[j] = clip(random.uniform(-10, 10), -10, 10)
initial_solution.utility = test_function(initial_solution)



def hill_climbing(initial_solution, iterations):
    current_solution = initial_solution
    utility_values = []  # List to store utility values during iterations

    for iteration in range(iterations):
        neighbor = Solution()
        neighbor.variable = current_solution.variable.copy()

        change_point = random.randint(0, N - 1)
        neighbor.variable[change_point] = clip(random.uniform(-10, 10), -10, 10)
        neighbor.utility = test_function(neighbor)

        if neighbor.utility <= current_solution.utility:
            current_solution = neighbor

        utility_values.append(current_solution.utility)  # Collect utility values

    return current_solution, utility_values


# Run hill climbing algorithm and collect utility values
final_solution, utility_values = hill_climbing(initial_solution, iterations)#
# Print the final solution
print("Final Solution:")
print("Genes:", final_solution.variable)
print("Utility:", final_solution.utility)

# Plot utility values over iterations
plt.plot(range(iterations), utility_values)
plt.xlabel('Iteration')
plt.ylabel('Utility')
plt.title('Utility over Iterations in Hill Climbing')
plt.show()
