"""
a2_task3_solution.py
List comprehensions
L.L.
"""

# a)
# range(x, y): x, x+1, .... y-1
num_repetitions = 3
hashtag_list = ['#'*i for i in range(1, num_repetitions+1)]
print(f"Hashtag list: {hashtag_list}")

# b)
factors_list = [2, 3, 5, 10]

number = 5
result_list = [number * i for i in factors_list]

print(f"Result list: {result_list}.")

# c)
integer_list = [2, 3, 6, 1, 9, 342, 23, 97]

even_list = [i for i in integer_list if i % 2 == 0]
odd_list = [i for i in integer_list if i % 2 == 1]

print(f"Complete integer list: {integer_list}")
print(f"All even numbers are: {even_list}")
print(f"All odd numbers are: {odd_list}")