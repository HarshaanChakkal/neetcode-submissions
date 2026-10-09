class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,4,4,3,3,3] k = 2
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort() # [[1, 1], [2, 4], [3, 3]]

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res