from .kvstore_base import KVStoreBase


class MemoryStore(KVStoreBase):
    """
    Memory store, which uses 'dict' data structure to
    store the key-value pairs.
    """

    def __init__(self):
        super().__init__(dict())

    def __getitem__(self, key: str) -> str:
        """
        Get value for the given key from dict
        :param key: Key for which the value is to be retrieved.
        :return: value
        """
        return self.store.get(key, "")

    def __setitem__(self, key: str, value: str) -> None:
        """
        Set value for the given key into dict.
        :param key: Key to be added.
        :param value: Value corresponding to the key.
        :return: None
        """
        self.store[key] = value

    def __contains__(self, key: str) -> bool:
        """
        Check whether the given key is present in the dict.
        :param key: Key whose presence is to be checked.
        :return: True if key is present, False otherwise.
        """
        return True if key in self.store else False
