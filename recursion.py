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

def check_prime(start):
    def is_prime(start, number):
        if number == 1:
            return True
        elif start % number == 0 and start != number:
            return False
        else:
            return is_prime(start, number-1)

    return is_prime(start, start-1)

def gcd_recursion(number1, number2):
    def gcd_check(number1, number2, gcd):
        if number1 % gcd == 0 and number2 % gcd == 0:
            return gcd
        else:
            return gcd_check(number1, number2, gcd-1)
    if number1 > number2:
        number1, number2 = number2, number1
    return gcd_check(number1, number2, number2-1)

print(gcd_recursion(24,54))