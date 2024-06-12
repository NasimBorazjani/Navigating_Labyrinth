
import heapq

def dijkstra(graph, start, end, num_districts):
    queue = [(0, start, [])]
    visited_districts = set()
    while queue:
        time, current, path = heapq.heappop(queue)
        if current not in visited_districts:
            visited_districts.add(current[0] // len(graph[0]) + 1)
            if len(visited_districts) == num_districts:
                return path + [current]
        for next_node in graph[current]:
            if next_node not in visited_districts:
                heapq.heappush(queue, (time + graph[current][next_node], next_node, path + [current]))
    return None

def main():
    graph = [
        {(0, 1): 15, (0, 3): 8, (0, 4): 6, (0, 5): 11},
        {(1, 0): 15, (1, 1): 10, (1, 2): 18, (1, 3): 9, (1, 4): 2, (1, 5): 16, (1, 6): 9, (1, 7): 8},
        {(2, 1): 18, (2, 3): 10, (2, 4): 18, (2, 6): 13, (2, 7): 12, (2, 8): 14},
        {(3, 0): 11, (3, 1): 18, (3, 2): 4, (3, 3): 11, (3, 4): 14, (3, 5): 2, (3, 7): 15},
        {(4, 1): 18, (4, 3): 8, (4, 5): 10, (4, 6): 10, (4, 7): 4},
        {(5, 0): 5, (5, 1): 19, (5, 2): 20, (5, 3): 15, (5, 4): 11, (5, 6): 14, (5, 8): 18},
        {(6, 1): 5, (6, 3): 9, (6, 7): 9},
        {(7, 2): 18, (7, 4): 4, (7, 6): 4, (7, 7): 17, (7, 8): 13},
        {(8, 2): 17, (8, 4): 7, (8, 6): 7, (8, 7): 19}
    ]
    start = (3, 0)
    end = (4, 8)
    num_districts = 3
    path = dijkstra(graph, start, end, num_districts)
    print(path)

if __name__ == "__main__":
    main()
