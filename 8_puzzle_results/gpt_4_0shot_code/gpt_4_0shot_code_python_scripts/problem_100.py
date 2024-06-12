
import numpy as np
from queue import PriorityQueue

class Puzzle:
    goal_state = np.array([[94, 91, 76, 74, 29, '_'], [93, 61, 37, 34, 44, 17], [69, 67, 55, 32, 26, 19]])
    initial_state = np.array([[94, 91, 76, '_', 74, 29], [61, 93, 17, 37, 34, 44], [67, 32, 55, 19, 26, 69]])
    swap_list = []

    def __init__(self):
        self._queue = PriorityQueue()
        self._queue.put((0, self.initial_state))

    def solve(self):
        while not self._queue.empty():
            priority, state = self._queue.get()
            if np.array_equal(state, self.goal_state):
                return self.swap_list
            else:
                empty_spot = tuple(map(int, np.where(state == '_')))
                for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_spot = (empty_spot[0] + direction[0], empty_spot[1] + direction[1])
                    if 0 <= new_spot[0] < 3 and 0 <= new_spot[1] < 6:
                        new_state = np.copy(state)
                        new_state[empty_spot], new_state[new_spot] = new_state[new_spot], new_state[empty_spot]
                        self.swap_list.append(new_state[new_spot])
                        self._queue.put((priority + 1, new_state))

puzzle = Puzzle()
print(puzzle.solve())
