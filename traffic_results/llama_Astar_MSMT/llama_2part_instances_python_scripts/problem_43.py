
import heapq

def initialize():
    initial_state = (('x', '10', '2', 'x', 'x', 'x', '3', 'x', '4', 'x', '14'), ('x', 'x', '17', '16', '8', 'x', 'x', 'x', 'x', '1', 'x'), ('18', '18', '16', '16', '15', 'x', 'x', '17', '12', '16', '15'), ('x', '4', 'x', 'x', '18', '9', 'x', '15', 'x', '1', '9'), ('3', '2', '7', 'x', 'x', '17', '2', '14', 'x', '4', '2'), ('16', '17', '6', '4', '9', '2', '5', '7', 'x', 'x', '7'), ('x', 'x', '12', 'x', 'x', '16', '1', '11', 'x', 'x', '4'), ('x', 'x', '13', 'x', 'x', '19', '16', '9', 'x', 'x', 'x'), ('x', 'x', 'x', '9', '7', 'x', '11', '5', 'x', 'x', 'x'), ('x', '2', 'x', 'x', 'x', '4', '5', 'x', '10', 'x', 'x'), ('x', 'x', 'x', '12', '16', 'x', '6', '16', 'x', '18', '7'))
    start_workshop = (3, 10)
    end_workshop = (6, 2)
    districts = [(0, 3), (4, 5), (6, 9)]
    moves = [((- 1), 0), (1, 0), (0, (- 1)), (0, 1)]
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], start_workshop)]
    return (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue)

def a_star():
    (initial_state, start_workshop, end_workshop, districts, moves, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, current_workshop) = heapq.heappop(queue)
        if (current_workshop == end_workshop):
            return actions
        for move in moves:
            new_workshop = ((current_workshop[0] + move[0]), (current_workshop[1] + move[1]))
            if ((0 <= new_workshop[0] < len(initial_state)) and (0 <= new_workshop[1] < len(initial_state[0])) and (initial_state[new_workshop[0]][new_workshop[1]] != 'x') and any(((district[0] <= new_workshop[0] <= district[1]) for district in districts)) and any(((district[0] <= current_workshop[0] <= district[1]) for district in districts))):
                new_cost = (g + 1)
                if ((new_workshop not in visited_costs) or (new_cost < visited_costs[new_workshop])):
                    visited_costs[new_workshop] = new_cost
                    h = heuristic(new_workshop, end_workshop)
                    heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [new_workshop]), new_workshop))
    return None

def heuristic(current_workshop, end_workshop):
    return ((((current_workshop[0] - end_workshop[0]) ** 2) + ((current_workshop[1] - end_workshop[1]) ** 2)) ** 0.5)
print(a_star())
