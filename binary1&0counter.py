def binary_ones():
    number1 = int(input("first number: "))
    number2 = int(input("sceond number: "))
    counter_one = 0
    counter_zero = 0
    result = number1 * number2
    while result > 0:
        if result & 1 == True:
            counter_one = counter_one + 1
        else:
            counter_zero = counter_zero + 1
        result = result >> 1
    return [counter_one, counter_zero]

result = binary_ones()
print("number of binary '1': " + str(result[0]) + " number of binary '0': " + str(result[1]))