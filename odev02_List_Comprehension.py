n = 2
valid_permutations = []

for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            arr = [i, j, k]
            if sum(arr) != n:
                valid_permutations.append(arr)

print(valid_permutations)
