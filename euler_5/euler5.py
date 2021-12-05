#Euler 5
from math import gcd

def leastCommonMultiple(x,y):
    return y // gcd(x,y) * x

result = 1
for number in range(1,21):
    result = leastCommonMultiple(result, number)
print("Least Common multiple for range(1,21):", result)