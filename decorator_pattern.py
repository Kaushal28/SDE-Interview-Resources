# Decorator is a structural design pattern.

# Decorator pattern is used when the behaviour of a single or multiple
# class objects is required be extended (not all class objects, otherwise
# this can be done using subclass). It creates a wrapper like structure,
# which wraps new functionalities over existing functionalities of the object
# at run time (dynamically). https://stackoverflow.com/a/1549777/5353128

# One example where this pattern can be used is for extending the behaviour of
# any third party library class objects without modifying library itself.

# It satisfies "O" from SOLID principles.


class Pizza:

    def __init__(self):
        super().__init__()
        self.price = 250

    def get_cost(self) -> int:
        return self.price
    
    def show_pizza(self) -> None:
        print("==========")
        print()

# Pizza variants
class PeppyPaneer(Pizza):

    def __init__(self, pizza: Pizza):
        super().__init__()
        self.pizza = pizza
    
    def get_cost(self) -> int:
        return self.pizza.get_cost() + 100
    
    def show_pizza(self) -> None:
        print("##########")
        self.pizza.show_pizza()


class Cheese(Pizza):

    def __init__(self, pizza: Pizza):
        super().__init__()
        self.pizza = pizza
    
    def get_cost(self):
        return self.pizza.get_cost() + 150
    
    def show_pizza(self):
        print("~~~~~~~~~~")
        self.pizza.show_pizza()


if __name__ == "__main__":
    # Simple pizza
    pizza_base = Pizza()

    print(f"{type(pizza_base).__name__}: Cost: {pizza_base.get_cost()}")
    pizza_base.show_pizza()

    # peppy paneer only
    peppy_paneer = PeppyPaneer(pizza_base)
    print(f"{type(peppy_paneer).__name__}: Cost: {peppy_paneer.get_cost()}")
    peppy_paneer.show_pizza()

    # peppy paneer with cheese
    peppy_paneer_cheese = Cheese(peppy_paneer)
    print(f"{type(peppy_paneer_cheese).__name__}: Cost: {peppy_paneer_cheese.get_cost()}")
    peppy_paneer_cheese.show_pizza()

    # Double cheese pizza!!
    double_cheese = Cheese(Cheese(pizza_base))
    print(f"{type(double_cheese).__name__}: Cost: {double_cheese.get_cost()}")
    double_cheese.show_pizza()
    
