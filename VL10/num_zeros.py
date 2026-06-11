def num_zeros(liste:list[int]) -> int:
    count = 0
    for element in liste:
        if element == 0:
            count += 1
    return count

if __name__ == "__main__":
    print(num_zeros([0, 1, 2, 3]))