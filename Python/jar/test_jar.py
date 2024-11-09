import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    jar.withdraw(3)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
