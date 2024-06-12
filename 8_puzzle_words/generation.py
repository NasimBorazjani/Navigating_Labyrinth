import numpy as np
import random
import nltk
from nltk.corpus import words
nltk.download('words')


def find_words(lengths, seed):
    random.seed(seed)
    word_list = words.words()
    result = []
    for length in lengths:
        words_of_length = [word.lower() for word in word_list if len(word) == length]
        if words_of_length:
            result.append(random.choice(words_of_length))
    return result

def generate_word_board(h, w, seed):
    word_lengths = [w for i in range(h)]
    word_lengths[0] = w - 1
    words = find_words(word_lengths, seed)
    target_words = words[:]
    words[0] = "_" + words[0]
    board = np.zeros((h, w)).tolist()
    for i in range(h):
        for j in range(w):
            board[i][j] = words[i][j]
    board[0][0] = "_"
    return board, target_words

def swap_blank(board_main, seed):
    board = board_main[:]
    random.seed(seed)
    h = len(board)
    w = len(board[0])
    # Find the blank cell
    blank_pos = [(i, row.index("_")) for i, row in enumerate(board) if "_" in row][0]  

    swapped = False
    seed -= 1
    while not swapped:
        seed += 1
        random.seed(seed)
        # Generate a random move
        move = random.choice(['up-left', 'down-left', 'up-right', 'down-right'])

        if move == 'up-left' and blank_pos[0] > 0 and blank_pos[1] > 0:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0] - 1][blank_pos[1] - 1] = board[blank_pos[0] - 1][blank_pos[1] - 1], board[blank_pos[0]][blank_pos[1]]
            swapped = True
        elif move == 'down-left' and blank_pos[0] < h -1  and blank_pos[1] > 0:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0] + 1][blank_pos[1] - 1] = board[blank_pos[0] + 1][blank_pos[1] - 1], board[blank_pos[0]][blank_pos[1]]
            swapped = True
        elif move == 'up-right' and blank_pos[0] > 0 and blank_pos[1] < w -1:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0] - 1][blank_pos[1] + 1] = board[blank_pos[0] - 1][blank_pos[1] + 1], board[blank_pos[0]][blank_pos[1]]
            swapped = True
        elif move == 'down-right' and blank_pos[0] < h-1 and blank_pos[1] < w-1:
            board[blank_pos[0]][blank_pos[1]], board[blank_pos[0] + 1][blank_pos[1] + 1] = board[blank_pos[0] + 1][blank_pos[1] + 1], board[blank_pos[0]][blank_pos[1]]
            swapped = True

    return board

def generate_puzzle(h, w, num_moves, seed):
    board, target_words = generate_word_board(h, w, seed)
    for i in range(num_moves):
        seed += i
        board = swap_blank(board, seed)
    return board, target_words


"""print(generate_word_board(4, 4, 1))
print(generate_puzzle(4, 4, 100, 1))"""
