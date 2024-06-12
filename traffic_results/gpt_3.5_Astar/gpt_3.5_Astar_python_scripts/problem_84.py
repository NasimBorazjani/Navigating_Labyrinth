
import heapq
import math

def a_star():
    # Define the matrix map of the city
    city_map = [[math.inf, 10, 16, 12, math.inf, math.inf, math.inf, math.inf, 18, 18, 10, math.inf, math.inf, 19],
                [7, math.inf, math.inf, 11, 5, 13, 6, math.inf, math.inf, math.inf, math.inf, math.inf, 8, 14],
                [math.inf, 15, 6, 20, 4, 9, 16, 9, 16, math.inf, 11, math.inf, math.inf, 9],
                [1, 16, math.inf, math.inf, math.inf, 6, 15, 1, 10, 10, 9, 4, math.inf, 4],
                [math.inf, math.inf, math.inf, 1, 12, math.inf, 12, 17, math.inf, math.inf, 13, math.inf, math.inf, 2],
                [math.inf, math.inf, 9, math.inf, math.inf, math.inf, math.inf, 17, math.inf, math.inf, math.inf, math.inf, 10, 11],
                [7, math.inf, 7, 12, math.inf, math.inf, math.inf, 2, 2, 8, 10, 8, math.inf, math.inf],
                [3, 3, math.inf, 16, 11, math.inf, 4, 6, math.inf, math.inf, 4, 17, 13, 16],
                [4, 15, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 11, 19, 16, math.inf, math.inf, math.inf],
                [10, 5, 17, math.inf, 2, math.inf, math.inf, 3, 10, 3, 12, math.inf, 8, math.inf],
                [math.inf, 17, 12, math.inf, math.inf, math.inf, 6, 2, 13, math.inf, math.inf, math.inf, math.inf, math.inf],
                [math.inf, 10, math.inf, math.inf, 15, math.inf, math.inf, math.inf, 8, math.inf, 3, math.inf, math.inf, 19],
                [1, 7, math.inf, math.inf, 16, math.inf, math.inf, math.inf, 3, 15, 10, 12, 6, 8],
                [math.inf, math.inf, math.inf, math.inf, 9, math.inf, math.inf, math.inf, 7, math.inf, math.inf, math.inf, math.inf, 8]]
    
    # Define the districts
    district1 = set(range(3))
    district2 = set(range(3, 9))
    district3 = set(range(9, 14))
    
    # Define the start and end workshops
    start = (9, 10)
    end = (2, 3)
    
    visited_costs = {}
    visited_costs[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, 0, [start], start))
    
    while queue:
        _, g, path, current = heapq.heappop(queue)
        
        if current == end and all(len(set(path) & district) > 0 for district in [district1, district2, district3]):
            return path
        
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = current[0] + i, current[1] + j
            if 0 <= new_i < len(city_map) and 0 <= new_j < len(city_map[0]) and city_map[new_i][new_j] != 'x':
                new_cost = g + city_map[new_i][new_j]
                new_path = path + [(new_i, new_j)]
                if new_cost < visited_costs.get((new_i, new_j), math.inf):
                    visited_costs[(new_i, new_j)] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic((new_i, new_j), end), new_cost, new_path, (new_i, new_j)))
    
    return None

def heuristic(current, end):
    # A heuristic function that calculates the Manhattan distance between two points
    return abs(current[0] - end[0]) + abs(current[1] - end[1])

print(a_star())
