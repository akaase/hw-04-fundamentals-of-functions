# Part 1
def double(my_number):
    return my_number * 2

print(double(3))

# Part 2
def negative(num):
    if num >= 0:
        return False
    else:
        return True

print(negative(10))  # False
print(negative(0))   # False
print(negative(-10)) # True

# Part 3
def is_long(word):
    if len(word) < 8:
        return False
    else:
        return True

print(is_long('programming')) # True
print(is_long('birthday'))    # True
print(is_long('cat'))         # False
