# Your task is to implement a function solution(key), which takes a string key and returns an encoded 5 × 5 matrix.

# The encoding happens in the following way: the initial letters in the matrix are the unique characters of the given string converted to upper case and in the order in which they appear, which then followed by the remaining letters of the English alphabet in order (except "J" is replaced by "I" to fit in the 5 × 5 matrix).

# Example

# For key = "Instacart", the output should be
# [
# ["I", "N", "S", "T", "A"],
# ["C", "R", "B", "D", "E"],
# ["F", "G", "H", "K", "L"],
# ["M", "O", "P", "Q", "U"],
# ["V", "W", "X", "Y", "Z"]
# ]


def solution(key: str):
    key = key.upper().replace("J", "I")
    seen = set()
    result = []

    # Step 1: Add unique characters from key
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            result.append(ch)

    # Step 2: Add remaining letters of the alphabet
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Note: J is skipped
        if ch not in seen:
            result.append(ch)

    # Step 3: Build the 5x5 matrix
    matrix = [result[i : i + 5] for i in range(0, 25, 5)]
    return matrix


def reverseKey(matrix: list[list]):
    flat = [char for row in matrix for char in row]
    # Map I and J both to I (because original key would have treated J as I)
    used = set()
    key_chars = []

    for ch in flat:
        # Treat J and I the same
        normalized = "I" if ch == "J" else ch
        if normalized not in used:
            used.add(normalized)
            key_chars.append(normalized)

    # Reconstruct the key from these characters
    return "".join(key_chars)


key = "ABCDEFGHIKLMNOPQRS"
matrix = solution(key)
for row in matrix:
    print(row)

print(reverseKey(matrix))
