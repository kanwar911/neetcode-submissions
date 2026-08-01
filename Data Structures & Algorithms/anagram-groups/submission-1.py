class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # visit each word
    # create a shared identity,add all matching to the list of that identity key
    # return the grouped list
        res = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        
                 