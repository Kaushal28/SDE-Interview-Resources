# SOLID Principles

- S - Single responsibility
- O - Open/Closed principle
- L - Liskov substitution
- I - Interface segregation
- D - Dependency Inversion

## 1. Single Responsibility Principle (SRP)
<p align="center"><img src="https://i.imgur.com/olWf6e1.jpg" width="550" height="550"></p>

- Any class should have only one responsibility. That also means a class should have only one reason to change. This makes classes easier to **test** and also helps **decoupling** the code.
- Example includes the objects that can print/save themselves. In such cases, it's easier to violate SRP.

```python
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title
        
    @property
    def author(self):
        return self._author

    def print_page(self):
        """Logic to print current page."""
        print(...)
```
- In the above example, adding method `print_page` to `Book` class violates the SRP because the `Book` class contains the state of the book as well as the procedure to print the page of the book. Therefore, in future, if there a change in print destination/formatting, the book class would require changes. That makes new builds bug prone and require more testing.
- To fix this, we can segregate the print/save mechanism from the `Book` class. Here is an example

```python
class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title
        
    @property
    def author(self):
        return self._author

    def get_page(self):
        """This only returns the content of current page."""
        pass


class Printer:
    def print_page(self, book: Book):
        raise NotImplementedError()


class PlainTextPrinter(Printer):
    def print_page(self, book: Book):
        print(book.get_page())


class HTMLPrinter(Printer):
    def print_page(self, book: Book):
        print(f"<html> {book.get_page()} </html>")
```
- Now these classes follow the SRP. Both `Book` and `Printer` have a single responsibility.

## 2. Open/Closed Principle [Open for Extension/Closed for Modification]
<p align="center"><img src="https://i.imgur.com/0RZcEgl.jpg" width="550" height="550"></p>

- Software entities (classes, functions, modules etc.) should be open for extension but closed for modification. In doing so, we stop ourselves from modifying existing code and causing potential new bugs.
- Entities should be designed in such a way that when a new functionality is needed, we should not modify our existing code but rather write new code that will be used by existing code.
- Consider an example of shape classes and their area calculator class.

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height


class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._redius


class AreaCalculator:
    """
    Calculates the total area from collection of objects.
    """
    def area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width * shape.height
            elif isinstance(shape, Circle):
                total_area += 3.14 * shape.radius * shape.radius
        return total_area
```

- Considering the above design, if we need to add two more shapes (e.g. triangle and hexagone), then `AreaCalculator` class must be changed. This is violating the Open/Closede principle. This design in not closed for modification. Each new requirement of adding new shape would require changes in existing code.
- To fix this, we could move the area calculation logic to respective shapes so that the `AreaCalculator` class does not require any change in case of adding new shapes in our system.

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def area(self):
        return self.height * self.width


class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._redius
    
    def area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    """
    Calculates the total area from collection of objects.
    """
    def area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area
```
- Now, in the above design, adding new shapes is very easy.

## 3. Liskov Substitution Principle (LSP)
<p align="center"><img src="https://i.imgur.com/hEYUuQN.jpg" width="550" height="550"></p>

- Liskov Substitution principle states that if `S` is a subtype of `T`, then objects of type `T` may be replaced with objects of type `S`. That also means child classes should never break the parent class' type definitions.
- Objects of child class should be used in place of parent class objects because child class should only extend the properties/behaviour of its parent and should not modify it.
- For example, deriving `Square` class from `Rectangle` violates the above definition because objects of rectangle can set it's width and height independently. So we can not replace `Rectangle` objects with `Square` objects and hence the abstraction of having `Square` inherit from `Rectangle` is a bad one.
- Here is another example: Almost all birds can fly except Ostrich. So if we define `Bird` class as following, it'll violate the LSP.

```python
class Bird:
    def fly(self):
        pass
```
- Because, if we have to define class `Ostrich`, it'll have to implement `fly()` method even if it's not required in case of `Ostrich`. So, a meaningful design which doesn't violate the LSP can be given as following:

```python
class Bird:
    pass

class FlyingBirds(Bird):
    def fly(self):
        pass

class Duck(FlyingBirds):
    def fly(self):
        pass

class Ostrich(Bird):
    pass
```

- Objects of class `Ostrich` can now be used in place of objects of class `Bird`. Same goes for classes `FlyingBirds` and `Duck`.


## 4. Interface Segregation Principle (ISP)
<p align="center"><img src="https://i.imgur.com/hTngExc.jpg" width="550" height="550"></p>

- This means that larger interfaces should be split into smaller ones. By doing so, we can ensure that implementing classes only need to be concerned about the methods that are of interest to them. Here is an example:

```python
class Bird:
    pass

class FlyingBirds(Bird):
    def fly(self):
        pass

class Duck(FlyingBirds):
    def fly(self):
        pass

class Ostrich(Bird):
    pass
```
- As `Ostrich` can't fly, there is no need to implement `fly()` method for its objects. So we segregated the interfaces for Ostrich and other birds that can fly.

## 5. Dependency Inversion Principle (DIP)
<p align="center"><img src="https://i.imgur.com/khSbeDs.jpg" width="550" height="550"></p>

---
### References:
- http://joelabrahamsson.com/a-simple-example-of-the-openclosed-principle/
- https://www.baeldung.com/solid-principles
- https://stackoverflow.com/q/56860/5353128
