# https://leetcode.com/playground/k3HaoUmm

# // A trade is defined as a fixed-width string containing the 4 properties given below separated by commas:

# // Symbol (4 alphabetical characters, left-padded by spaces)
# // Type (either "B" or "S" for buy or sell)
# // Quantity (4 digits, left-padded by zeros)
# // ID (6 alphanumeric characters)
# // e.g.
# // "AAPL,B,0100,ABC123"

# // which represents a trade of a buy of 100 shares of AAPL with ID "ABC123"

# // Given two lists of trades - called "house" and "street" trades, write code to filter out groups of matches between trades and return a list of unmatched house and street trades sorted alphabetically. There are many ways to match trades, the first and most important way is an exact match (Tests 1-5):

# // An exact match is a house_trade+street_trade pair with identical symbol, type, quantity, and ID
# // Note: Trades are distinct but not unique

# // For example, given the following input:

# // // house_trades:
# // [
# // "AAPL,B,0080,ABC123",
# // "AAPL,B,0050,ABC123",
# // "GOOG,S,0050,CDC333"
# // ]

# // // street_trades:
# // [
# // " FB,B,0100,GBGGGG",
# // "AAPL,B,0100,ABC123"
# // ]

# // We would expect the following output:

# // [
# // " FB,B,0100,GBGGGG",
# // "AAPL,B,0100,ABC123",
# // "GOOG,S,0050,CDC333"
# // ]

# // Because the first (or second) house trade and second street trade form an exact match, leaving behind three unmatched trades.

# // Follow-up 1 (Test 6,7,8,9): A "fuzzy" match is a house_trade+street_trade pair with identical symbol, type, and quantity ignoring ID. Prioritize exact matches over fuzzy matches. Prioritize matching the earliest alphabetical house trade with the earliest alphabetical street trade in case of ties.

# // Follow-up 2: (Test 10) An offsetting match is a house_trade+house_trade or street_trade+street_trade pair where the symbol and quantity of both trades are the same, but the type is different (one is a buy and one is a sell). Prioritize exact and fuzzy matches over offsetting matches. Prioritize matching the earliest alphabetical buy with the earliest alphabetical sell.

from collections import defaultdict
from typing import List, Tuple


def parse_trade(trade: str) -> Tuple[str, str, str]:
    tokens = trade.split(",")
    symbol = tokens[0]
    type_ = tokens[1]
    quantity = tokens[2]
    return symbol, type_, quantity


def exactMatch(houseTrades: list[str], streetTrades: list[str]) -> tuple[list, list]:
    houseTrades.sort()
    streetTrades.sort()
    resHouse, resStreet = [], []
    for houseT in houseTrades:
        if not houseT in streetTrades:
            resHouse.append(houseT)

    for streetT in streetTrades:
        if streetT not in houseTrades:
            resStreet.append(streetT)

    return resHouse, resStreet


def fuzzyMatch(houseTrades: list[str], streetTrades: list[str]) -> tuple[list, list]:
    houseTradesS = [parse_trade(trade) for trade in houseTrades]
    streetTradeS = [parse_trade(trade) for trade in streetTrades]

    houseTrades.sort()
    streetTrades.sort()
    resHouse, resStreet = [], []
    for houseT in houseTrades:
        if not parse_trade(houseT) in streetTradeS:
            resHouse.append(houseT)

    for streetT in streetTrades:
        if parse_trade(streetT) not in houseTradesS:
            resStreet.append(streetT)

    return resHouse, resStreet


def offsetMatch(houseTrades: list[str], streetTrades: list[str]) -> tuple[list, list]:
    houseTradesS = [parse_trade(trade) for trade in houseTrades]
    streetTradeS = [parse_trade(trade) for trade in streetTrades]

    houseTrades.sort()
    streetTrades.sort()
    resHouse, resStreet = [], []
    for houseT in houseTrades:
        parsedHouseT = parse_trade(houseT)
        found = False
        for houseTs in houseTradesS:
            if (
                parsedHouseT[0] == houseTs[0]
                and parsedHouseT[2] == houseTs[2]
                and parsedHouseT[1] != houseTs[1]
            ):
                found = True
                break
        if not found:
            resHouse.append(houseT)

    for streetT in streetTrades:
        parsedstreetT = parse_trade(streetT)
        found = False
        for streetTs in streetTradeS:
            if (
                parsedstreetT[0] == streetTs[0]
                and parsedstreetT[2] == streetTs[2]
                and parsedstreetT[1] != streetTs[1]
            ):
                found = True
                break
        if not found:
            resStreet.append(streetT)

    return resHouse, resStreet


def main():
    house_trades = [
        "AAPL,B,0100,AAA111",
        "MSFT,S,0200,BBB222",
        "AAPL,B,0100,ABC123",
        "GOOG,S,0050,CDC333",
        "   W,S,0050,CDD222",
        "   W,B,0050,DDG333",
    ]
    street_trades = [
        "AAPL,B,0100,XXX999",
        "MSFT,S,0200,YYY888",
        "AAPL,B,0100,ABC123",
        " FB,B,0100,GBGGGG",
        " FB,S,0100,FFF222",
    ]

    unmatchedHouseTrades, unmatchedStreedTrades = exactMatch(
        house_trades, street_trades
    )

    unmatchedHouseTrades, unmatchedStreedTrades = fuzzyMatch(
        unmatchedHouseTrades, unmatchedStreedTrades
    )

    unmatchedHouseTrades, unmatchedStreedTrades = offsetMatch(
        unmatchedHouseTrades, unmatchedStreedTrades
    )
    print(unmatchedHouseTrades)
    print(unmatchedStreedTrades)


if __name__ == "__main__":
    main()
