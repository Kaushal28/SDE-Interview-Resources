import io

from .kvstore_base import KVStoreBase


class FileStore(KVStoreBase):
    """
    Memory store, which uses 'dict' data structure to
    store the key-value pairs.
    """

    def __init__(self):
        super().__init__(open("db.txt", "a+"))

    def __getitem__(self, key: str) -> str:
        """
        Get value for the given key from dict
        :param key: Key for which the value is to be retrieved.
        :return: value
        """
        # iterate over file and search for given key.
        try:
            # move pointer to initial position in file
            self.store.seek(0, io.SEEK_SET)
            for line in self.store:
                suffix, long_url = line.split()
                if suffix == key:
                    return long_url
        except Exception as err:
            print(str(err))
        return ""

    def __setitem__(self, key: str, value: str) -> None:
        """
        Set value for the given key into dict.
        :param key: Key to be added.
        :param value: Value corresponding to the key.
        :return: None
        """
        # move pointer to the end of the file for writing.
        self.store.seek(0, io.SEEK_END)
        if self.store.tell() != 0:
            self.store.write(f"\n{key} {value}")
        else:
            self.store.write(f"{key} {value}")
        self.store.flush()

    def __contains__(self, key: str) -> bool:
        """
        Check whether the given key is present in the dict.
        :param key: Key whose presence is to be checked.
        :return: True if key is present, False otherwise.
        """
        return True if self.__getitem__(key) else False

    def __del__(self) -> None:
        """
        Free file resource.
        """
        self.store.close()
