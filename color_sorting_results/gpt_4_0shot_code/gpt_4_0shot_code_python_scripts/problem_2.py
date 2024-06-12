
from collections import deque

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    moves = []
    while not is_sorted(tubes):
        for i in range(3):
            if tubes[i]:
                for j in range(3):
                    if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1]) and len(tubes[j]) < 6:
                        ball = tubes[i].pop()
                        tubes[j].append(ball)
                        moves.append((i, j))
                        break
    return moves

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

tubes = [['Red', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Red', 'Green'], ['Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
