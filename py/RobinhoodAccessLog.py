# https://leetcode.com/playground/dFdc67iQ

# 1. For each user, what are the earliest and latest times they accessed any resource?
# 2. Within any 5-minute (300-second) sliding window, which resource was visited the most times, and how many times?
# 3. Given all user sessions, what is the probability of visiting a particular resource next, given the current resource?

from math import inf
from collections import defaultdict


logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["54002", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

logs2 = [
    ["400", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"],
]


def getMinAndMaxPerUser(logs):
    userVisits = defaultdict(lambda: [inf, -inf])
    for time, user, _ in logs:
        time = int(time)

        userVisits[user][0] = min(userVisits[user][0], time)
        userVisits[user][1] = max(userVisits[user][1], time)

    return userVisits


def getMostVisitedResource(logs):
    perSecMap = defaultdict(lambda: defaultdict(int))  # time -> resource -> count
    for time, _, resource in logs:
        time = int(time)
        perSecMap[time][resource] += 1

    maxCount, maxResource = 0, ""
    windowCount = defaultdict(int)  # resource -> count in 300s window
    for i in range(0, 60 * 60 * 24):
        if i > 300:
            timeToRemove = perSecMap[i - 300]
            for resource, count in timeToRemove.items():
                windowCount[resource] -= count

        curTimeVisit = perSecMap[i]
        for resource, count in curTimeVisit.items():
            windowCount[resource] += count
            if windowCount[resource] > maxCount:
                maxCount = windowCount[resource]
                maxResource = resource
    return maxResource, maxCount


# print(getMinAndMaxPerUser(logs1))
# print(getMinAndMaxPerUser(logs2))
print(getMostVisitedResource(logs1))
print(getMostVisitedResource(logs2))
