class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # One outer-loop anchor creates one current group.
    #The inner loop adds all matching words to that group.
    #Only after the inner loop ends do you append the group to the final result.
        grlist = []
        processed = set()

        for i in range(len(strs)):
            if i in processed:
                continue
            
            anchor = strs[i]
            currGroup = [anchor]
            processed.add(i)

            for j in range(i + 1, len(strs)):
                if j in processed:
                    continue
                candidate = strs[j]

                if len(anchor) == len(candidate) and sorted(anchor) == sorted(candidate):
                    currGroup.append(candidate)
                    processed.add(j)
            
            grlist.append(currGroup)
        return grlist
                