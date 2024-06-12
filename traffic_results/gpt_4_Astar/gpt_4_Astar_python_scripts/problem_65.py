
import heapq
import numpy as np


def a_star():
    # Define the initial state and the goal state of the problem
    initial_state = (8, 11)
    goal_state = (2, 3)
    # Define the map of the city as a 2d numpy array
    city_map = np.array([[11, 'x', 'x', 'x', 15, 5, 18, 4, 1, 17, 14, 'x', 9],
                         ['x', 10, 10, 7, 12, 12, 6, 'x', 'x', 8, 4, 19, 11],
                         [17, 'x', 'x', 12, 8, 'x', 'x', 'x', 14, 19, 'x', 18, 16],
                         [17, 'x', 16, 'x', 'x', 17, 4, 'x', 15, 'x', 'x', 'x', 17],
                         [17, 'x', 'x', 6, 'x', 'x', 12, 6, 10, 3, 11, 'x', 19],
                         [10, 'x', 9, 15, 17, 4, 'x', 'x', 'x', 'x', 14, 17, 18],
                         [4, 'x', 'x', 'x', 'x', 13, 18, 13, 'x', 17, 12, 'x', 19],
                         ['x', 2, 11, 7, 6, 14, 9, 'x', 12, 17, 9, 13, 14],
                         ['x', 18, 16, 'x', 'x', 'x', 11, 6, 12, 'x', 'x', 10, 'x'],
                         [5, 3, 'x', 'x', 'x', 5, 'x', 14, 'x', 'x', 'x', 'x', 'x'],
                         [18, 'x', 'x', 'x', 'x', 14, 'x', 'x', 13, 1, 3, 'x', 'x'],
                         [1, 16, 10, 'x', 'x', 14, 13, 'x', 10, 'x', 1, 'x', 18],
                         [8, 'x', 'x', 10, 2, 10, 'x', 'x', 'x', 'x', 'x', 13, 5]])
    # Define the districts of the city
    districts = [range(0, 3), range(3, 8), range(8, 13)]
    # Define the set of visited states
    visited = set()
    # Define the priority queue for the A* search
    queue = [(0, 0, [initial_state], initial_state, [0, 0, 0])]
    # Define the directions in which Ben can move
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        _, g, path, current_state, visited_districts = heapq.heappop(queue)
        if current_state == goal_state and all(visited_districts):
            return path
        if current_state in visited:
            continue
        visited.add(current_state)
        for dx, dy in directions:
            next_state = (current_state[0] + dx, current_state[1] + dy)
            if (0 <= next_state[0] < city_map.shape[0] and
                0 <= next_state[1] < city_map.shape[1] and
                city_map[next_state] != 'x'):
                new_visited_districts = visited_districts[:]
                for i, district in enumerate(districts):
                    if next_state[0] in district:
                        new_visited_districts[i] = 1
                new_path = path + [next_state]
                new_g = g + city_map[next_state]
                new_f = new_g + heuristic(next_state, goal_state)
                heapq.heappush(queue, (new_f, new_g, new_path, next_state, new_visited_districts))
    return None


def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
