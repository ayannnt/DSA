class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current = 0
        maximum = 0
        for num in nums:
            if num == 1:
                current += 1
                if current > maximum:
                    maximum = current
                  
            else:
                current = 0
        return maximum

        """
        :type nums: List[int]
        :rtype: int
        """
        