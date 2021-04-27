# Facade is structural design pattern

# Facade means front of the building. It hides building's structural
# complexities and shows simple building view. Similarly, in software,
# it provides simplified (but limited) interface to a complex system of
# classes, library or framework.

# $ in jquery is an example of facade pattern.
# https://stackoverflow.com/a/5242476/5353128

class CPU:
    """Complex CPU implementation."""
    def freeze(self):
        pass

    def jump(self):
        pass

    def execute(self):
        pass


class Memory:
    """RAM implementation."""

    def load(self):
        pass


class HDD:
    """Hard disk implementation."""

    def read(self):
        pass

    def load(self):
        pass


class ComputerFacade:
    """
    A computer facade which hides the complex details of computer
    implementation and provides users a easy to use interface which
    interacts with computer.

    This decouples the client code from library code
    (computer in this case).
    """
    
    def __init__(self):
        super().__init__()
        self.cpu = CPU()
        self.memory = Memory()
        self.hdd = HDD()
    
    def start(self):
        """
        This method actually interacts with library code and provide
        an abstraction.
        """
        self.cpu.freeze()
        self.memory.load()
        self.cpu.jump()
        self.cpu.execute()


if __name__ == "__main__":
    computer = ComputerFacade()
    # Using facade, starting computer is now easier. If there are
    # any changes in process of starting computer, it can be
    # incorporated in facade without changing client code.
    computer.start()
