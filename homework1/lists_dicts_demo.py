#list.append(item) to add item to the end of list
#list.insert(index, item) to add item at the index of the list
#list.remove(item) to remove itemfrom list
#list.pop(index) to remove element at index from list

colors = ["pink", "white", "black"]
print(colors[1])
print(colors[-1])
colors.append("blue")
for color in colors:
    print(color)

#print(list[start:stop:step]) #slice a list so that it keeps values from index start and ends at index stop-1
#print(list[::n]) #grab every other nth element
#print(list[start::n]) #start at index start, grab every nth
#list.reverse(() reverse list

student ={
    "name": "Ariana", 
    "year": 4, 
    "major": "Computer Science", 
}

print(student.keys())
print(student.values)

for key in student:
    print(f"{key} = {student[key]}")

for key,value in student.items():
    print(f"{key} = {value}")



