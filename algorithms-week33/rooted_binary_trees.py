def count_rooted_binary_trees(n, modulus=1000000):
    result = 1
    for k in range(2 * n - 3, 1, -2):
        result = (result * k) % modulus
    return result

species = ["dog", "cat", "mouse", "elephant", "rabbit", "horse", "wolf"]

print(count_rooted_binary_trees(len(species)))
