class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        countS = defaultdict(int)
        need = len(countT)
        have = 0
        left = 0
        smallest = ""
        smallestLength = float("inf")

        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] += 1
                
                if countS[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                windowLength = r - left + 1

                if windowLength < smallestLength:
                    smallestLength = windowLength
                    smallest = s[left:r + 1]

                if s[left] in countT:
                    countS[s[left]] -= 1

                    if countS[s[left]] < countT[s[left]]:
                        have -= 1

                left += 1

        return smallest