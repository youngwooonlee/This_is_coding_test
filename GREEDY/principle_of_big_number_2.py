N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
number_A = numbers[-1]
number_B = numbers[-2]
sums = number_A * K + number_B

answer = sums * (M // (K + 1)) + number_A * (M % (K + 1))

print(answer)