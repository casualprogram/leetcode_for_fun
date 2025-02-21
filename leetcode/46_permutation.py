class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        subSet = [[]]
        # for each number in the list
        for num in nums:
            # create a new set
            currSet = []
            # for each subset in the current set
            for eachSub in subSet:
                print("\n current num ", num)
                print("eachSub this set", eachSub)
                # for each position in the subset
                for position in range(len(eachSub)+1):
                    print("\n\t- position this time", position)
                    tempSet = eachSub.copy()
                    print("\t- tempSet this time", tempSet)
                    tempSet.insert(position, num)
                    print("\t- tempSet after insert", tempSet)
                    currSet.append(tempSet)
                print("currSet add tempSet", currSet)
            subSet = currSet
        return subSet