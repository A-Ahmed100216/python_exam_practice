# # 1. Declare a list with numbers 1 to 5 and add 6 at the end.
# # Create a list making sure to use square brackets and print.
# my_list=[1,2,3,4,5]
# print(my_list)
# # Use the append method to add 6 at the end
# my_list.append(6)
# # Print the new list
# print(my_list)

# # 2.
# # (a)Create a tuple with numbers 1 to 5 and add the number 2.2 at index 1
# my_tuple=(1,2,3,4,5)
# print(my_tuple)
# # Tuples are immutable so we convert to list
# tuple_to_list=list(my_tuple)
# # Insert the value at the required index.
# tuple_to_list.insert(1,2.2)
# # Convert back into tuple
# tuple2=tuple(tuple_to_list)
# # Print the amended tuple
# print(tuple2)
# (b) Create a dictionary and iterate to print the numbers up to 3.
my_dict={"num1":1, "num2":2, "num3":3, "num4":4, "num5":5}
# Use for loop to iterate through values
for x in my_dict.values():
    # If the value is less than 4, print it
    if x<4:
        print(x)

