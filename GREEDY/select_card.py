N, M = map(int, input().split())
cards = []
for i in range(N):
    cards.append(list(map(int, input().split())))

mins = []
for i in range(N):
    mins.append(min(cards[i]))
answer = max(mins)
print(answer)
