# Our goal is to build a simplified version of a real Robinhood system that reads prices from a stream and aggregates those prices into historical datapoints aka candlestick charts. We’re looking for clean code, good naming, testing, etc.

# Step 1: Parse Prices

# Your input will be a comma-separated string of prices and timestamps in the format price:timestamp e.g.

# 1:0,3:10,2:12,4:19,5:35 is equivalent to

# price: 1, timestamp: 0
# price: 3, timestamp: 10
# price: 2, timestamp: 12
# price: 4, timestamp: 19
# price: 5, timestamp: 35

# You can assume the input is sorted by timestamp and values are non-negative integers.

# Step 2: Aggregate Historical Data from Prices

# We calculate historical data across fixed time intervals. In this case, we’re interested in intervals of 10, so the first interval will be [0, 10). For each interval, you’ll build a datapoint with the following values.

# Start time
# First price
# Last price
# Max price
# Min price

# Important: If an interval has no prices, use the previous datapoint’s last price for all prices. If there are no prices and no previous datapoints, skip the interval.

# You should return a string formatted as {start,first,last,max,min}. For the prices shown above, the expected datapoints are

# {0,1,1,1,1}{10,3,4,4,2}{20,4,4,4,4}{30,5,5,5,5}

# [execution time limit] 3 seconds (cs)

# [input] string prices_to_parse

# [output] string


def aggregate_prices(prices_to_parse: str) -> str:
    if not prices_to_parse:
        return ""

    # Step 1: Parse the prices
    prices = []
    for entry in prices_to_parse.split(","):
        price_str, timestamp_str = entry.split(":")
        prices.append((int(price_str), int(timestamp_str)))

    interval = 10
    result = []
    i = 0
    n = len(prices)
    previous_last_price = None
    current_interval_start = 0

    # Determine the end time we need to process
    last_timestamp = prices[-1][1]
    end_time = (last_timestamp // interval + 1) * interval

    while current_interval_start < end_time:
        interval_end = current_interval_start + interval
        interval_prices = []

        # Collect all prices within the current interval
        while i < n and prices[i][1] < interval_end:
            interval_prices.append(prices[i])
            i += 1

        if interval_prices:
            first_price = interval_prices[0][0]
            last_price = interval_prices[-1][0]
            max_price = max(p[0] for p in interval_prices)
            min_price = min(p[0] for p in interval_prices)
            previous_last_price = last_price
        elif previous_last_price is not None:
            first_price = last_price = max_price = min_price = previous_last_price
        else:
            # No prices and no previous data; skip
            current_interval_start += interval
            continue

        result.append(
            f"{{{current_interval_start},{first_price},{last_price},{max_price},{min_price}}}"
        )
        current_interval_start += interval

    return "".join(result)


print(aggregate_prices("1:0,3:10,2:12,4:19,5:35"))
