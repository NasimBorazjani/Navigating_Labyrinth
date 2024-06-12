
import heapq

class Puzzle:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.empty = [i for i in range(len(initial)) if initial[i] == '_'][0]

    def get_moves(self):
        moves = []
        if self.empty > 0:
            moves.append(self.empty - 1)
        if self.empty < len(self.initial) - 1:
            moves.append(self.empty + 1)
        return moves

    def swap(self, pos):
        new_initial = self.initial[:]
        new_initial[self.empty], new_initial[pos] = new_initial[pos], new_initial[self.empty]
        return Puzzle(new_initial, self.goal)

    def heuristic(self):
        return sum([1 if self.initial[i] != self.goal[i] else 0 for i in range(len(self.initial))])

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

def astar(puzzle):
    heap = []
    heapq.heappush(heap, puzzle)
    while heap:
        current = heapq.heappop(heap)
        if current.initial == current.goal:
            return current
        for move in current.get_moves():
            heapq.heappush(heap, current.swap(move))
    return None

initial = [88, 59, 84, 71, 80, 72, 79, 74, 96, 51, '_', 28, 25, 24, 19]
goal = [96, 88, 84, 80, 79, 74, 72, 71, 59, 51, 28, 25, 24, 19, '_']
puzzle = Puzzle(initial, goal)
solution = astar(puzzle)
moves = []
while solution and solution.initial != initial:
    moves.append(solution.initial[solution.empty])
    solution = solution.parent
moves.reverse()
print(moves)
