class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closestNum = 999999999
        for number in nums:
            if(abs(number) < abs(closestNum)):
                closestNum = number
            elif(abs(number) == abs(closestNum)):
                if(number > closestNum):
                    closestNum = number
        
        return closestNum
