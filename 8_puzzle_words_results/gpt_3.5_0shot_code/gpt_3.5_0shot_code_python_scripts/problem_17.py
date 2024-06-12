
from queue import PriorityQueue

def heuristic(state, target_words):
    total_cost = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != '_':
                if state[i][j] != target_words[i][j]:
                    total_cost += 1
    return total_cost

def get_neighbors(state):
    neighbors = []
    blank_pos = None
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                blank_pos = (i, j)
                break
    if blank_pos[0] > 0:
        neighbors.append((blank_pos[0]-1, blank_pos[1], 'up'))
    if blank_pos[0] < len(state)-1:
        neighbors.append((blank_pos[0]+1, blank_pos[1], 'down'))
    if blank_pos[1] > 0:
        neighbors.append((blank_pos[0], blank_pos[1]-1, 'left'))
    if blank_pos[1] < len(state[0])-1:
        neighbors.append((blank_pos[0], blank_pos[1]+1, 'right'))
    return neighbors

def a_star(initial_state, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_state, []))
    explored = set()

    while not frontier.empty():
        cost, current_state, path = frontier.get()
        if current_state == target_words:
            return path
        explored.add(str(current_state))

        for neighbor in get_neighbors(current_state):
            new_state = [list(row) for row in current_state]
            new_state[neighbor[0]][neighbor[1]], new_state[blank_pos[0]][blank_pos[1]] = new_state[blank_pos[0]][blank_pos[1]], new_state[neighbor[0]][neighbor[1]]
            if str(new_state) not in explored:
                new_cost = cost + 1 + heuristic(new_state, target_words)
                frontier.put((new_cost, new_state, path + [neighbor[2]]))

    return None

initial_state = [['e', 'h', 'r', 'y'], ['w', 'f', 'r', 'r'], ['_', 'u', 'd', 'd'], ['f', 'a', 'i', 'b']]
target_words = [['h', 'a', 'y', '_'], ['w', 'e', 'r', 'f'], ['r', 'u', 'd', 'd'], ['f', 'r', 'i', 'b']]

result = a_star(initial_state, target_words)
print(result)
