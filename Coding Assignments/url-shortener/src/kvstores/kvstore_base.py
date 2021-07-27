from abc import ABC, abstractmethod


class KVStoreBase(ABC):
    """
    Base key-value store class that provides abstract methods required for
    any storage mechanism used to store shortened URLs.
    """

    def __init__(self, store):
        """
        Constructor.

        :param store: Object of any storage mechanism.
        """
        self.store = store

    @abstractmethod
    def __getitem__(self, key: str) -> str:
        pass

    @abstractmethod
    def __setitem__(self, key: str, value: str) -> None:
        pass

    @abstractmethod
    def __contains__(self, key: str) -> bool:
        pass
