class Solution:

    def encode(self, strs: List[str]) -> str:
    #lengthword#lengthword 5#hello2#go
        result = ""
        for s in strs:
            length = len(s)
            result = result+str(length)+"#"+s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            wordStart = j + 1
            wordEnd = wordStart + length
            result.append(s[wordStart:wordEnd])

            i = wordEnd

        return result
             
        

