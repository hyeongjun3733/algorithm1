import sys
N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

M = max(score)


crt_score = []

for i in score:
    crt_score.append(i / M *100)

print(sum(crt_score) / len(crt_score))