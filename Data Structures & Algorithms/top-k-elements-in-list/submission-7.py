class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        res = []

        for item, c in count.most_common(k):
            res.append(item)

        return res