from .memory_store import MemoryStore
from .file_store import FileStore
from .kvstore_base import KVStoreBase


class Factory:
    """
    KV Store factory to instantiate storage objects.
    """

    kvstore_map: dict = {"MEMORY": MemoryStore, "FILE": FileStore}

    @staticmethod
    def get_instance(instance_type: str) -> KVStoreBase:
        """
        Instantiate given KV store class dynamically.
        :param instance_type: Type of KV store to be instantiated.
        :return: KV store object.
        """
        try:
            return Factory.kvstore_map[instance_type]()
        except KeyError:
            raise Exception("Invalid instance requested.")
