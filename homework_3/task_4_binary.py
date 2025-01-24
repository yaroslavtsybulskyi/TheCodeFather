class BinaryNumber:
    """
    Binary number class that represents a binary number.
    """

    def __init__(self, value: str):
        """
        Constructor for binary number.
        :param value: value of the binary number.
        """
        if not all(bit in '01' for bit in value):
            raise ValueError('Invalid binary value')
        self.value = value

    def __and__(self, other):
        """
        And operator for binary number.
        :param other: other binary number.
        :return: result of the operation.
        """
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)

        result = ''.join('1' if a[i] == '1' and b[i] == '1' else '0' for i in range(max_len))
        return BinaryNumber(result)

    def __or__(self, other):
        """
        Or operator for binary number.
        :param other: other binary number.
        :return: result of the operation.
        """
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)

        result = ''.join('1' if a[i] == '1' or b[i] == '1' else '0' for i in range(max_len))
        return BinaryNumber(result)

    def __xor__(self, other):
        """
        Xor operator for binary number.
        :param other: other binary number.
        :return: result of the operation.
        """
        max_len = max(len(self.value), len(other.value))
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)

        result = ''.join('1' if a[i] != b[i] else '0' for i in range(max_len))
        return BinaryNumber(result)

    def __invert__(self):
        """
        Invert operator for binary number.
        :return: inverted binary number.
        """
        result = ''.join('1' if self.value[i] == '0' else '0' for i in range(len(self.value)))
        return BinaryNumber(result)

    def __repr__(self) -> str:
        """String representation for binary number."""
        return self.value
