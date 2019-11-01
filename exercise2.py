def c_to_f(temp_in_c):
    return temp_in_c * 9/5 + 32

temp_in_c = int(input('Enter a temperature in Celsius: '))
print(f'The temperature in Fahrenheit is {c_to_f(temp_in_c)}')
