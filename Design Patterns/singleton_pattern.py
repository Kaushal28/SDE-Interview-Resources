# Singleton is the simplest object creational design pattern.

# Singleton design pattern is used when only one instance of any class
# is required across the entire application. For example, there should
# be only one instance of database connection class across the application.


# Singleton metaclass. In Python, metaclass is class of class.
# So classes are instances of metaclass in python.
class Singleton(type):

    _instances = {}

    # __call__ in called when object of class is called
    # (https://stackoverflow.com/a/9663601/5353128). As classes
    # are object on metaclass, when class is initialized, it's a 
    # call to object of metaclass, so this method will be called.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DBConnection(metaclass=Singleton):
    """Any class which is required to be singleton."""
    def __init__(self):
        super().__init__()
        # Establish connection here.
        # ...


if __name__ == "__main__":
    db1 = DBConnection()
    db2 = DBConnection()

    print(db1 is db2)


# OUTPUT:
# True
