
import heapq
import copy

# Define the initial state and goal state
initial_state = [[79, 82, 80, 67, 45], [51, '_', 63, 41, 5], [39, 99, 31, 16, 50]]
goal_state = [[99, 82, 80, 79, 67], [63, 51, 45, 41, 39], [31, 16, 5, '_', 50]]

# Define the possible moves
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Define the heuristic function
def heuristic(state):
    return sum(abs(b % 5 - g % 5) + abs(b//5 - g//5)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, 16)))

# Define the search function
def search(state):
    queue = [(heuristic(state), state)]  # Priority queue

    while queue:
        (h, state) = heapq.heappop(queue)

        if state == goal_state:
            return state

        moves = []
        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_state = copy.deepcopy(state)
            pos = [(index, row.index('_')) for index, row in enumerate(new_state) if '_' in row][0]
            if 0 <= pos[0] + d[0] < 3 and 0 <= pos[1] + d[1] < 3:
                new_state[pos[0]][pos[1]], new_state[pos[0] + d[0]][pos[1] + d[1]] = new_state[pos[0] + d[0]][pos[1] + d[1]], new_state[pos[0]][pos[1]]
                moves.append(new_state[pos[0] + d[0]][pos[1] + d[1]])

        for move in moves:
            heapq.heappush(queue, (h + heuristic(move), move))

    return None

# Print the solution
print(search(initial_state))
