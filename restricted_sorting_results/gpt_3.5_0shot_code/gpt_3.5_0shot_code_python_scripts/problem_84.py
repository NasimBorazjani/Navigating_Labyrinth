
import heapq

# Initial state of the stacks
initial_state = [[], [], [], [], ['Pink', 'Red', 'Green', 'Pink', 'White', 'Blue', 'Yellow'], [], ['Yellow', 'White', 'Yellow', 'Blue', 'Yellow', 'Black', 'White'], ['Black', 'Green', 'Pink', 'Pink', 'Green', 'Yellow', 'Green'], ['White', 'Blue', 'Red', 'Red', 'Red', 'Yellow', 'Black'], ['Black', 'Blue', 'Blue', 'Pink', 'Red', 'White', 'Green'], [], ['Blue', 'Black', 'Black', 'White', 'Red', 'Green', 'Pink']]
# Cost of moving one block to the top of each stack
cost = {0: 12, 1: 3, 2: 11, 3: 5, 4: 11, 5: 13, 6: 2, 7: 2, 8: 12, 9: 4, 10: 2, 11: 10}

def heuristic(state):
    # Heuristic function to estimate the cost to reach the goal state
    return sum(len(stack) for stack in state) - 6

def is_goal_state(state):
    # Check if the state is a goal state
    return all(len(stack) == 6 for stack in state)

def get_neighbors(state):
    # Generate neighboring states by moving blocks between stacks
    neighbors = []
    for i in range(12):
        for j in range(12):
            if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                new_state = [stack.copy() for stack in state]
                new_state[j].append(new_state[i].pop())
                cost = 1 if i == j else 0
                neighbors.append((new_state, cost))
    return neighbors

def solve(initial_state, cost):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_list = set()

    while open_list:
        _, g, state, path = heapq.heappop(open_list)

        if is_goal_state(state):
            return path

        closed_list.add(tuple(state))

        for neighbor_state, neighbor_cost in get_neighbors(state):
            if tuple(neighbor_state) not in closed_list:
                new_g = g + neighbor_cost
                new_path = path + [(state.index(stack), neighbor_state.index(neighbor_state))]
                heapq.heappush(open_list, (new_g + heuristic(neighbor_state), new_g, neighbor_state, new_path))

    return None

solution = solve(initial_state, cost)
print(solution)
