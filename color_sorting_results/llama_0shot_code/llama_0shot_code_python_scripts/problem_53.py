
import heapq

def move(tubes, fr, to):
    """
    Perform a move operation from tube fr to tube to.
    """
    ball = tubes[fr].pop()
    tubes[to].append(ball)

def next_moves(tubes):
    """
    Generate all possible next moves.
    """
    moves = []
    for i in range(len(tubes)):
        for j in range(len(tubes)):
            if i != j and len(tubes[i]) > 0 and (len(tubes[j]) == 0 or tubes[j][-1] == tubes[i][-1]):
                moves.append((len(tubes[j]) - (len(tubes[j]) == 8), (i, j)))
    return moves

def sort_it(tubes):
    """
    Solve the Sort It problem.
    """
    tubes = [list(reversed(t)) for t in tubes]  # Reverse the tubes to sort from bottom to top
    pq = []
    heapq.heappush(pq, (0, tuple()))  # Start from the initial state
    visited = {tuple(tubes): 0}
    while pq:
        _, state = heapq.heappop(pq)
        if all(len(t) <= 1 for t in tubes):  # All balls are sorted
            return visited[state]
        for _, move in next_moves(tubes):
            fr, to = move
            new_tubes = [list(t) for t in tubes]
            move(new_tubes, fr, to)
            new_state = tuple(tuple(t) for t in new_tubes)
            if new_state not in visited:
                heapq.heappush(pq, (len(new_tubes[fr]) + len(new_tubes[to]) - 2, new_state))
                visited[new_state] = visited[state] + 1
    return None

# Test the function
tubes = [['Red', 'Blue', 'Blue', 'Red', 'Green'], ['Blue', 'Green', 'Green', 'Green', 'Blue'], ['Red', 'Green', 'Blue', 'Red', 'Red']]
print(sort_it(tubes))
