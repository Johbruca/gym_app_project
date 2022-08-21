class GymSession:
    def __init__(self, name, description, duration, id=None):
        self.name = name
        self.description = description
        self.duration = duration
        self.id = id