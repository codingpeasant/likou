from collections import defaultdict


orders = [
    {"dasherId": 1, "orderId": 1, "timestamp": 1, "status": "a"},
    {"dasherId": 1, "orderId": 2, "timestamp": 2, "status": "a"},
    {"dasherId": 1, "orderId": 3, "timestamp": 3, "status": "a"},
    {"dasherId": 1, "orderId": 1, "timestamp": 4, "status": "f"},
    {"dasherId": 1, "orderId": 2, "timestamp": 5, "status": "f"},
    {"dasherId": 1, "orderId": 3, "timestamp": 6, "status": "f"},
    {"dasherId": 1, "orderId": 7, "timestamp": 7, "status": "a"},
    {"dasherId": 2, "orderId": 8, "timestamp": 8, "status": "a"},
    {"dasherId": 2, "orderId": 8, "timestamp": 9, "status": "f"},
    {"dasherId": 1, "orderId": 7, "timestamp": 10, "status": "f"},
    {"dasherId": 1, "orderId": 9, "timestamp": 11, "status": "a"},
]


def getPay(dasherId: int):
    dasherOrders = [order for order in orders if order["dasherId"] == dasherId]
    if not dasherId:
        return 0

    orderIdToIntervals = defaultdict(list)  # [from, to] or just [from]
    for order in dasherOrders:
        orderIdToIntervals[order["orderId"]].append(order["timestamp"])
    timeCounts = defaultdict(int)
    for interval in orderIdToIntervals.values():
        if len(interval) < 2:
            continue
        timeCounts[interval[0]] += 1
        timeCounts[interval[1]] -= 1

    timeIntervals = sorted(timeCounts.keys())
    res = 0
    curOrderCount = 0
    for i in range(len(timeIntervals) - 1):
        start = timeIntervals[i]
        to = timeIntervals[i + 1]
        curOrderCount += timeCounts[timeIntervals[i]]
        res += curOrderCount * (to - start) * curOrderCount
    return res


print(getPay(1))
print(getPay(2))
