class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)
        max = 0
        for i in range(1, n + 1):
            temp = 0
            for j in range(1, i + 1):
                temp += j * satisfaction[i - j]
            if temp > max:
                max = temp
        return max
