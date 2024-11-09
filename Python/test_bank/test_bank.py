from bank import value
def main():
    test_return_zero()
    test_h()
    test_no_h()
def test_return_zero():
    assert value("hello gi") == 0
    assert value("Hello") == 0
    assert value("Hello Gi") == 0
def test_h():
    assert value("How are you") == 20
    assert value("Hi") == 20
    assert value("hey") == 20
def test_no_h():
    assert value("What’s up") == 100
if __name__ == "__main__":
    main()

