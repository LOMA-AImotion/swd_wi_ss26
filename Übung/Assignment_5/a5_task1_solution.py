"""
a5_task1.py
Code for the experiments on datastructures on slide 26 of "Data Structures"
"""

import random
import time

# different sizes of list/set for the experiments
num_elements = [10000, 100000, 500000, 1000000]
num_samples = 1000

lower_bound = 0
upper_bound = 10000000

for num_el in num_elements:
    # random.sanples draws a list with length num_el from the specified range
    elements_as_list = random.sample(range(lower_bound, upper_bound+1), num_el)
    elements_as_set = set(elements_as_list)

    print(f"Size of list: {len(elements_as_list)}")
    print(f"Size of set: {len(elements_as_set)}")

    random_samples = random.sample(range(lower_bound, upper_bound+1), num_samples)

    start_list = time.time()
    for i in random_samples:
        # not interested in the result of in, just want to run the command
        # in is used as search-operation here
        i in elements_as_list
    end_list = time.time()

    start_set = time.time()
    for i in random_samples:
        # not interested in the result of in, just want to run the command
        i in elements_as_set
    end_set = time.time()

    print(f"##### {num_el} elements #####")
    print(f"Duration for list: {end_list - start_list}")
    print(f"Duration for set: {end_set - start_set}")
    print("##############################")