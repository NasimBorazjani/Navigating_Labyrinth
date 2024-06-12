
from queue import PriorityQueue

def get_blank_position(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)

def is_goal_state(board, target_words):
    for i in range(len(target_words)):
        if ''.join(board[i]) != target_words[i]:
            return False
    return True

def get_neighbors(board, blank_pos):
    neighbors = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in directions:
        x, y = blank_pos[0] + dx, blank_pos[1] + dy
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            new_board = [list(row) for row in board]
            new_board[blank_pos[0]][blank_pos[1]], new_board[x][y] = new_board[x][y], new_board[blank_pos[0]][blank_pos[1]]
            neighbors.append((tuple(tuple(row) for row in new_board), (x, y)))
    return neighbors

def heuristic(board, target_words):
    cost = 0
    for i in range(len(target_words)):
        for j in range(len(target_words[i])):
            if board[i][j] != target_words[i][j]:
                cost += 1
    return cost

def a_star_search(initial_board, target_words):
    frontier = PriorityQueue()
    frontier.put((0, initial_board, get_blank_position(initial_board), []))
    explored = set()

    while not frontier.empty():
        _, current_board, blank_pos, actions = frontier.get()

        if is_goal_state(current_board, target_words):
            return actions

        if current_board in explored:
            continue

        explored.add(current_board)

        for neighbor, new_blank_pos in get_neighbors(current_board, blank_pos):
            new_actions = actions + [(blank_pos, new_blank_pos)]
            cost = len(new_actions) + heuristic(neighbor, target_words)
            frontier.put((cost, neighbor, new_blank_pos, new_actions))

    return None

initial_board = [['a', 'j', '_', 'k', 'e'], ['t', 's', 'w', 'y', 'e'], ['t', 'r', 'a', 'p', 'a'], ['s', 'e', 'a', 'm', 'h'], ['c', 'r', 's', 'e', 'p']]
target_words = ['jake', 'tawse', 'trypa', 'smash', 'creep']

actions = a_star_search(tuple(tuple(row) for row in initial_board), target_words)
print(actions)
