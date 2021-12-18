N, K = map(int, input().split())

cnt = 0

while True:
    target = (N // K) * K
    cnt += N - target
    N = target

    if N < K:
        break
    N //= K
    cnt += 1

cnt += N - 1

print(cnt)
