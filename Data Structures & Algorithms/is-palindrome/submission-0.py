class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers
        # strip all the space from the string, convert to lowercase
        # one at start, other at end
        # keep comparing for == and rt bool
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()

        length = len(clean)
        start = 0
        last = length - 1
        while start < last:
            if clean[start] == clean[last]:
                start += 1
                last -= 1
            else:
                return False
        return True

        