class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._rec_search(0, len(nums)-1, nums, target)
    def _rec_search(self, left, right, nums, target):
        if left > right:
            return -1
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self._rec_search(mid+1, right, nums, target)
        else:
            return self._rec_search(left, mid - 1, nums, target)
        
        
        
