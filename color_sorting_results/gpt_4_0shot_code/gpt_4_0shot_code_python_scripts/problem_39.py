
from collections import deque

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    moves = []
    while not is_sorted(tubes):
        for i in range(len(tubes)):
            if tubes[i]:
                for j in range(len(tubes)):
                    if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1]):
                        move_ball(tubes, i, j)
                        moves.append((i, j))
                        break
    return moves

def is_sorted(tubes):
    for tube in tubes:
        if tube and len(set(tube)) > 1:
            return False
    return True

def move_ball(tubes, i, j):
    tubes[j].append(tubes[i].pop())

tubes = [['Red', 'Green', 'Blue', 'Red'], ['Blue', 'Red', 'Blue', 'Green'], ['Green', 'Red', 'Blue', 'Green']]
print(sort_it(tubes))
