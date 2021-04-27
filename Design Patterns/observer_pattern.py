# Observer pattern is a behavioral design pattern.

# Observer pattern is used when the change in state of one object is
# required to be accessed by other objects. One example where this
# pattern fits is GUI components like buttons (subject) and their
# onClick listeners (observer).


from __future__ import annotations
from typing import List


class Subject:
    """
    Abstract Subject class, which produces data.
    For example GUI component like button.
    """

    def __init__(self):
        super().__init__()
        self.observers: List[Observer] = []
        self.state: int = 0

    def register(self, observer: Observer) -> None:
        """Register an observer to the subject."""
        raise NotImplementedError()
    
    def unregister(self, observer: Observer) -> None:
        """Unregister an observer from the subject."""
        raise NotImplementedError()
    
    def notify(self) -> None:
        """Notify the event to all registered observers."""
        raise NotImplementedError()


# Concrete Subject implementation
class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies
    observers when the state changes.
    """

    def __init__(self):
        super().__init__()
    
    def register(self, observer: Observer) -> None:
        """Register an observer to the subject."""
        self.observers.append(observer)
    
    def unregister(self, observer: Observer) -> None:
        """Unregister an observer from the subject."""
        self.observers.remove(observer)
    
    def notify(self) -> None:
        """Notify the event to all registered observers."""
        for observer in self.observers:
            observer.update(self.state)

    def business_logic(self) -> None:
        """
        Some action which actually triggers the update.
        For example button click.
        """
        self.state += 1
        self.notify()


class Observer:
    """
    Abstract observer class which requires the state changes
    information from the subject it is registered to.
    """
    def update(self, state: int) -> None:
        """Recieves update from the subject."""
        raise NotImplementedError()


class ConcreteObserverA(Observer):
    def update(self, state: int) -> None:
        print(f"{type(self).__name__}: New state: {state}")


class ConcreteObserverB(Observer):
    def update(self, state: int) -> None:
        print(f"{type(self).__name__}: New state: {state}")


if __name__ == "__main__":
    subject = ConcreteSubject()
    
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.register(observer_a)
    subject.register(observer_b)

    subject.business_logic()

    subject.unregister(observer_a)

    subject.business_logic()


# OUTPUT:
# ConcreteObserverA: New state: 1
# ConcreteObserverB: New state: 1
# ConcreteObserverB: New state: 2
