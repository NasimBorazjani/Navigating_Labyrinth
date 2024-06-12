
import heapq

def initialize():
    coins = [14, 29, 39, 40, 16, 35, 17, 37, 43, 30, 28, 26, 13, 13, 42, 30, 10, 7, 44, 5, 34, 7, 32, 11, 40, 35, 12, 34, 35, 38, 29, 42, 33, 26, 4, 36, 41, 35, 26, 34, 16, 6, 38, 13, 41, 23, 20]
    tax_values = {11: 4, 10: 3, 41: 9, 34: 4, 7: 2, 17: 16, 29: 8, 37: 1, 44: 8, 30: 13, 32: 9, 20: 18, 23: 8, 6: 4, 5: 3, 14: 3, 13: 7, 35: 4, 33: 5, 39: 9, 40: 11, 28: 3, 4: 2, 43: 14, 42: 15, 38: 14, 16: 5, 36: 5, 12: 9, 26: 1}
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
