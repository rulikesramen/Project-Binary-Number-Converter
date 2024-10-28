def decimalToBinary(num):
  """
  Converts a decimal number to a 4-bit binary string.

  Args:
    num: The decimal number to convert.

  Returns:
    A 4-bit binary string representation of the decimal number.
  """

  if 0 <= num <= 15:
    binary = bin(num)[2:].zfill(4)
    print(binary)
  else:
    print("Input number should be between 0 and 15.")


def binaryToDecimal(binary_string):
  """
  Converts a binary string to a decimal number.

  Args:
    binary_string: The binary string to convert.

  Returns:
    The decimal representation of the binary string.
  """

  if len(binary_string) == 4:
    decimal = int(binary_string, 2)
    print(decimal)
  else:
    print("Input binary string should be 4 bits long.")

decimalToBinary(9) # Output: 1001
decimalToBinary(0) # Output: 0000
decimalToBinary(15) # Output: 1111

binaryToDecimal("1001") # Output: 9
binaryToDecimal("0000") # Output: 0
binaryToDecimal("1111") # Output: 15
