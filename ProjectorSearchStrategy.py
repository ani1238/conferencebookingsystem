from SearchStrategy import SearchStrategy


class ProjectorSearchStrategy(SearchStrategy):
    def __init__(self, has_projector):
        self.has_projector = has_projector

    def search(self, rooms):
        results = []
        for room in rooms:
            if room.has_projector() == self.has_projector:
                results.append(room)
        return results
