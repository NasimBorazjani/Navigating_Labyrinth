
import heapq

def manhattan_distance(state):
    goal_state = [[60, 66, 46, 8, 36], [81, 77, 88, 70, 24], [20, 17, 6, 62, 28]]
    distance = 0
    for i in range(3):
        for j in range(5):
            if state[i][j] != '_':
                x_goal, y_goal = divmod(goal_state[i][j] - 1, 5)
                x_state, y_state = divmod(state[i][j] - 1, 5)
                distance += abs(x_goal - x_state) + abs(y_goal - y_state)
    return distance

def get_neighbors(state):
    neighbors = []
    empty_x, empty_y = None, None
    for i in range(3):
        for j in range(5):
            if state[i][j] == '_':
                empty_x, empty_y = i, j
                break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = empty_x + dx, empty_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 5:
            new_state = [row.copy() for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            neighbors.append(new_state)
    return neighbors

def a_star_search(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state)]
    visited = set()
    while heap:
        _, cost, state = heapq.heappop(heap)
        if state == [[60, 66, 46, 8, 36], [81, 77, 88, 70, 24], [20, 17, 6, 62, 28]]:
            return cost
        if str(state) in visited:
            continue
        visited.add(str(state))
        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (manhattan_distance(neighbor) + cost + 1, cost + 1, neighbor))

initial_state = [[60, 66, 46, 8, 36], [81, '_', 88, 70, 24], [20, 17, 6, 62, 28]]
shortest_path = a_star_search(initial_state)
print(shortest_path)
