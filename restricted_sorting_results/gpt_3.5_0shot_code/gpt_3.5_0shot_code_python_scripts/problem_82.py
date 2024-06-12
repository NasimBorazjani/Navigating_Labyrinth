
import heapq

# Define the initial state of the stacks
initial_state = [['Red', 'Black', 'Yellow', 'Black', 'White', 'Blue', 'White'], [], ['White', 'Blue', 'Green', 'Yellow', 'Blue', 'Yellow', 'Pink'], ['Yellow', 'Red', 'Pink', 'Green', 'Black', 'Red', 'White'], [], ['Pink', 'Red', 'Green', 'Green', 'Green', 'Black', 'Blue'], ['Pink', 'Blue', 'Blue', 'Black', 'Red', 'Pink', 'Black'], ['Yellow', 'Red', 'Pink', 'White', 'White', 'Yellow', 'Green'], [], [], [], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 7, 1: 13, 2: 10, 3: 12, 4: 4, 5: 13, 6: 2, 7: 11, 8: 11, 9: 10, 10: 8, 11: 9}

# Define a function to calculate the heuristic cost (h-value) for a given state
def heuristic(state):
    h = 0
    for stack in state:
        if stack:
            top_block = stack[0]
            h += sum(1 for block in stack if block != top_block)
    return h

# Define a function to generate the possible next states from a given state
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][0] == state[i][0]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].insert(0, new_state[i].pop(0))
                    next_states.append((new_state, i, j))
    return next_states

# Define the A* search algorithm
def astar_search(initial_state):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_list = set()

    while open_list:
        _, g, state, path = heapq.heappop(open_list)
        if state == [[], [], [], [], [], [], [], [], [], [], [], []]:
            return path
        if tuple(map(tuple, state)) in closed_list:
            continue
        closed_list.add(tuple(map(tuple, state))

        for next_state, i, j in generate_next_states(state):
            next_g = g + cost[j]
            next_h = heuristic(next_state)
            heapq.heappush(open_list, (next_g + next_h, next_g, next_state, path + [(i, j)]))

    return None

# Find the optimal sequence of moves
optimal_path = astar_search(initial_state)
print(optimal_path)
