# https://leetcode.com/playground/XprywfeP

from collections import defaultdict, deque


# Given a list of badge records (employee name and badge-in time in 24-hour format without colon, e.g., "835" for 8:35 AM), identify all employees who used their badge three or more times within any 60-minute window.

badge_records = [
    ["Paul", "1355"],
    ["Jennifer", "1910"],
    ["John", "835"],
    ["John", "830"],
    ["Paul", "1315"],
    ["John", "1615"],
    ["John", "1640"],
    ["Paul", "1405"],
    ["John", "855"],
    ["John", "930"],
    ["John", "915"],
    ["John", "730"],
    ["John", "940"],
    ["Jennifer", "1335"],
    ["Jennifer", "730"],
    ["John", "1630"],
    ["Jennifer", "5"],
]


def get_time_diff(start, end):
    if end < start:
        raise ValueError("End time is before start time")
    hour_diff = end // 100 - start // 100
    minute_diff = end % 100 - start % 100
    return hour_diff * 60 + minute_diff


def find_target_employees(records):
    # Group times per employee
    emp_times = defaultdict(list)
    for name, time_str in records:
        emp_times[name].append(int(time_str))

    targets = {}

    # For each employee, sort their times and apply sliding window
    for name, times in emp_times.items():
        times.sort()
        q = deque()
        for time in times:
            while q and get_time_diff(q[0], time) > 60:
                q.popleft()
            q.append(time)
            if len(q) >= 3:
                targets[name] = list(q)
                break  # Stop at first valid window

    return targets


print(find_target_employees(badge_records))
