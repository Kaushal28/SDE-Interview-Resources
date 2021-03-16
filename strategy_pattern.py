# Strategy is a behavioral design pattern.

# Strategy design pattern is used when there are multiple approaches or
# strategies or algorithms for performing a same tasks in various situations.

# For example, consider a website, which shows graphics based on the device
# type it's loaded on (mobile/desktop). Then rendering on mobile and desktop
# are two strategies which will be used by the core application. Core app.
# wouldn't aware of rendering stratagies. It'd just use a single "context" object
# which contains the appropriate rendering mechanism based on device.

# Using this, we could achieve loose coupling between core app. logic and 
# business logic (rendering in this case). When a new stratagy is added 
# (e.g. for rendering on tablets), the core app. code would not required to
# be changed.


from __future__ import annotations

# Context class, which switches between strategies based on requirements.
class Context:

    def __init__(self, strategy: Strategy):
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.

        This object is an appropriate strategy to be executed based on some
        conditions (e.g. device type).
        """
        super().__init__()
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy abstract class.
        """
        return self._strategy
    
    @strategy.setter
    def stratagy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy
    
    def execute_strategy(self) -> None:
        """
        Implementation of some business logic (e.g. graphic rendering)
        Which will be executed by the core application logic.
        """
        print(f"Executing {self.stratagy.execute()}...")


class Strategy:
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm/strategy.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    def execute(self):
        """
        Actual code for execution of any strategy/algorithm
        (e.g. rendering graphic)
        """
        raise NotImplementedError()


# Concrete Strategy implementations.

# e.g. Render graphic on mobile screen
class StrategyA(Strategy):
    def execute(self) -> str:
        return type(self).__name__


# e.g. Render graphic on desktop screen 
class StrategyB(Strategy):
    def execute(self) -> str:
        return type(self).__name__


if __name__ == "__main__":
    context = Context(StrategyA())
    context.execute_strategy()

    context = Context(StrategyB())
    context.execute_strategy()


# OUTPUT:
# Executing StrategyA...
# Executing StrategyB...
