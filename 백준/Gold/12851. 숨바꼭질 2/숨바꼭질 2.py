from collections import deque, defaultdict
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

### edge cases ###
if K <= N:
    print(N - K)
    print(1)
    exit(0)


### common cases ###
MAX = 100_000
queue = deque([N])
visit = [0] * (MAX + 1)
visit[N] = True


def inspect():
    counter = defaultdict(int)

    for _ in range(len(queue)):
        cur = queue.popleft()
        for nxt in (cur - 1, cur + 1, 2 * cur):
            if nxt < 0 or nxt > MAX:  # block IndexError
                continue
            if not visit[nxt] and not counter[nxt]:
                queue.append(nxt)
            counter[nxt] += visit[cur]

    for point, count in counter.items():
        if not visit[point]:
            visit[point] += count


for seconds in range(1, MAX + 1):
    inspect()
    if K in queue:
        break

print(seconds)
print(visit[K])
