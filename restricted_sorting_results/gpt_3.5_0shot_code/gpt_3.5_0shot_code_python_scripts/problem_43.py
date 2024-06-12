
import heapq

# Define the initial state of the stacks
initial_state = [['Green', 'Green', 'Red', 'Blue', 'Red'],
                 ['Black', 'Red', 'Black', 'Red', 'Green'],
                 ['Yellow', 'Green', 'Black', 'Black', 'Blue'],
                 [],
                 ['Blue', 'Yellow', 'Blue', 'Yellow', 'Yellow'],
                 [],
                 [],
                 []]

# Define the goal state
goal_state = [['Green', 'Green', 'Green', 'Green'],
              ['Red', 'Red', 'Red', 'Red'],
              ['Black', 'Black', 'Black', 'Black'],
              ['Blue', 'Blue', 'Blue', 'Blue'],
              ['Yellow', 'Yellow', 'Yellow', 'Yellow'],
              [],
              [],
              []]

# Define the cost of moving a block to each stack
cost = {0: 5, 1: 2, 2: 8, 3: 7, 4: 5, 5: 6, 6: 1, 7: 1}

# Define a heuristic function to estimate the cost of reaching the goal state
def heuristic(state):
    h = 0
    for i in range(len(state)):
        for j in range(4):
            if len(state[i]) > j and state[i][j] != goal_state[i][j]:
                h += 1
    return h

# Define a function to get the neighbors of a state
def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state)):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]):
                    new_state = [stack.copy() for stack in state]
                    new_state[j].append(new_state[i].pop())
                    neighbors.append((new_state, cost[i]))
    return neighbors

# Implement the A* search algorithm
def astar(initial_state, goal_state):
    open_list = [(heuristic(initial_state), 0, initial_state, [])]
    closed_list = set()

    while open_list:
        _, g, current_state, path = heapq.heappop(open_list)

        if current_state == goal_state:
            return path

        if tuple(map(tuple, current_state)) in closed_list:
            continue

        closed_list.add(tuple(map(tuple, current_state)))

        for neighbor, c in get_neighbors(current_state):
            heapq.heappush(open_list, (heuristic(neighbor) + g + c, g + c, neighbor, path + [(current_state.index(neighbor) - 1, current_state.index(neighbor))]))

    return None

# Find the optimal sequence of moves
optimal_path = astar(initial_state, goal_state)
print(optimal_path)
