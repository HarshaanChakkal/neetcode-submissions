class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = [[6,7], [1,3],[1,5]]
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals: # start = 6, end = 7
            lastEnd = output[-1][1]
            if start > lastEnd:
                output.append([start, end])
            else:
                output[-1][1] = max(end, lastEnd)
        return output