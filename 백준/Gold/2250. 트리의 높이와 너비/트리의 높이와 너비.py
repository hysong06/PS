import collections
import sys

# inits
input = sys.stdin.readline
N = int(input())
graph = [(0, 0) for _ in range(N + 1)]
root = set(range(1, N + 1))

for _ in range(N):
    n, l, r = map(int, input().split())
    graph[n] = (l, r)
    root.discard(l)
    root.discard(r)

root = root.pop()


# 1. make dfs_tree by inorder traversal
# 2. get the column where each nodes locate by using dfs_tree
def dfs(node):
    l, r = graph[node]
    if l != -1:
        dfs(l)
    dfs_tree.append(node)
    if r != -1:
        dfs(r)


dfs_tree = [0]
dfs(root)

column_of = [0] * (N + 1)
for i, n in enumerate(dfs_tree):
    column_of[n] = i


# get the answer: (ans_level, max_width)
level, ans_level = 1, 0
max_width = 0
row = collections.deque([root])

while row:
    if (width := column_of[row[-1]] - column_of[row[0]] + 1) > max_width:
        max_width = width
        ans_level = level

    for _ in range(len(row)):
        l, r = graph[row.popleft()]
        if l != -1:
            row.append(l)
        if r != -1:
            row.append(r)

    level += 1

print(ans_level, max_width)
