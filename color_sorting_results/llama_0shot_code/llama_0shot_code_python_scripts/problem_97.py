
from collections import Counter

def sort_it(tubes):
    colors = [tube[0] for tube in tubes]
    color_counts = Counter(colors)
    moves = []

    while len(set(colors)) > 1:
        most_common_color = color_counts.most_common(1)[0][0]
        least_common_tube = min([(color_counts[tube[0]], i) for i, tube in enumerate(tubes) if color_counts[tube[0]] > 0 and tube[0] != most_common_color], default=(float('inf'), None))[1]
        most_common_tube = colors.index(most_common_color)
        colors[least_common_tube] = most_common_color
        colors[most_common_tube] = tubes[most_common_tube].pop()
        color_counts[most_common_color] -= 1
        color_counts[tubes[most_common_tube][0]] += 1
        moves.append((most_common_tube, least_common_tube))

    return moves

tubes = [['Red', 'Red', 'Blue', 'Red', 'Blue', 'Green'], ['Red', 'Green', 'Blue', 'Blue', 'Green', 'Red'], ['Blue', 'Green', 'Green', 'Red', 'Blue', 'Green']]
print(sort_it(tubes))
