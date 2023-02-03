#Recursion

def multiple_recursion(number1, number2):
    if number2 > 0:
        print(number1, number2)
        return number1 + multiple_recursion(number1, number2-1)
    else:
        return 0

def find_largest_digit_in_number(number, max):
    last_digit = number % 10
    number = (number - last_digit) // 10
    if number == 0:
        if max > 0:
            return max
        else:
            return last_digit
    else:
        if max > last_digit:
            return find_largest_digit_in_number(number, max)
        else:
            return find_largest_digit_in_number(number, last_digit)

def x_to_power_of_y(x,y):
    if y >0:
        return x * x_to_power_of_y(x,y-1)
    else:
        return 1