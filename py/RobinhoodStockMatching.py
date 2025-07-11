# https://leetcode.com/discuss/post/1052406/robinhood-telephonic-interviewreject-by-el99b/


from heapq import heappop, heappush


def getExecuted(orders: list[list]) -> int:
    sellH, buyH = [], []  # min, max
    res = 0
    for price, amount, type in orders:
        price = int(price)
        amount = int(amount)
        if type == "buy":
            while sellH and amount > 0 and sellH[0][0] <= price:
                sellPrice, sellAmount = heappop(sellH)
                if amount >= sellAmount:
                    amount = amount - sellAmount
                    res += sellAmount
                else:
                    res += amount
                    amount = 0
                    heappush(sellH, (sellPrice, sellAmount - amount))
            if amount:
                heappush(buyH, (-price, amount))
        else:
            while buyH and amount > 0 and -buyH[0][0] >= price:
                buyPrice, buyAmount = heappop(buyH)
                if amount >= buyAmount:
                    amount = amount - buyAmount
                    res += buyAmount
                else:
                    res += amount
                    amount = 0
                    heappush(buyH, (buyPrice, sellAmount - amount))
            if amount:
                heappush(sellH, (price, amount))

    return res


orders = [
    ["150", "5", "buy"],  # Order A
    ["190", "1", "sell"],  # Order B
    ["200", "1", "sell"],  # Order C
    ["100", "9", "buy"],  # Order D
    ["140", "8", "sell"],  # Order E
    ["210", "4", "buy"],  # Order F
]
print(getExecuted(orders))
