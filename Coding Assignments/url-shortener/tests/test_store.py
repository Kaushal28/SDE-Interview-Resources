from src.utils.store_connector import StoreConnector
from src.kvstores.memory_store import MemoryStore


def test_store_singleton():
    """
    Ensure that the store is singleton and
    """
    store1 = StoreConnector().store
    store2 = StoreConnector().store

    assert isinstance(store1, MemoryStore) and isinstance(store2, MemoryStore)
    # reference test
    assert store1 is store2
