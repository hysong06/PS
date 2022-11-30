psum, answer = 0, 0  # answer == psum that is closest to 100.

for _ in range(10):
    psum += int(input())
    if abs(psum - 100) <= abs(answer - 100):
        answer = max(psum, answer)

print(answer)
