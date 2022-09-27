class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = dict() 
        
        for i in range(len(nums)):#2
            res = target - nums[i] #2
            if res in output: 
                return [output[res], i]
            else: 
                output[nums[i]] = i 
