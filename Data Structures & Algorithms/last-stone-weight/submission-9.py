class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-i for i in stones]
        heapq.heapify(max_heap)
        print(f"Before loop:", max_heap)
        print("- - - - - - - - - - - - - -")
        while len(max_heap)>1:
            print("Inside loop:-")
            first = heapq.heappop(max_heap)
            print(f"first:",first)
            second = heapq.heappop(max_heap)
            print(f"second:",second)
            print(max_heap)
            if second>first:
                print(f"second {second} > first {first}, {first} + {-second}=", first - second)
                heapq.heappush(max_heap, first-second)
            print(max_heap)
        
        print(f"Outside loop:", max_heap)
        max_heap.append(0)
        print(max_heap)
        return abs(max_heap[0])