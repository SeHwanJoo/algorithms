class Solution:
    def countVowelStrings(self, n: int) -> int:
        return cal(n, 0)


def cal(i: int, j: int) -> int:
    if i == 1:
        return 5 - j
    else:
        result = 0
        for index in range(5 - j):
            result += cal(i - 1, 4 - index)
        return result