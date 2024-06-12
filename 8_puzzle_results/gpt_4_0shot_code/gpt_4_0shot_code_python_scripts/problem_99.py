
import heapq
import copy

# Define the initial state and the goal state
initial_state = [[92, 75, 100, 61, 43, 87], [64, 34, 55, 90, 20, 86], [36, '_', 32, 5, 42, 83]]
goal_state = [[100, 92, 87, 86, 83, 75], [61, 55, 43, 42, 36, 34], [32, 20, 5, '_', 90, 64]]

# Define the heuristic function
def heuristic(state):
    return sum(abs(b % 6 - g % 6) + abs(b//6 - g//6)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, 9)))

# Define the search function
def search(state):
    queue = [(heuristic(state), state)] # Priority queue

    while queue:
        (h, state) = heapq.heappop(queue)

        if state == goal_state:
            return state

        moves = []
        index = state.index(0)
        if index not in [0, 1, 2, 3, 4, 5]:
            moves.append('up')
        if index not in [0, 6, 12, 18, 24, 30]:
            moves.append('left')
        if index not in [5, 11, 17, 23, 29, 35]:
            moves.append('right')
        if index not in [30, 31, 32, 33, 34, 35]:
            moves.append('down')

        for move in moves:
            _state = copy.deepcopy(state)
            if move == 'up':
                _state[index], _state[index-6] = _state[index-6], _state[index]
            if move == 'left':
                _state[index], _state[index-1] = _state[index-1], _state[index]
            if move == 'right':
                _state[index], _state[index+1] = _state[index+1], _state[index]
            if move == 'down':
                _state[index], _state[index+6] = _state[index+6], _state[index]

            heapq.heappush(queue, (h + heuristic(_state), _state))

# Print the solution
print(search(initial_state))
