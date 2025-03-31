from collections import Counter

def minkowski_difference(S1, S2):
    differences = Counter()
    for s1 in S1:
        for s2 in S2:
            diff = s1 - s2
            differences[diff] += 1
    
    max_multiplicity = max(differences.values())
    max_x = max(k for k, v in differences.items() if v == max_multiplicity)
    
    return max_multiplicity, max_x

S1 = [186.07931, 287.12699, 548.20532, 580.18077, 681.22845, 706.27446, 782.27613, 968.35544, 968.35544]
S2 = [101.04768, 158.06914, 202.09536, 318.09979, 419.14747, 463.17369]

multiplicity, x = minkowski_difference(S1, S2)
print(multiplicity)
print(f"{x:.5f}")
