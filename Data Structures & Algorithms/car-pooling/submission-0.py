class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for numPassengers, start, end in trips:
            events.append((start, numPassengers))
            events.append((end, -numPassengers))
        events.sort()


        current = 0
        for loc, change in events:
            current += change
            if current > capacity:
                return False

        return True