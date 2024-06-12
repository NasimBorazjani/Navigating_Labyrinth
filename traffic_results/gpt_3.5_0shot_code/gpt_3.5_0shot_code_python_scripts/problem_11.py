
import heapq

def get_neighbors(matrix, row, col):
    neighbors = []
    if row > 0 and matrix[row-1][col] != 'x':
        neighbors.append((row-1, col))
    if row < len(matrix) - 1 and matrix[row+1][col] != 'x':
        neighbors.append((row+1, col))
    if col > 0 and matrix[row][col-1] != 'x':
        neighbors.append((row, col-1))
    if col < len(matrix[0]) - 1 and matrix[row][col+1] != 'x':
        neighbors.append((row, col+1))
    return neighbors

def dijkstra(matrix, start, end):
    districts = {1: [(0, 0), (0, 1), (0, 2)],
                 2: [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
                 3: [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)]}
    
    heap = [(0, start, [start])]
    visited = set()
    
    while heap:
        (cost, current, path) = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        
        if current == end:
            return path
        
        for neighbor in get_neighbors(matrix, current[0], current[1]):
            new_cost = cost + matrix[neighbor[0]][neighbor[1]]
            new_path = path + [neighbor]
            district_check = set()
            for workshop in new_path:
                for district, workshops in districts.items():
                    if workshop in workshops:
                        district_check.add(district)
            if len(district_check) == 3:
                heapq.heappush(heap, (new_cost, neighbor, new_path))
    
    return None

matrix = [[0, 15, 0, 18, 8, 6, 11, 0, 7],
          [9, 10, 18, 9, 2, 16, 9, 8, 0],
          [14, 0, 0, 10, 18, 0, 13, 12, 14],
          [11, 18, 4, 11, 14, 2, 20, 0, 15],
          [12, 0, 0, 8, 10, 0, 0, 10, 11],
          [5, 19, 20, 15, 11, 0, 14, 0, 18],
          [0, 5, 0, 0, 0, 0, 0, 9, 0],
          [0, 0, 18, 0, 0, 4, 0, 17, 13],
          [0, 7, 17, 0, 0, 0, 0, 7, 19]]

start = (3, 0)
end = (4, 8)

path = dijkstra(matrix, start, end)
print(path)
