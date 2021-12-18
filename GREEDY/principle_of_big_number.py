N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
answer = 0
j = 0
for _ in range(M):
    if j == K:
        answer += numbers[-2]
        j = 0
    else:
        answer += numbers[-1]
        j += 1
print(answer)