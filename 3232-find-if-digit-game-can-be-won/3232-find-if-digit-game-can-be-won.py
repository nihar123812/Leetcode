class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        count1 = 0
        count2 = 0
        for i in range(0,len(nums)):
            if nums[i]>9:
                count1+=nums[i]
            else:
                count2+=nums[i]
        if count1>count2 or count2>count1:
            return True
        else:
            return False