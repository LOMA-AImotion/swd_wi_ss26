# for number in range(10):
#     print(f"Current loop: {number}")

example_list = [1, 2.012, False, "Hello"]

for i in range(len(example_list)):
    print(f"Current element: {example_list[i]}")

print(20*"-")

# This is equivlent to l6ff, but much easier and less error prone 
for element in example_list:
    print(f"Current element: {element}")

print(20*"-")

factors = [1, 2, 3]
number = 100

# result_list = []
# for factor in factors:
#     result_list.append(number * factor)

result_list = [number * factor for factor in factors]

print(result_list)

