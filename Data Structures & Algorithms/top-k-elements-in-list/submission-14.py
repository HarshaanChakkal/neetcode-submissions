class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
            # 1 : 1, 2 : 2, 3 : 3
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num]) # [[1, 1], [2, 2], [3, 3]]
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
