class Card:
    def __init__(self, prefix, letter, count):
        self.prefix = prefix
        self.letter = letter
        self.count = count


def find_valid_hands(deck: list):

    res = []
    n = len(deck)

    def isValid(hand: list[Card]):
        prefixes, letters, counts = set(), set(), set()
        for card in hand:
            prefixes.add(card.prefix)
            letters.add(card.letter)
            counts.add(card.count)

        if len(prefixes) == 2 or len(letters) == 2 or len(counts) == 2:
            return False

        return True

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if isValid(
                    [
                        Card(deck[i][0], deck[i][1], len(deck[i][1:])),
                        Card(deck[j][0], deck[j][1], len(deck[j][1:])),
                        Card(deck[k][0], deck[k][1], len(deck[k][1:])),
                    ]
                ):
                    res.append([deck[i], deck[j], deck[k]])

    return res


deck = ["-A", "-B", "-BB", "+C", "-C", "-CC", "=CCC"]
valid_hands = find_valid_hands(deck)

for hand in valid_hands:
    print(hand)
