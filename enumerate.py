numbers = [1,2,3,4]

# enumerate() is used to loop through a list and get both the index and the value of each item in the list. It returns an enumerate object which can be converted to a list of tuples, where each tuple contains the index and the corresponding value from the original list.
for index, value in enumerate(numbers):
    print(f"index: ", index, end=" ")
    print(f"value: ",value,end='\n')