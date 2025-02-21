from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the list
        candidates.sort()
        currSet, subSet = [], []
        # call the helper function
        self.helper(candidates, target, 0, currSet, subSet)
    
        return subSet
    
    # helper function to recursively find the subset
    def helper(self,candi, target, i, currSet, subSet):
        # if the index is greater than the length of the list
        if i >= len(candi):
            # if the sum of the current set is equal to the target
            if sum(currSet) == target and currSet not in subSet:
                subSet.append(currSet.copy())
            return
        
        currSet.append(candi[i])
        self.helper(self,candi, target, i+1, currSet, subSet)
        currSet.pop()
        self.helper(self,candi, target, i+1, currSet, subSet)
