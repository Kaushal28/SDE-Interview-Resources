from src.kvstores.memory_store import MemoryStore

memory_store = MemoryStore()


def test_get_item():
    """
    Test __getitem__ method.
    """
    memory_store["key1"] = "value1"
    assert memory_store["key1"] == "value1"
    assert memory_store["key2"] == ""


def test_set_item():
    """
    Test __setitem__ method.
    """
    memory_store["key1"] = "value1"
    assert "key1" in memory_store
    assert memory_store["key1"] == "value1"


def test_contains():
    """
    Test __contains__ method.
    """
    memory_store["key1"] = "value1"
    assert "key1" in memory_store
    assert "key2" not in memory_store
