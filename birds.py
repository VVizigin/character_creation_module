class Bird:

    name: str
    size: str

    def __init__(self, name: str, size: str):
        self.name = name
        self.size = size

    def describe(self):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    ...


class Penguin(Bird):
    ...
