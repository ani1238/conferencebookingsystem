from SearchStrategy import SearchStrategy


class CapacitySearchStrategy(SearchStrategy):
    def __init__(self, min_capacity):
        self.min_capacity = min_capacity

    def search(self, rooms):
        results = []
        for room in rooms:
            if room.get_capacity() >= self.min_capacity:
                results.append(room)
        return results
