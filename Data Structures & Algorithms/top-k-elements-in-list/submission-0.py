class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for i in nums:
            counter[i] = 1 + counter.get(i, 0)
        for i, j in counter.items():
            frequency[j].append(i)

        output = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                output.append(j)
                if len(output) == k:
                    return output