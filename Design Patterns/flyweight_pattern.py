# Flyweight is structural design pattern

# Flyweight is a structural design pattern that lets you fit more objects
# into the available amount of RAM by sharing common parts of state between
# multiple objects instead of keeping all of the data in each object.

# The object attributes which are constant (intrinsic attributes) are kept
# inside the object but the attributes which varies between objects of same
# class are passed to methods which requires them and hence kept outside
# of the object (extrinsic attributes).

# Consider a game creating objects for particles, missiles and guns, the
# common properties like their skin image, color etc. are common between all
# objects of same class and hence kept inside the object. Now, as attributes
# of object for a single class do not vary, we only require a single object for
# each class, which reduces memory usage drastically.

# The objects which only stores intrinsic states (constant attributes) are
# called flyweight objects.

# Note that as intrinsic attributes are used by all methods, they should be
# immutable.


from typing import Dict, List


class Flyweight:

    def __init__(self, shared_state):
        super().__init__()
        self.shared_state = shared_state
    
    def business_logic(self, unique_state):
        """
        This method has access to both shared states and unique states.
        Using all the states, flyweights act as a single object.
        """
        print(f"Shared state: {self.shared_state}")
        print(f"Unique state: {unique_state}")
    

class FlyweightFactory:

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, flyweights):
        super().__init__()
        for state in flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state: list) -> str:
        """
        Returns a unique hash for a given shared states.
        """
        return "_".join(state)
    
    def get_flyweight(self, shared_state) -> Flyweight:
        """Returns an existing flyweight creates a new one."""
        flyweight_key = self.get_key(shared_state)
        if flyweight_key not in self._flyweights:
            # Create a new flyweight
            self._flyweights[flyweight_key] = Flyweight(shared_state)
        
        return self._flyweights[flyweight_key]

    def list_flyweights(self) -> None:
        """Lists existing flyweight objects."""
        print(list(self._flyweights.keys()))


# A driver function, which combines shared and unique states 
# and executes the flyweight object's business logic. The unique
# states will be passed to this function on the fly.
# This is the crux of flyweight design pattern.
def execute_business_logic(
    factory, number_plate,
    owner, brand, model, color
) -> None:
    # Get flyweight using shared states/attributes
    flyweight = factory.get_flyweight([brand, model, color])

    # Execute the flyweight business logic
    flyweight.business_logic([number_plate, owner])


if __name__ == "__main__":
    # Initialize flyweight factory with some initial shared states
    # of various objects
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"]
    ])

    factory.list_flyweights()

    # As we can see, executing object's functionality only creates
    # new objects if required. Otherwise reuses it. This reduces
    # memory usage
    execute_business_logic(
        factory,
        "GJ01 PX 1234", "Kaushal28", "BMW", "M5", "red"
    )

    execute_business_logic(
        factory,
        "GJ01 PX 3456", "Kaushal28", "Mercedes Benz", "C300", "black"
    )


# OUTPUT:
# ['Chevrolet_Camaro2018_pink', 'Mercedes Benz_C300_black', 'Mercedes Benz_C500_red', 'BMW_M5_red', 'BMW_X6_white']
# Shared state: ['BMW', 'M5', 'red']
# Unique state: ['GJ01 PX 1234', 'Kaushal28']
# Shared state: ['Mercedes Benz', 'C300', 'black']
# Unique state: ['GJ01 PX 3456', 'Kaushal28']
