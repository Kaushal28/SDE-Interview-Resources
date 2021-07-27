"""Provides the singleton metaclass."""


class Singleton(type):
    """The singleton metaclass."""

    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        """Override to create only one instance ever.

        Returns:
            objet: Instance of the class initialized.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
