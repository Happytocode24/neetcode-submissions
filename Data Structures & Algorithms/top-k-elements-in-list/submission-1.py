from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=[]
        freq=defaultdict(int)
        for i in nums:
            freq[i]=freq[i]+1
        # print(freq)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1])
        l=len(freq)-1
        l = len(sorted_freq) - 1

        while l >= 0 and k > 0:
            arr.append(sorted_freq[l][0])
            l -= 1
            k -= 1

        return arr
        