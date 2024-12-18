def check_rightmost_set_bit(number):

  if number & 1 == 1:
    return True
  else:
    return False

number = int(input("Enter a number: "))
result = check_rightmost_set_bit(number)
print(f"Rightmost set bit in {number} is 1: {result}")