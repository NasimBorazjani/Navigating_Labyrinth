
import heapq

def initialize():
    coins = [26, 24, 8, 2, 11, 10, 11, 14, 20, 9, 13, 10, 25, 21, 7, 20, 15, 27, 18, 12, 23, 4, 2, 4, 22, 23, 15, 16, 24, 14, 22, 13, 15, 21, 5, 14, 2, 21, 14, 10, 2, 2, 24, 26, 17, 2, 20, 22, 3, 27, 8, 20, 2, 25, 7]
    tax_values = {24: 18, 14: 4, 15: 10, 23: 15, 26: 12, 22: 4, 17: 8, 5: 2, 18: 2, 16: 3, 11: 3, 2: 1, 27: 9, 3: 3, 10: 5, 20: 4, 4: 2, 21: 4, 12: 1, 8: 6, 13: 2, 7: 2, 9: 6, 25: 15}
    target_sum = 273
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
