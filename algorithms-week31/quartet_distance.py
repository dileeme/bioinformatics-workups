import re
from itertools import combinations
from collections import deque, defaultdict

def parse_newick(text):
    text = text.strip().rstrip(";")
    tokens = re.findall(r"[(),]|[^(),]+", text)
    edges = []
    leaves = {}
    counter = [0]

    def new_node():
        counter[0] += 1
        return counter[0]

    root = new_node()
    stack = [root]
    for tok in tokens:
        if tok == "(":
            child = new_node()
            edges.append((stack[-1], child))
            stack.append(child)
        elif tok == ",":
            stack.pop()
            child = new_node()
            edges.append((stack[-1], child))
            stack.append(child)
        elif tok == ")":
            stack.pop()
        else:
            leaves[stack[-1]] = tok
    return edges, leaves

def leaf_distances(text):
    edges, leaves = parse_newick(text)
    adjacency = defaultdict(list)
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)

    distances = {}
    for start_node, name in leaves.items():
        dist = {start_node: 0}
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            for neighbor in adjacency[node]:
                if neighbor not in dist:
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)
        distances[name] = {leaves[n]: dist[n] for n in leaves}
    return distances

def quartet_topology(distances, quartet):
    a, b, c, d = quartet
    options = {
        frozenset([frozenset([a, b]), frozenset([c, d])]): distances[a][b] + distances[c][d],
        frozenset([frozenset([a, c]), frozenset([b, d])]): distances[a][c] + distances[b][d],
        frozenset([frozenset([a, d]), frozenset([b, c])]): distances[a][d] + distances[b][c],
    }
    return min(options, key=options.get)

def quartet_distance(tree1, tree2):
    dist1 = leaf_distances(tree1)
    dist2 = leaf_distances(tree2)
    taxa = sorted(dist1.keys())
    mismatches = 0
    for quartet in combinations(taxa, 4):
        if quartet_topology(dist1, quartet) != quartet_topology(dist2, quartet):
            mismatches += 1
    return mismatches

tree1 = "(A,B,(C,(D,E)));"
tree2 = "(A,C,(B,(D,E)));"

print(quartet_distance(tree1, tree2))
