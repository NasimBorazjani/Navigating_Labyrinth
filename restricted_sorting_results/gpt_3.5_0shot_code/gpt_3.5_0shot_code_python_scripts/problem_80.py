
import heapq

# Initial state of the stacks
initial_state = (
    ('Yellow', 'Yellow', 'Pink', 'Black', 'Green', 'Green', 'Yellow'),
    ('Pink', 'Yellow', 'White', 'Red', 'Black', 'Blue', 'Blue'),
    (),
    (),
    ('Pink', 'Green', 'Pink', 'Pink', 'Blue', 'Red', 'Red'),
    ('Black', 'Black', 'Black', 'Blue', 'Yellow', 'Red', 'White'),
    (),
    (),
    (),
    (),
    ('Green', 'Blue', 'Red', 'Red', 'Green', 'White', 'Black'),
    ('White', 'White', 'Green', 'Yellow', 'Blue', 'White', 'Pink')
)

# Cost of moving one block to the top of each stack
costs = {0: 12, 1: 11, 2: 5, 3: 11, 4: 10, 5: 9, 6: 5, 7: 5, 8: 3, 9: 10, 10: 5, 11: 5}

# Define a function to calculate the heuristic cost (in this case, 0 since we want to find the optimal solution)
def heuristic(state):
    return 0

# Define a function to get the possible next states from the current state
def get_next_states(state):
    next_states = []
    for i in range(12):
        for j in range(12):
            if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                new_state = list(state)
                new_state[j] = new_state[j] + (new_state[i][-1],)
                new_state[i] = new_state[i][:-1]
                next_states.append((tuple(new_state), (i, j)))
    return next_states

# A* search algorithm
def astar_search(initial_state, costs):
    frontier = [(0, initial_state, [])]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        cost, state, actions = heapq.heappop(frontier)

        if state in explored:
            continue

        if all(not stack or len(set(stack)) == 1 for stack in state):
            return actions

        explored.add(state)

        for next_state, action in get_next_states(state):
            new_cost = cost + costs[action[1]]
            heapq.heappush(frontier, (new_cost + heuristic(next_state), next_state, actions + [action]))

    return None

# Solve the problem
solution = astar_search(initial_state, costs)
print(solution)
