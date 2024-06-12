
import heapq

def initialize():
    coins = [7, 2, 20, 24, 9, 24, 29, 6, 32, 26, 17, 61, 33, 14, 12, 20, 15, 34, 60, 18, 18, 37, 25, 9, 9, 21, 24, 30, 28, 3, 21, 32, 13, 10, 4, 2, 33, 36, 13, 24, 27, 7, 21, 4, 8, 17, 22, 3, 21, 12]
    tax_values = {28: 10, 36: 13, 18: 13, 17: 8, 24: 3, 37: 19, 60: 16, 13: 5, 14: 8, 30: 18, 20: 5, 27: 16, 26: 11, 2: 2, 21: 3, 7: 7, 8: 6, 3: 3, 25: 20, 22: 8, 15: 12, 12: 4, 32: 11, 9: 5, 34: 15, 4: 2, 29: 5, 33: 6, 6: 6, 10: 3, 61: 10}
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
