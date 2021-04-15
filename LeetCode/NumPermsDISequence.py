class Solution:
    def numPermsDISequence(self, S):
        cases = [1 for _ in range(len(S) + 1)]
        for c in S:
            if c == "D":
                for i in range(1, len(cases) - 1):
                    cases[i] += cases[i - 1]
                del cases[-1]
            else:
                for i in range(len(cases) - 2, 0, -1):
                    cases[i] += cases[i + 1]
                del cases[0]
        return cases[0] % (10 ** 9 + 7)


