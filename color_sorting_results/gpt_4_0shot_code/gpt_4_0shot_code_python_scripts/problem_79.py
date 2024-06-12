
from collections import deque

def sort_it(tubes):
    tubes = [deque(tube) for tube in tubes]
    moves = []
    visited = set()

    def dfs(tubes):
        state = tuple(tuple(tube) for tube in tubes)
        if state in visited:
            return False
        visited.add(state)

        # Check if tubes are sorted
        if all(len(set(tube)) <= 1 for tube in tubes):
            return True

        for i in range(3):
            if tubes[i]:
                for j in range(3):
                    if i != j and (not tubes[j] or tubes[j][-1] == tubes[i][-1]) and len(tubes[j]) < 9:
                        ball = tubes[i].pop()
                        tubes[j].append(ball)
                        moves.append((i, j))
                        if dfs(tubes):
                            return True
                        moves.pop()
                        tubes[j].pop()
                        tubes[i].append(ball)
        return False

    dfs(tubes)
    return moves

tubes = [['Red', 'Green', 'Red', 'Blue', 'Blue', 'Green'], ['Green', 'Green', 'Red', 'Red', 'Blue', 'Blue'], ['Blue', 'Red', 'Green', 'Blue', 'Green', 'Red']]
print(sort_it(tubes))
