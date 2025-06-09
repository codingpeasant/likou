class StreamingPalindromeChecker:
    """
    Real-time palindrome checker for a growing string using a single rolling hash.
    """
    def __init__(self, base: int = 131, mod: int = 10**9+7):
        self.base = base
        self.mod = mod
        self.fwd_hash = 0
        self.rev_hash = 0
        self.power = 1  # base^size

    def append(self, c: str) -> None:
        val = ord(c)
        self.fwd_hash = (self.fwd_hash * self.base + val) % self.mod
        self.rev_hash = (self.rev_hash + val * self.power) % self.mod
        self.power = (self.power * self.base) % self.mod

    def is_palindrome(self) -> bool:
        return self.fwd_hash == self.rev_hash

# Example usage
if __name__ == "__main__":
    stream = StreamingPalindromeChecker()
    inputStream = "A man, a plan, a canal: Panama"
    for i, ch in enumerate(inputStream):
        if ch.isalnum():
            stream.append(ch.lower())
            print(inputStream[:i+1], stream.is_palindrome())