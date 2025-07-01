# Part 1
# Food delivery companies employ tens of thousands of delivery drivers who each submit hundreds of deliveries per week.
# Delivery details are automatically sent to the system immediately after the delivery.
# Delivery drivers have different hourly payment rates, depending on their performance.
# Drivers can take on, and be paid for, multiple deliveries simultaneously.
# If a driver is paid $10.00 per hour, and a delivery takes 1 hour and 30 minutes, the driver is paid $15.00 for that delivery.
# We are building a dashboard to show a single number - the total cost of all deliveries - on screens in the accounting department offices.
# At first, we want the following functions:
# * add_driver(driver_id [integer], usd_hourly_rate [float])
#    - The given driver will not already be in the system
# * record_delivery(driver_id [integer], start_time, end_time)
#    - Discuss the time format you choose
#    - Times require minimum one-second precision
#    - The given driver will already be in the system
#    - All deliveries will be recorded immediately after the delivery is completed
#    - No delivery will exceed 3 hours
# * get_total_cost()
#    - Return the total, aggregated cost of all drivers' deliveries recorded in the system
#    - For example, return 135.30 if one driver is in the system and has a total cost of 100.30 USD and another driver is in the system and has a total cost of 35.00 USD.
#    - This will be used for a live dashboard
#    - Do not worry about exact formatting
# All inputs will be valid. use python

# You said:
# The analytics team uses the live dashboard reporting function you built to see how much money is owed in total to all drivers.
# Add the following functions:
# * pay_up_to (pay_time [integer, Unix time from epoch])
#    - Pay all drivers for recorded deliveries which ended up to and including the given time
# * get_total_cost_unpaid()
#    - Return the total, aggregated cost of all drivers' deliveries which have not been paid
# The solution does not need to be thread-safe or handle concurrency.

# Part 3
# Some cities have restrictions on the total number of drivers that can be active at any time.
# As one part of understanding our compliance with restrictions,
# our team wants to understand the maximum number of drivers who have been actively making deliveries simultaneously.
# For one of our tasks in this large project, write a new function:
# * max_simultaneous_drivers_24h_before (end_time [integer])
#    * Returns the maximum number of simultaneous drivers who were active in the 24 hours before the given end time.
# The solution does not need to be thread-safe or handle concurrency.

from collections import defaultdict
from datetime import datetime, timedelta
from typing import List, Dict
import time

class DeliveryCostDashboard:
    def __init__(self):
        self.drivers: Dict[int, float] = {}
        self.deliveries: List[Dict] = []

    def add_driver(self, driver_id: int, usd_hourly_rate: float):
        self.drivers[driver_id] = usd_hourly_rate

    def record_delivery(self, driver_id: int, start_time: datetime, end_time: datetime):
        duration_seconds = (end_time - start_time).total_seconds()
        cost = (duration_seconds / 3600.0) * self.drivers[driver_id]
        self.deliveries.append({
            'driver_id': driver_id,
            'start_time': start_time,
            'end_time': end_time,
            'cost': cost,
            'paid': False
        })

    def get_total_cost(self) -> float:
        return sum(delivery['cost'] for delivery in self.deliveries)

    def pay_up_to(self, pay_time_unix: int):
        pay_cutoff = datetime.fromtimestamp(pay_time_unix)
        for delivery in self.deliveries:
            if not delivery['paid'] and delivery['end_time'] <= pay_cutoff:
                delivery['paid'] = True

    def get_total_cost_unpaid(self) -> float:
        return sum(delivery['cost'] for delivery in self.deliveries if not delivery['paid'])

    def max_simultaneous_drivers_24h_before(self, end_time_unix: int) -> int:
        window_end = datetime.fromtimestamp(end_time_unix)
        window_start = window_end - timedelta(hours=24)

        intervalCount = defaultdict(int)
        for d in self.deliveries:
            if d['end_time'] < window_start or d['start_time'] >= window_end:
                continue  # Completely outside the window

            # Clamp delivery times to within the window
            start = max(d['start_time'], window_start)
            end = min(d['end_time'], window_end)

            intervalCount[start]+=1
            intervalCount[end]-=1

        res = cur = 0
        for time in sorted(intervalCount.keys()):
            cur += intervalCount[time]
            res = max(res, cur)  # find out the max overlap
        return res

from datetime import datetime, timedelta
import time

dashboard = DeliveryCostDashboard()
dashboard.add_driver(1, 10.0)
dashboard.add_driver(2, 12.0)
dashboard.add_driver(3, 15.0)

now = datetime(2025, 6, 30, 12, 0, 0)
t1 = now - timedelta(hours=1)
t2 = now - timedelta(hours=0.5)
t3 = now - timedelta(hours=0.75)
t4 = now - timedelta(hours=1.5)

# Deliveries overlap in the last hour
dashboard.record_delivery(1, t1, now)        # driver 1 active
dashboard.record_delivery(2, t3, t2)         # driver 2 active overlaps partially
dashboard.record_delivery(3, t4, t1)         # driver 3 active before t1

print(dashboard.max_simultaneous_drivers_24h_before(int(now.timestamp())))  # Should print 2
