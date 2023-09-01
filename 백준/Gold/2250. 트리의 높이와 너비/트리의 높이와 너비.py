import sys
import collections

# inits
input = sys.stdin.readline
N = int(input())
graph = dict()
is_child = [False] * (N + 1)

for _ in range(N):
    n, a, b = map(int, input().split())
    graph[n] = (a, b)
    if a != -1:
        is_child[a] = True
    if b != -1:
        is_child[b] = True

root = is_child.index(False, 1)


# make dfs_tree made by preorder traversal
def dfs(node):
    if node not in graph:
        return
    dfs(graph[node][0])
    dfs_tree.append(node)
    dfs(graph[node][1])


dfs_tree = [0]
dfs(root)


# get the answer
ans_level, max_width = 0, 0
column_of = {n: i for i, n in enumerate(dfs_tree[1:], start=1)}
nodes = collections.deque([root])  # nodes at the same level

for level in range(1, N + 1):
    if not nodes:
        break

    if (width := column_of[nodes[-1]] - column_of[nodes[0]] + 1) > max_width:
        max_width = width
        ans_level = level

    for _ in range(len(nodes)):
        p = nodes.popleft()
        l, r = graph[p][0], graph[p][1]
        if l != -1:
            nodes.append(l)
        if r != -1:
            nodes.append(r)

print(ans_level, max_width)
