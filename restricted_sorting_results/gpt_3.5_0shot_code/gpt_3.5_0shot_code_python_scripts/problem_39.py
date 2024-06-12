
import heapq

# Define the initial state of the stacks
initial_state = [['Green', 'Green', 'Black', 'Blue', 'Black'], [], [], [], ['Yellow', 'Red', 'Black', 'Red', 'Blue'], ['Yellow', 'Blue', 'Red', 'Black', 'Blue'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow'], []]

# Define the cost of moving one block to the top of each stack
cost = {0: 8, 1: 8, 2: 1, 3: 2, 4: 9, 5: 4, 6: 7, 7: 8}

# Define a function to calculate the heuristic cost (number of blocks out of order)
def heuristic(state):
    count = 0
    for stack in state:
        for i in range(len(stack) - 1):
            if stack[i] != stack[i+1]:
                count += 1
    return count

# Define a function to generate the possible next states
def generate_next_states(state):
    next_states = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]):
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

        if state == [[], [], [], [], ['Black', 'Black', 'Green', 'Green', 'Blue'], ['Black', 'Blue', 'Red', 'Red', 'Yellow'], ['Green', 'Green', 'Red', 'Yellow', 'Yellow'], []]:
            return path

        if str(state) in closed_list:
            continue

        closed_list.add(str(state))

        for next_state, i, j in generate_next_states(state):
            new_cost = cost_so_far + cost[i]
            new_heuristic = heuristic(next_state)
            total_cost = new_cost + new_heuristic
            heapq.heappush(open_list, (total_cost, new_cost, next_state, path + [(i, j)]))

    return None

# Find the optimal sequence of moves
optimal_path = astar(initial_state)
print(optimal_path)
