from main import add


def test_add():
    assert add(3, 8.0)["total"] == 11
    assert add(-5, 3)["total"] == -2
    assert add(0, 0)["total"] == 0
