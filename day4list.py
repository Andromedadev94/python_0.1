matrix_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix_list)
print(matrix_list[1])
print(matrix_list[2][1])
for rows in matrix_list:
    for items in rows:
        print(items)
matrix_list[0][0]= 12
print(matrix_list[0][0])

list_a= ["a", "b", "c"]
list_b= [1, 2, 3]
list_c= list_a + list_b
list_d= list_a * 2
print(list_c, list_d)

list_a= ["a", "b", "c"]
del list_a[0]  #to delete a value at an index
print(list_a)

cat = ['fat', 'gray', 'loud']
for index, item in enumerate(cat): #instead of range of list
    print(index, item)

#list methods
list_of_numbers=[1,5,2,77,3,44,2]
print(list_of_numbers.count(2)) # to check how many of an item is in the list
list_of_numbers.sort() # to sort the items in a list assending
print(list_of_numbers)  
list_of_numbers.reverse()  # to sort the items in a list decending
print(list_of_numbers)
list_of_numbers.append(20)  # to add an item at the end of a list
print(list_of_numbers)
list_of_numbers.remove(20)   #to remove an item from list
print(list_of_numbers)
list_of_numbers.insert(0,10)  #to add an item somewhere in the list with index
print(list_of_numbers)
list_of_numbers.pop()         #to remove last item in the list
print(list_of_numbers)
print(list_of_numbers.index(2))  #find the index of and item, first time it finds it
list_of_numbers.clear()
print(list_of_numbers)  #to clear a list
print(12 in list_of_numbers)  #to check if an item is inside a list
list2=list_of_numbers.copy() # to copy a list, note that everychanges to the original copy will not affect the copy after this line
print(list2) 
list_of_numbers.append(10)
print(list_of_numbers)
print(list2)


#to delete duplicates in a list
list_to_remove = [10,33,22,33,19,20,22,10,3,2]
no_dup_list=[]
for number in list_to_remove:
    if number not in no_dup_list:
        no_dup_list.append(number)
print(no_dup_list)

list_tuple=(1,2,5,3)  #tuple lists are inside() and the difference with normal list is that , we can not change them
print(list_tuple[0])
#unpacking: 
list_to_unpack=[1,3,5,3]
x=list_to_unpack[0]
y=list_to_unpack[1]
z=list_to_unpack[2]
t=list_to_unpack[3]
#or we can do it easier by doing unpacking
x,y,z,t=list_to_unpack
print(y*z)

#dictionaries are used to A fast way to store and look up data using a key → value relationship
user_data={
    "name":"farhad",
    "age":22,
    "married":False
}
print(user_data)
print(user_data.get("name", "country")) #get can take two parameters, second on will be used
                                        # if first key was not in the dictionary



p_number=str(input("phone number pls: "))
translation={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten"
}
for part in p_number:
    print(translation.get(part), end=" and ")  #the end part we tell the print fuction to what to do after each word being printed, default is going to next line

spam = {'color': 'red', 'age': 42}
print(list(spam.values()))
print(list(spam.keys()))
print(spam.items())
for key, value in spam.items():
    print(f"key = {key}, and value = {value}")
