from abc import ABC, abstractmethod


class ConverterBase(ABC):
    """
    Base class for any converter which provides necessary methods for
    annotation conversion.
    """

    @abstractmethod
    def load(self, annotation: dict):
        """
        Load the given annotation into python object from given dict.

        :param annotation: Annotation to be loaded.
        :return: Annotation object.
        """
        pass

    @abstractmethod
    def convert(self, annotation):
        """
        Convert one annotation format to another.

        :param annotation: annotation to be converted.
        :return: Resulting annotation string.
        """
        pass

    @abstractmethod
    def to_str(self, annotation) -> str:
        """
        Reverse of "load()". Converts the given annotation object to string.

        :param annotation: Annotation object to be converted to string.
        :return: Annotation string.
        """
        pass
