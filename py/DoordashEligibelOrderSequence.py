# https://leetcode.com/discuss/post/4154082/doordash-phone-eligible-order-sequence-b-fz98/

from heapq import *


def process(orders: list[int]):
    orders = [float("-inf")] + orders + [float("-inf")]
    # min heap + hashmap approach, keep neighbor info in hashmap

    def is_eligible(order_id):
        left, right = neighbors[order_id]
        return order_id > left and order_id > right

    neighbors = dict()
    heap = []
    for i in range(1, len(orders) - 1):
        neighbors[orders[i]] = [orders[i - 1], orders[i + 1]]
        if orders[i] > orders[i - 1] and orders[i] > orders[i + 1]:
            heappush(heap, orders[i])

    res = []
    while heap:
        order = heappop(heap)
        res.append(order)
        # update neighbors map
        left, right = neighbors[order]
        if left != float("-inf"):
            neighbors[left][1] = right
            if is_eligible(left):
                heappush(heap, left)
        if right != float("-inf"):
            neighbors[right][0] = left
            if is_eligible(right):
                heappush(heap, right)
        neighbors.pop(order)

    return res


# --------- driver code ---------
tests = [
    ([3, 1, 5, 4, 2], [3, 5, 4, 2, 1]),
    ([30, 10, 70, 40, 20, 50, 15, 16], [16, 30, 50, 70, 40, 20, 15, 10]),
]

for orders, expected in tests:
    print("actual = {} | expected = {}".format(process(orders), expected))
