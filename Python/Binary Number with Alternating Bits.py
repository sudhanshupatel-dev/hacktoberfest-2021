# Time-complexity - O(n) | | Space-complexity - O(1)

def hasAlternatingBits(n):

    binary_digits = bin(n)[2:]  # [2:] Strip "0b" from binary representation

    count = 0

    for digit in binary_digits:
        count = (count + 1) % 2

        if int(digit) != count:
            return False

    return True


# Testcase
assert hasAlternatingBits(5) == True
assert hasAlternatingBits(7) == False
assert hasAlternatingBits(11) == False
assert hasAlternatingBits(10) == True
assert hasAlternatingBits(3) == False
