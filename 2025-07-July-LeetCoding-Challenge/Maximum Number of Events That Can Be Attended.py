import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()  # Sort by start day
        event_count = 0
        min_heap = []
        day = 0
        i = 0
        n = len(events)

        while i < n or min_heap:
            # If heap is empty, jump to next available event's start day
            if not min_heap:
                day = events[i][0]

            # Add all events starting today to the heap
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])  # store end day
                i += 1

            # Remove events that have already expired
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                event_count += 1
                day += 1  # Move to the next day

        return event_count
