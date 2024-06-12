
import heapq

# Initial state of the stacks
initial_state = [['Green', 'Black', 'White', 'Red', 'White', 'Yellow', 'Blue'], [], ['White', 'Pink', 'White', 'White', 'Green', 'Red', 'Blue'], [], ['Pink', 'Black', 'Black', 'White', 'Black', 'Green', 'Blue'], ['Pink', 'Green', 'Pink', 'Yellow', 'Yellow', 'Blue', 'Red'], [], ['Red', 'Yellow', 'Yellow', 'Yellow', 'Blue', 'Red', 'Black'], [], [], [], ['Red', 'Green', 'Black', 'Blue', 'Pink', 'Pink', 'Green']]
# Cost of moving one block to the top of each stack
cost = {0: 13, 1: 5, 2: 8, 3: 11, 4: 6, 5: 9, 6: 5, 7: 11, 8: 2, 9: 11, 10: 11, 11: 7}

def heuristic(state):
    # Heuristic function to estimate the cost to reach the goal state
    return sum(len(stack) for stack in state)

def get_neighbors(state):
    # Generate possible next states by moving one block at a time
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and (not state[i] or not state[j] or state[i][-1] == state[j][-1]):
                new_state = [stack.copy() for stack in state]
                if new_state[i]:
                    block = new_state[i].pop()
                    new_state[j].append(block)
                    cost_so_far = cost[i]
                    neighbors.append((new_state, cost_so_far))
    return neighbors

def a_star(initial_state):
    # A* search algorithm to find the optimal solution
    open_list = [(heuristic(initial_state), initial_state, 0)]
    closed_list = set()

    while open_list:
        _, current_state, cost_so_far = heapq.heappop(open_list)

        if current_state == [[], [], [], [], [], [], [], [], [], [], [], []]:
            return current_state

        if tuple(map(tuple, current_state)) in closed_list:
            continue

        closed_list.add(tuple(map(tuple, current_state)))

        for neighbor, neighbor_cost in get_neighbors(current_state):
            total_cost = cost_so_far + neighbor_cost + heuristic(neighbor)
            heapq.heappush(open_list, (total_cost, neighbor, cost_so_far + neighbor_cost))

    return None

solution = a_star(initial_state)
print(solution)
