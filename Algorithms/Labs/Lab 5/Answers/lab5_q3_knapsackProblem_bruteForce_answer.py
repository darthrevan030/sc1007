import time
import itertools
import matplotlib.pyplot as plt


def brute_force_knapsack(weights, values, W):
    n = len(weights)
    max_value = 0
    best_combination = []

    # itertools.product((0, 1], repeat = n): generate all possible binary combinations (of Os and 1s) of length n.
    # Each combination is a tuple where each element indicates whether an item is excluded (0) or included (1)
    for combination in itertools.product([0, 1], repeat = n): #(0(2^n))
        total_weight = sum(weights[i] for i in range(n) if combination[i] == 1)
        total_value = sum(values[i] for i in range(n) if combination[i] == 1)

        # Alternative implementation of the above two lines:
        # total_weight = np.sum(np.array(weights)T" np.array(combination))
        # total_value = np.sum(np.array(values) ' np.array(combination))


    if total_weight <= W and total_value > max_value:
        max_value = total_value
        best_combination = combination 
        
    
    selected_items = [(weights[i], values[i]) for i in range(n) if best_combination[i] == 1]
    total_selected_weight = sum(item[0] for item in selected_items)
    
    return max_value, selected_items, total_selected_weight


def measure_time(func, weights, values, W):
    start_time = time.time()
    max_value, selected_items, total_weight = func(weights, values, W)
    return time.time() - start_time, max_value, selected_items, total_weight


def read_input(filename):
    scenarios = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
