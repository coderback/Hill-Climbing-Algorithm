# Hill-Climbing-Optimization-Algorithm
This repository contains a Python implementation of the Hill Climbing optimization algorithm applied to a minimisation fitness function.

## Getting Started
These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites
Make sure you have the required Python packages installed. You can install them using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Configuration
You can modify the following parameters in the hill_climbing.py script:

- d: Number of genes in an individual.
- iterations: Number of iterations for the Hill Climbing algorithm.


### Test Function
The optimization algorithm is applied to the following test function defined in the script:

``` bash
def test_function(ind):
    n = len(ind.variable)
    sum_part = sum(i * (2 * ind.variable[i] ** 2 - ind.variable[i - 1]) ** 2 for i in range(2, n))
    return (ind.variable[0] - 1) ** 2 + sum_part
Feel free to replace it with your own function in the script.
```

### Results
The script prints the final solution and plots the utility values over iterations using Matplotlib.
