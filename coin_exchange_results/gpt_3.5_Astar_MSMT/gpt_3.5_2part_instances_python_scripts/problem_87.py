
import heapq

def initialize():
    coins = [25, 41, 34, 19, 19, 36, 37, 13, 28, 26, 181, 7, 14, 6, 29, 36, 33, 7, 8, 43, 19, 9, 3, 2, 18, 40, 43, 22, 23, 21]
    tax_values = {21: 5, 26: 13, 36: 8, 28: 8, 34: 12, 3: 2, 6: 2, 23: 10, 2: 2, 9: 5, 41: 4, 29: 19, 7: 6, 18: 18, 43: 2, 8: 7, 181: 9, 25: 10, 33: 8, 14: 13, 13: 1, 22: 13, 40: 7, 37: 11, 19: 11}
    target_sum = 449
    visited_costs = {}
    visited_costs[(0, 0, 0)] = 0
    queue = [(0, 0, [], (0, 0, 0))]
    return (coins, tax_values, target_sum, visited_costs, queue)

def a_star():
    (coins, tax_values, target_sum, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        (total_value, prev_coin, total_tax) = state
        if (total_value == target_sum):
            return actions
        for coin in coins:
            if ((coin not in actions) and ((total_value + coin) <= target_sum)):
                if (((coin < prev_coin) and ((coin % 2) == 0)) or ((coin >= prev_coin) and ((coin % 2) != 0))):
                    coin_tax = tax_values[coin]
                    new_total_tax = (total_tax + coin_tax)
                    new_state = ((total_value + coin), coin, new_total_tax)
                    new_cost = (g + coin_tax)
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((g + new_total_tax), new_cost, (actions + [coin]), new_state))
    return None
print(a_star())
