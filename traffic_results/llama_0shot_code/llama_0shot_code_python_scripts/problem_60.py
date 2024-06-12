
import heapq

def shortest_path(matrix):
    # size of the matrix
    n, m = len(matrix), len(matrix[0])

    # helper function to get neighbours of a cell
    def neighbours(r, c):
        for x, y in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= x < n and 0 <= y < m and matrix[x][y] != 'x':
                yield x, y

    # convert matrix to graph
    graph = {(r, c): list(neighbours(r, c)) for r in range(n) for c in range(m) if matrix[r][c] != 'x'}

    # start and end positions
    start, end = (3, 0), (9, 7)

    # shortest distances from start to all other nodes
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # track districts visited
    districts_visited = set()

    # priority queue for nodes to visit
    queue = [(0, start)]

    # path dictionary to store the path
    path = {start: None}

    # districts each node belongs to
    district = {(r, c): (r // 4) + 1 for r in range(n) for c in range(m) if matrix[r][c] != 'x'}

    # required districts to visit
    required_districts = set(range(1, 4))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        # check if the end node is reached
        if current_node == end:
            nodes = []
            while current_node is not None:
                nodes.append(current_node)
                current_node = path[current_node]
            return nodes[::-1]  # shortest path from start to end

        # visiting districts
        districts_visited.add(district[current_node])

        # check if all districts are visited
        if districts_visited == required_districts:
            return None  # stop if all districts are visited

        for neighbour in graph[current_node]:
            distance = current_distance + matrix[neighbour[0]][neighbour[1]]
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                path[neighbour] = current_node
                heapq.heappush(queue, (distance, neighbour))

    return None  # if no path is found

matrix = [
    ['x', '5', '6', 'x', 'x', 'x', 'x', '6', 'x'],
    ['x', 'x', 'x', '5', 'x', '5', '7', 'x', 'x'],
    ['3', '19', 'x', 'x', 'x', '18', 'x', '13', '7', 'x'],
    ['13', 'x', 'x', '8', '7', '4', 'x', '15', 'x', 'x'],
    ['5', '17', '18', '12', '3', 'x', '14', '2', '4', '18', 'x', '1'],
    ['4', '10', '1', '19', '10', 'x', 'x', '17', 'x', '17', '16', '4'],
    ['7', 'x', '16', 'x', '1', '3', 'x', '13', 'x', 'x'],
    ['x', 'x', '9', '1', '7', '18', '16', '3', 'x', 'x'],
    ['2', 'x', '13', '10', 'x', 'x', 'x', 'x', 'x', '12'],
    ['x', 'x', 'x', '18', '8', '4', 'x', '11', 'x', '14', '18', 'x'],
    ['x', '19', '2', 'x', '2', '6', '5', 'x', '5', 'x', 'x'],
    ['x', '2', '7', 'x', 'x', '8', '7', 'x', '11', '16', 'x']
]

print(shortest_path(matrix))
