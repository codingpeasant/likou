# https://leetcode.com/problems/integer-to-english-words/description/

# Approach
# Initialization:
# Create lists for words representing numbers less than twenty and multiples of ten.
# Check for Zero:
# If the number is zero, return "Zero".
# Define Function for Two-Digit Numbers:
# If the number is less than twenty, return the corresponding word from the list.
# Otherwise, split the number into tens and ones, and return the words by combining the tens place word and the ones place word.
# Define Function for Three-Digit Numbers:
# If the number is zero, return an empty string.
# If the number is less than 100, use the two-digit function to get the word.
# Otherwise, split the number into hundreds, tens, and ones, and combine the words for hundreds, "Hundred", and the two-digit number.
# Split the Number into Billions, Millions, Thousands, and Hundreds:
# Divide the number by 1 billion, 1 million, 1 thousand, and 1 to get the respective parts.
# Build the Result String:
# Initialize an empty result string.
# For each part (billions, millions, thousands, hundreds), if the part is non-zero, convert it to words using the three-digit function and append the appropriate scale ("Billion", "Million", "Thousand").
# Ensure proper spacing between the parts.
# return res by removing the extra space


class Solution:
    def numberToWords(self, num):
        less_than_twenty = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        ten_places = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        if num == 0:
            return "Zero"

        def two_digit(num):
            if num < 20:
                return less_than_twenty[num]
            else:
                tens = num // 10
                ones = num % 10
                return ten_places[tens] + (
                    "" if ones == 0 else " " + less_than_twenty[ones]
                )

        def three_digit(num):
            if not num:
                return ""
            if not num // 100:
                return two_digit(num)
            return (
                less_than_twenty[num // 100]
                + " "
                + "Hundred"
                + (" " + two_digit(num % 100) if num % 100 else "")
            )

        billion = num // 1000000000
        million = (num // 1000000) % 1000
        thousand = (num // 1000) % 1000
        hundred = num % 1000

        res = ""
        if billion:
            res += three_digit(billion) + " Billion"

        if million:
            if res:
                res += " "
            res += three_digit(million) + " Million"

        if thousand:
            if res:
                res += " "
            res += three_digit(thousand) + " Thousand"

        if hundred:
            if res:
                res += " "
            res += three_digit(hundred)

        return res.strip()


s = Solution()
print(s.numberToWords(1234))
