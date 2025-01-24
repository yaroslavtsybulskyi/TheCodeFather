from homework_3.task_4_binary import BinaryNumber

b1 = BinaryNumber('0011')
b2 = BinaryNumber('0010')


def test_and():
    assert str(b1 & b2) == '0010', f"Expected 0010, but got {str(b1 & b2)}"


def test_or():
    assert str(b1 | b2) == '0011', f"Expected 0011, but got {str(b1 | b2)}"


def test_xor():
    assert str(b1 ^ b2) == '0001', f"Expected 0001, but got {str(b1 ^ b2)}"


def test_not():
    assert str(~b1) == '1100', f"Expected 1100, but got {str(~b1)}"
