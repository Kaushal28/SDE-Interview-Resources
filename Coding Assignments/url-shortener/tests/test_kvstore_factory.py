import pytest

from src.kvstores.kvstore_factory import Factory
from src.kvstores.memory_store import MemoryStore
from src.kvstores.file_store import FileStore


def test_factory():
    """
    Test kv store object instantiation based on given type.
    """
    isinstance(Factory.get_instance("MEMORY"), MemoryStore)
    isinstance(Factory.get_instance("FILE"), FileStore)
    with pytest.raises(Exception):
        Factory.get_instance("INVALID")
