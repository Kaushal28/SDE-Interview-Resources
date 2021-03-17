# Abstract factory is creational pattern.

# It's factory of factories. https://stackoverflow.com/a/1001803/5353128


class AbstractFactory:

    def get_instance(self, type):
        raise NotImplementedError()

# Concrete implementation of abstract factory class.
class DogFactory(AbstractFactory):
    type_map = {
        "bulldog": BullDog,
        "husky": Husky
    }

    def get_instance(self, instance_type):
        try:
            return self.type_map[instance_type]()
        except KeyError:
            # Create custom exception if required
            raise Exception("Invalid instance requested.")


class CatFactory(AbstractFactory):
    type_map = {
        "bengalcat": BengalCat,
        "persiancat": PersianCat
    }

    def get_instance(self, instance_type):
        try:
            return self.type_map[instance_type]()
        except KeyError:
            # Create custom exception if required
            raise Exception("Invalid instance requested.")


class Dog:
    def bark(self):
        raise NotImplementedError()

class Cat:
    def meow(self):
        raise NotImplementedError()


class BullDog(Dog):
    def bark(self):
        print("Hav Hav!")


class Husky(Dog):
    def bark(self):
        print("Woof Woof!")


class BengalCat(Cat):
    def meow(self):
        print("meow!")


class PersianCat(Cat):
    def meow(self):
        print("MEOW!")
