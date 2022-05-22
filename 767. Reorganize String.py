class Solution:
    def reorganizeString(self, s: str) -> str:
        d = collections.Counter(s)
        maxHeap = [(-cnt, char) for char, cnt in d.items()]
        res = ""
        heapq.heapify(maxHeap)
        prev = None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ''
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, char)
        return res
        
