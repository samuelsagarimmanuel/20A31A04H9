# write a porg of user defined function which returns a interger value to the column
def add_numbers(a,b):
    return a+b
def sub_numbers(a,b):
    return a-b
def mult_numbers(a,b):
    return a*b
def div_numbers(a,b):
    return a/b
def floor_division(a,b):
    return a//b
def mod(a,b):
    return a%b
def main():
    num1 = 8
    num2 = 6
    num3 = 4
    num4 = 2
    num5 = 10
    num6 = 0

    result1 = add_numbers(num1, num2)
    result2 = sub_numbers(num3, num4)
    result3 = mul_numbers(num5, num6)
    result4 = div_numbers(num1, num4)
    result5 = floor_division(num2, num3)
    result6 = mod(num5, num2)

    print("Result 1:", result1)
    print("Result 2:", result2)
    print("Result 3:", result3)
    print("Result 4:", result4)
    print("Result 5:", result5)
    print("Result 6:", result6)