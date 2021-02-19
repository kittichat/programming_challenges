class Solution:
    def twoSum(self, nums ,target: int):
        i = 0
        result = 0
        a = []
        self.nums = nums
        self.target = target
        while i < len(nums):
          j = i + 1
          while j < len(nums):
            result =  nums[i] + nums[j]
            if result == target:
                a.extend((i,j))
                break
            j += 1
          if result == target:
            break
          i += 1
              
        return a

test = Solution()
x = test.twoSum([1,2,3,4],6)
print(x)