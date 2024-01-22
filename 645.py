class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # First sort the list
        nums.sort()
        n = len(nums)

        # Return list
        ret = []

        # If the missing one is 1
        if nums[0] != 1:
            temp = 1

        # If the missing one is the last one
        elif nums[-1] != n:
            temp = n
        for i in range(n):
            if i >0:

                # Check for repeating digit
                if nums[i] == nums[i-1]:
                    ret.append(nums[i])
                # Check for jumping, which is missing digit
                elif nums[i] > nums[i-1]+1:
                    temp = nums[i]-1
        ret.append(temp)
        return ret
# This is not a good solution, since it might be not general with this much if's
# A simple way is to count the appearance of digits, which is very very easy and intuitive,
# I wonder why I didn't consider about that...
