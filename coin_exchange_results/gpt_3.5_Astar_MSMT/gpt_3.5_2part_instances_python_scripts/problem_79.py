
import heapq

def initialize():
    coins = [33, 4, 5, 9, 31, 26, 25, 19, 31, 33, 24, 6, 13, 17, 15, 37, 7, 21, 3, 23, 22, 7, 3, 11, 19, 28, 24, 32, 27, 31, 24, 12, 23, 22, 16, 6, 33, 8, 19, 13, 5, 11, 10, 4, 8, 16, 14, 17, 13, 9, 25, 17]
    tax_values = {3: 3, 19: 1, 5: 2, 9: 4, 17: 4, 24: 11, 8: 5, 22: 10, 4: 2, 32: 10, 16: 1, 37: 5, 23: 12, 26: 18, 12: 1, 27: 9, 14: 5, 25: 13, 15: 8, 6: 6, 21: 13, 10: 3, 31: 17, 7: 3, 33: 10, 11: 2, 28: 10, 13: 10}
    target_sum = 389
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
