
import heapq

# Define the initial state of the stacks
initial_state = [[], ['Green', 'Yellow', 'Red', 'Red', 'Red'], [], ['Green', 'Yellow', 'Green', 'Blue', 'Black'], ['Red', 'Yellow', 'Black', 'Blue', 'Black'], [], [], ['Green', 'Black', 'Yellow', 'Blue', 'Blue']]
goal_state = [[], ['Black', 'Black', 'Blue', 'Blue', 'Green'], [], ['Red', 'Red', 'Yellow', 'Yellow', 'Yellow'], [], [], [], []]

# Define the cost of moving a block to each stack
cost = {0: 4, 1: 8, 2: 9, 3: 9, 4: 5, 5: 7, 6: 9, 7: 6}

# Define a heuristic function to estimate the cost of reaching the goal state
def heuristic(state):
    h = 0
    for i in range(len(state)):
        if state[i]:
            for j in range(len(state[i])):
                if state[i][j] != goal_state[i][j]:
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
    open_list = [(initial_state, 0, heuristic(initial_state), [])]
    closed_list = set()

    while open_list:
        state, g, h, path = heapq.heappop(open_list)

        if state == goal_state:
            return path

        if tuple(map(tuple, state)) in closed_list:
            continue

        closed_list.add(tuple(map(tuple, state)))

        for neighbor, c in get_neighbors(state):
            f = g + c + heuristic(neighbor)
            heapq.heappush(open_list, (neighbor, g + c, heuristic(neighbor), path + [(state.index(neighbor), state.index(neighbor)]))

    return None

# Find the optimal sequence of moves
optimal_path = astar(initial_state, goal_state)
print(optimal_path)
