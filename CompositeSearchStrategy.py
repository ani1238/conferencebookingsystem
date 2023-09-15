from SearchStrategy import SearchStrategy


class CompositeSearchStrategy(SearchStrategy):
    def __init__(self, *strategies):
        self.strategies = strategies

    def search(self, rooms):
        results = list(rooms)
        for strategy in self.strategies:
            results = strategy.search(results)
        return results
