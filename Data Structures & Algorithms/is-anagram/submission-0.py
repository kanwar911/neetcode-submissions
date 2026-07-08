class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1 = len(s)
        len2 = len(t)
        if (len1 != len2):
            return False

        s = sorted(s)
        t = sorted(t)
        j = 0
        for i in range(len(s)):
            if s[i] == t[j]:
                j = j + 1
                continue
            else:
                return False

        return True
                
        