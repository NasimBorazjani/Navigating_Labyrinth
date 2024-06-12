
import heapq

# Initial state of the stacks
stacks = [['Black', 'Blue', 'Green', 'Green', 'Pink', 'Black', 'Red'], [], ['Green', 'White', 'Yellow', 'Red', 'White', 'Blue', 'Pink'], [], [], ['Black', 'Green', 'Black', 'Yellow', 'Black', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Yellow', 'Red', 'Yellow', 'Pink'], ['Red', 'White', 'Blue', 'Pink', 'Red', 'Blue', 'White'], [], [], ['Red', 'White', 'Pink', 'Green', 'Yellow', 'White', 'Pink'], []]

# Cost of moving one block to the top of each stack
costs = {0: 7, 1: 9, 2: 13, 3: 3, 4: 4, 5: 4, 6: 6, 7: 11, 8: 12, 9: 3, 10: 13, 11: 5}

# Heuristic function to estimate the cost to reach the goal state
def heuristic(state):
    total_cost = 0
    for stack in state:
        if len(stack) > 0:
            shade = stack[0]
            total_cost += sum([costs[i] for i in range(len(stack)) if stack[i] != shade])
    return total_cost

# A* search algorithm
def astar():
    start_state = (tuple([tuple(stack) for stack in stacks]), 0)
    frontier = [(heuristic(stacks), start_state)]
    visited = set()

    while frontier:
        current_cost, (current_state, cost_so_far) = heapq.heappop(frontier)

        if current_state in visited:
            continue

        visited.add(current_state)

        if all(len(stack) == 0 or len(set(stack)) == 1 for stack in current_state):
            return current_state

        for i in range(len(current_state)):
            for j in range(len(current_state)):
                if i != j and current_state[i] and (not current_state[j] or current_state[i][0] == current_state[j][0]):
                    new_state = list(current_state)
                    new_state[j] = [current_state[i][0]] + new_state[j]
                    new_state[i] = new_state[i][1:]
                    new_cost = cost_so_far + costs[i]
                    heapq.heappush(frontier, (new_cost + heuristic(new_state), (tuple([tuple(stack) for stack in new_state]), new_cost)))

    return None

# Solve the problem
solution = astar()

# Print the list of transfer pairs
for i in range(len(stacks)):
    if stacks[i] != solution[i]:
        print((i, stacks.index(solution[i])))

