# SOLID Principles

- S - Single responsibility
- O - Open/Closed principle
- L - Liskov substitution
- I - Interface segregation
- D - Dependency Inversion

## 1. Single Responsibility Principle (SRP)
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

## 2. Open/Closed principle [Open for Extension/Closed for Modification]
- Software entities (classes, functions, modules etc.) should be open for extension but closed for modification. In doing so, we stop ourselves from modifying existing code and causing potential new bugs.
- 
