class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for num in range(len(nums)):
            complement = target - nums[num]
            if complement in hashmap:
                return [num, hashmap[complement]]
            hashmap[nums[num]] = num
        return []
