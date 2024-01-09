class Package:
    def __init__(self, name, version, path):
        self.name = name
        self.version = version
        self.path = path

    def __str__(self):
        return self.name + " " + self.version + " " + self.path

