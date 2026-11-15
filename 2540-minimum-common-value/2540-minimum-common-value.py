
class Solution:
    def getCommon(self, m: list[int], n: list[int]) -> int:
        a = len(m)
        b = len(n)

        i = 0
        j = 0

        while i < a and j < b:
            if m[i] == n[j]:
                return m[i]
            elif m[i] < n[j]:
                i += 1
            else:
                j += 1

        return -1
