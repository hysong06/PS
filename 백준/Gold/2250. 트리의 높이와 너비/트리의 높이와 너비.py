import collections
import sys

# inits
input = sys.stdin.readline
N = int(input())
graph = [None] * (N + 1)
root = set(range(1, N + 1))

for _ in range(N):
    n, a, b = map(int, input().split())
    graph[n] = (a, b)
    root.discard(a)
    root.discard(b)

root = root.pop()


# make dfs_tree made by inorder traversal
def dfs(node):
    if node != -1:
        dfs(graph[node][0])
        dfs_tree.append(node)
        dfs(graph[node][1])


dfs_tree = [0]
dfs(root)


# get the answer
level, ans_level = 1, 0
max_width = 0
column_of = {n: i for i, n in enumerate(dfs_tree[1:], start=1)}
row = collections.deque([root])

while row:
    if (width := column_of[row[-1]] - column_of[row[0]] + 1) > max_width:
        max_width = width
        ans_level = level

    for _ in range(len(row)):
        p = row.popleft()
        l, r = graph[p]
        if l != -1:
            row.append(l)
        if r != -1:
            row.append(r)

    level += 1

print(ans_level, max_width)
