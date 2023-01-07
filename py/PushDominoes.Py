# https://leetcode.com/problems/push-dominoes/

# L...L, in this case, we need to fill everything with L
# R...R, in this case, we need to fill everything with R
# L...R, we need to keep it as it is
# R...L, then we need to fill first half with R and second with L, handling odd and even cases.
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        res = ""
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            interval = j - i - 1
            if i:
                res += dominoes[i]
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * interval
            elif dominoes[i] == "L" and dominoes[j] == "R":
                res += "." * interval
            else:
                res += (
                    "R" * (interval // 2) + "." * (interval % 2) + "L" * (interval // 2)
                )
            i = j
        return res


s = Solution()
dominoes = ".L.R...LR..L.."
print(s.pushDominoes(dominoes))
