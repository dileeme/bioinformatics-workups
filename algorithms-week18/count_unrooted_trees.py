def count_unrooted_binary_trees(n):
    result = 1
    for k in range(2 * n - 5, 1, -2):
        result *= k
    return result

species = ["dog", "cat", "mouse", "elephant", "rabbit"]

print(count_unrooted_binary_trees(len(species)))
