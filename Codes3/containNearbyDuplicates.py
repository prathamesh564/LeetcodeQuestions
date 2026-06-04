class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         numb = set()
         for i , num in enumerate(nums):
            if num in numb:
                return True
            numb.add(num)     
            if len(numb)>k:
                numb.remove(nums[i-k])
         return False
