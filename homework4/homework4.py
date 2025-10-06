favorite_foods = ["mangoes", "icecream", "hotpot", "fries", "pasta"]

print(favorite_foods[1])
print(favorite_foods[-1])
favorite_foods.append("strawberries")
favorite_foods.insert(0, "sushi")
del favorite_foods[2]
print(len(favorite_foods))
for food in favorite_foods:
    print(food.upper())
first_last = [favorite_foods[0], favorite_foods[-1]]
if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!")


numbers = list(range(0,21))

def get_first_15(numbers_list):
    result = numbers_list[:15]
    return result

def get_every_5th(lst):
    result = lst[::5]
    return result

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    result = reversed_list[::3]
    return result

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])

numbers.append([10,11,12])
for row in numbers:
    print(row)

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for number in row:
            total += number
    return total
print(sum_nested(numbers))

def matrix_5x5():
    matrix = []
    counter = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(counter)
            counter += 1
        matrix.append(row)
    return matrix

# print(matrix_5x5())

matrix = matrix_5x5()

def replace_mult3(matrix):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(new_matrix)):
        for j in range (len(new_matrix[i])):
            if new_matrix[i][j] % 3 == 0:
                new_matrix[i][j] = "?"

    return new_matrix

# print(replace_mult3(matrix))

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])


ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

for key, value in ages.items():
    print(f"{key}: {value}")

def matrix_5x5():
    matrix = []
    counter = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(counter)
            counter += 1
        matrix.append(row)
    return matrix

print(matrix_5x5())


    
    
