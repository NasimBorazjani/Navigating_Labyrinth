
import heapq
import copy

# Define the initial state and goal state
initial_state = [[87, 49, 79, 68, '_'], [56, 19, 64, 37, 7], [27, 15, 41, 35, 78]]
goal_state = [[87, 79, 68, 64, 56], [49, 41, 37, 35, 27], [19, 15, 7, '_', 78]]

# Define the directions that a tile can move
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# Define the heuristic function
def heuristic(state):
    return sum(abs(b % 5 - g % 5) + abs(b//5 - g//5)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, 9)))

# Define the A* search algorithm
def astar():
    heap = [(heuristic(initial_state), initial_state)] # heap is a list of tuples (f-score, state)
    while heap:
        f_score, current_state = heapq.heappop(heap)
        if current_state == goal_state:
            return f_score, current_state
        for d in directions:
            new_state = copy.deepcopy(current_state)
            i, j = divmod(new_state.index('_'), 5) # find the empty spot
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < 3 and 0 <= nj < 5: # check if the new spot is inside the grid
                new_state[ni*5+nj], new_state[i*5+j] = new_state[i*5+j], new_state[ni*5+nj] # swap tiles
                new_f_score = f_score + 1 + heuristic(new_state)
                heapq.heappush(heap, (new_f_score, new_state))

# Run the A* search algorithm
f_score, result = astar()
print("The shortest list of tiles that need to be swapped is:", result)
