class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # visit each word
    # create a shared identity,add all matching to the list of that identity key
    # return the grouped list
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                compute = ord(c)-ord('a')
                count[compute] +=1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())