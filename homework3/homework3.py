#File: homework3.py


#3.1
def say_goodbye(name):
    print("Goodbye,", name)

# say_goodbye("Sara")

#3.2
def circle_area(radius):
    area = 3.14 * (radius**2)
    print(area)

# circle_area(3)

#4.1
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

#5.1
readings = [15, 14, 17, 20, 23, 28, 20]
tuple = []
def high_and_low():
    min_value = min(readings)
    max_value = max(readings)
    tuple = [min_value, max_value]
    print(tuple)

# high_and_low()
        
number_dayofweek = {

    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday" : 3,
    "Thursday" : 4,
    "Friday" : 5,
    "Saturday" : 6,
    "Sunday" : 7
}

#5.2
def is_weekend(day):
    if number_dayofweek[day] == 6 or number_dayofweek[day] == 7:
        return True
    else:
        return False
    
# print(is_weekend("Monday"))

#5.3
def fuel_efficiency(distance, fuel_used):
    efficiency = str(distance / fuel_used) + "mi/gal"
    print(efficiency)

# fuel_efficiency(5000, 300)

#5.4
def encryption(data):
    data = str(data)
    encrypted = int(data[-1] + data[:-1])
    return encrypted

encrypted = encryption(12345678)
print(f"The result of encryption (5.4) with the data = 12345678 is {encrypted}")


#6.2
def power(x, y):
    answer = 1
    while y > 0:
        answer = answer * x
        y = y - 1
    return answer

# print(power(2,3))

#6.2.1
integers = [1, 4, 5, 2, 6, 7, 3]
def minimum(integers):
    minimum = integers[0]
    for i in integers:
        if i < minimum:
            minimum = i

    return minimum

# print(minimum(integers))

def maximum(integers):
    maximum = integers[0]
    for i in integers:
        if i > maximum:
            maximum = i

    return maximum

# print(maximum(integers))

#6.2.2
def min_max(integers):
    temp = integers.copy()
    min = temp.pop(0)
    max = min
    while temp:
        current = temp.pop(0)
        if current < min:
            min = current
        if current > max:
            max = current
    return min, max
# print(min_max(integers))

6.3
def sums_of_digits(n:int):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
# print(sums_of_digits(5462384))












        




    