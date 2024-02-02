Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

------------------------PYTHON_SOLUTION----------------------------
  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
-------------------------JAVA_SOLUTION-----------------------------
class Solution {
        int[] twoSum(int[] nums, int target) {
          for(int i=1; i<nums.length; i++){
            if(nums[i-1] +nums[i] ==  target)
              return new int[]{i-1,i};
          }
        return new int[]{};
        }
    }
