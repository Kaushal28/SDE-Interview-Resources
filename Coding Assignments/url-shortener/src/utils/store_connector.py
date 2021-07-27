import os
import sys
from sys import stderr

from .singleton import Singleton
from ..kvstores.kvstore_factory import Factory
from ..kvstores.kvstore_base import KVStoreBase


class StoreConnector(metaclass=Singleton):
    """
    Key Value store singleton class that can be used across all modules.
    """

    def __init__(self):
        try:
            store_type = os.environ.get("STORE_TYPE", "MEMORY")
            self._store = Factory.get_instance(store_type)
        except KeyError as ex:
            print(ex, file=stderr)
            # one of the required environment variable is not set
            print(
                "One of the required environment variables is not set",
                file=stderr,
            )
            sys.exit(1)
        except Exception as ex:
            print(ex, file=stderr)
            sys.exit(1)

    @property
    def store(self) -> KVStoreBase:
        return self._store
