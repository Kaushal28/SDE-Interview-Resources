# Factory pattern is a creational design pattern.

# Factory pattern is used when the library/API provides multiple classes
# and the user/client of that library wants to initialize it dynamically.
# Factory creates and returns objects dynamically based on client's
# requirements.

# It hides the details required for object creation from the client.
# It achieves decoupling between core logic/library and its client.

class BaseLibraryClass:
    """
    Base library class which is abstraction of
    library's business logic.
    """
    def business_logic(self) -> None:
        raise NotImplementedError()


class LibraryClassA(BaseLibraryClass):
    def business_logic(self):
        print(f"Executing business logic of: {type(self).__name__}")


class LibraryClassB(BaseLibraryClass):
    def business_logic(self):
        print(f"Executing business logic of: {type(self).__name__}")


class Factory:

    # If new classes are added in library, add them in this map.
    # So there won't be ANY change in the clients implementing
    # library's functionalities.
    type_map = {
        "A": LibraryClassA,
        "B": LibraryClassB
    }

    @staticmethod
    def get_instance(instance_type: str) -> BaseLibraryClass:
        try:
            return Factory.type_map[instance_type]()
        except KeyError:
            # Create custom exception if required
            raise Exception("Invalid instance requested.")
            

class Client:
    """
    Client using the above library exposed classes.
    """
    
    def client_business_logic(self, instance_type: str) -> None:
        instance = Factory.get_instance(instance_type)
        instance.business_logic()


if __name__ == "__main__":
    client = Client()

    client.client_business_logic("A")
    client.client_business_logic("B")


# OUTPUT:
# Executing business logic of: LibraryClassA
# Executing business logic of: LibraryClassB
