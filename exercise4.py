# Part 1
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(10)) # True
print(is_even(9))  # False
print(is_even(0))  # True

# Part 2
def wrap_text(text, wrapper):
    return wrapper + text + wrapper

print(wrap_text('hello', '==='))

print(
    wrap_text(
        wrap_text(
            wrap_text('new_message', '###'),
            '==='
        ),
        '---'
    )
)
