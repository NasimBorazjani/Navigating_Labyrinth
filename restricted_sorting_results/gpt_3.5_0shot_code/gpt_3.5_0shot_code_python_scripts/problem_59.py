
import heapq

# Define the initial state of the stacks
initial_state = [['Green', 'Blue', 'Green', 'Yellow', 'Yellow'], [], ['Red', 'Red', 'Green', 'Black', 'Black'], [], ['Blue', 'Yellow', 'Black', 'Yellow', 'Blue'], [], [], ['Black', 'Blue', 'Red', 'Red', 'Green']]

# Define the cost of moving a block to each stack
cost = {0: 1, 1: 5, 2: 5, 3: 4, 4: 8, 5: 6, 6: 8, 7: 9}

# Define a function to calculate the heuristic cost (number of blocks out of order)
def heuristic(state):
    count = 0
    for stack in state:
        for i in range(len(stack) - 1):
            if stack[i] != stack[i + 1]:
                count += 1
    return count

# Define a function to generate the possible next states
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[i][-1] == state[j][-1]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].append(new_state[i].pop())
                    next_states.append((new_state, i, j))
    return next_states

# Define the A* search algorithm
def astar(initial_state):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_list = set()

    while open_list:
        _, cost_so_far, state, path = heapq.heappop(open_list)

        if state == [[], [], [], [], ['Black', 'Black', 'Green', 'Green', 'Red'], ['Blue', 'Blue', 'Blue', 'Yellow', 'Yellow'], ['Red', 'Red', 'Yellow', 'Yellow', 'Yellow'], ['Black', 'Black', 'Green', 'Green', 'Green']]:
            return path

        if tuple(map(tuple, state)) in closed_list:
            continue

        closed_list.add(tuple(map(tuple, state)))

        for next_state, i, j in generate_next_states(state):
            new_cost = cost_so_far + cost[i]
            new_heuristic = heuristic(next_state)
            total_cost = new_cost + new_heuristic
            heapq.heappush(open_list, (total_cost, new_cost, next_state, path + [(i, j)]))

    return None

# Find the optimal sequence of moves
optimal_path = astar(initial_state)
print(optimal_path)
