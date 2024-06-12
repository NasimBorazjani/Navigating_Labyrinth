
import heapq

# Initial state of the stacks
initial_state = (
    ('Pink', 'Red', 'Black', 'Green', 'Yellow', 'Yellow', 'Pink'),
    (),
    (),
    ('Pink', 'White', 'Yellow', 'Blue', 'Green', 'Blue', 'Black'),
    ('Black', 'Blue', 'Red', 'Pink', 'Yellow', 'Yellow', 'Blue'),
    (),
    ('White', 'Black', 'Yellow', 'Green', 'Red', 'Green', 'Green'),
    (),
    (),
    ('Pink', 'Red', 'Black', 'White', 'White', 'Red', 'White'),
    ('Blue', 'Green', 'Pink', 'Blue', 'White', 'Red', 'Black'),
    ()
)

# Cost of moving one block to the top of each stack
costs = {0: 8, 1: 5, 2: 4, 3: 12, 4: 9, 5: 9, 6: 3, 7: 2, 8: 11, 9: 9, 10: 3, 11: 2}

# Define a function to calculate the heuristic cost (in this case, 0 since we want to find the minimum cost)
def heuristic(state):
    return 0

# Define a function to generate possible next states from the current state
def generate_next_states(state):
    next_states = []
    for i in range(12):
        for j in range(12):
            if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                new_state = list(state)
                new_state[j] = new_state[j] + (new_state[i][-1],)
                new_state[i] = new_state[i][:-1]
                next_states.append((tuple(new_state), i, j))
    return next_states

# A* search algorithm
def astar_search(initial_state, costs):
    frontier = [(0, initial_state, [])]
    heapq.heapify(frontier)
    explored = set()

    while frontier:
        cost, state, path = heapq.heappop(frontier)

        if state in explored:
            continue

        if all(not stack or len(set(stack)) == 1 for stack in state):
            return path

        explored.add(state)

        for next_state, i, j in generate_next_states(state):
            new_cost = cost + costs[j]
            new_path = path + [(i, j)]
            heapq.heappush(frontier, (new_cost + heuristic(next_state), next_state, new_path))

    return None

# Find the optimal transfer pairs
optimal_transfers = astar_search(initial_state, costs)
print(optimal_transfers)
