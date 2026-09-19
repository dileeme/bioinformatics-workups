def color_tree(leaf_colors, children):
    colors = dict(leaf_colors)
    remaining = set(children.keys())
    while remaining:
        for node in list(remaining):
            kids = children[node]
            if all(kid in colors for kid in kids):
                kid_colors = {colors[kid] for kid in kids}
                colors[node] = kid_colors.pop() if len(kid_colors) == 1 else 2
                remaining.discard(node)
    return colors

leaf_colors = {0: 0, 1: 0, 2: 1, 3: 1}
children = {4: [0, 1], 5: [2, 3], 6: [4, 5]}

colors = color_tree(leaf_colors, children)
print(" ".join(str(colors[node]) for node in sorted(colors)))
