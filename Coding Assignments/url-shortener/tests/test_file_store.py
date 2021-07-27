from src.kvstores.file_store import FileStore

file_store = FileStore()


def test_get_item():
    """
    Test __getitem__ method.
    """
    file_store["key1"] = "value1"
    assert file_store["key1"] == "value1"
    assert file_store["key2"] == ""


def test_set_item():
    """
    Test __setitem__ method.
    """
    file_store["key1"] = "value1"
    assert "key1" in file_store
    assert file_store["key1"] == "value1"


def test_contains():
    """
    Test __contains__ method.
    """
    file_store["key1"] = "value1"
    assert "key1" in file_store
    assert "key2" not in file_store
