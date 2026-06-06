from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        return len(heap)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(sol.minMeetingRooms([[7,10],[2,4]]))
