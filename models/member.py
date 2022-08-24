class Member:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def equals(self, member):
        return member.name == self.name