import sys
import re

class Node:
    def __init__(self, name=None):
        self.name = name
        self.children = []
        self.parent = None
        self.seq = None

    def __repr__(self):
        return f"Node({self.name})"


def parse_newick(s: str) -> Node:
    s = s.strip()
    if not s.endswith(';'):
        raise ValueError('Newick must end with ;')
    s = s[:-1]

    stack = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '(':
            stack.append('(')
            i += 1
        elif c == ',':
            i += 1
        elif c == ')':
            kids = []
            while stack and stack[-1] != '(':
                kids.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise ValueError('Malformed Newick')
            stack.pop()
            kids.reverse()
            i += 1
            m = re.match(r"([A-Za-z0-9_.-]+)", s[i:])
            label = None
            if m:
                label = m.group(1)
                i += len(label)
            node = Node(label)
            for child in kids:
                child.parent = node
                node.children.append(child)
            stack.append(node)
        elif c.isspace():
            i += 1
        else:
            m = re.match(r"([A-Za-z0-9_.-]+)", s[i:])
            if not m:
                raise ValueError('Unexpected char in Newick at pos %d: %r' % (i, s[i]))
            label = m.group(1)
            node = Node(label)
            stack.append(node)
            i += len(label)

    if len(stack) != 1 or isinstance(stack[0], str):
        raise ValueError('Malformed Newick, stack=%r' % stack)
    return stack[0]


def parse_fasta(s: str):
    records = {}
    cur = None
    for line in s.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            cur = line[1:]
            records[cur] = []
        else:
            if cur is None:
                raise ValueError('FASTA format error')
            records[cur].append(line)
    for k in list(records.keys()):
        records[k] = ''.join(records[k])
    return records


def collect_nodes(root: Node):
    res = {}
    stack = [root]
    while stack:
        u = stack.pop()
        if u.name:
            res[u.name] = u
        for c in u.children:
            stack.append(c)
    return res


def find_reversing_substitutions(root: Node):
    nodes_by_name = collect_nodes(root)
    seqs = {name: nodes_by_name[name].seq for name in nodes_by_name}
    names = list(seqs.keys())
    if not names:
        return []
    L = len(next(iter(seqs.values())))

    results = []
    for parent_name, parent_node in nodes_by_name.items():
        for child in parent_node.children:
            s = parent_node.seq
            t = child.seq
            for i in range(L):
                if s[i] != t[i]:
                    a = s[i]
                    b = t[i]
                    stack = [child]
                    while stack:
                        u = stack.pop()
                        if u.seq[i] != b:
                            continue
                        for v in u.children:
                            if v.seq[i] == a:
                                results.append((child.name, v.name, i + 1, f"{a}->{b}->{a}"))
                            elif v.seq[i] == b:
                                stack.append(v)
    return results


def main():
    data = sys.stdin.read()
    if not data.strip():
        print('Provide input via stdin (Newick line ending with ;, then FASTA).')
        return

    idx = data.find(';')
    if idx == -1:
        print('No terminating ; found for Newick tree')
        return

    newick = data[:idx + 1].strip()
    fasta_part = data[idx + 1:]

    root = parse_newick(newick)
    fasta = parse_fasta(fasta_part)

    nodes = collect_nodes(root)
    for name, node in nodes.items():
        if name not in fasta:
            print(f"Error: No sequence for node '{name}' in FASTA input", file=sys.stderr)
            sys.exit(1)
        node.seq = fasta[name]

    lengths = {len(node.seq) for node in nodes.values()}
    if len(lengths) != 1:
        print('Error: sequences have differing lengths', file=sys.stderr)
        sys.exit(1)

    results = find_reversing_substitutions(root)
    for t_name, w_name, pos, rep in results:
        print(t_name, w_name, pos, rep)


if __name__ == '__main__':
    main()
