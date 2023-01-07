# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    # dp[i][j] is number of valid permutation strings length i that ends at vowel j, where 1 <= i <= n, 0 <= j <= 4.
    # state machine
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        MOD = 10**9 + 7
        for _ in range(n-1):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (i + o) % MOD
        return (a + e + i + o + u) % MOD