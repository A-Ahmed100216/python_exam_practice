# Python Exam Practice

## Assessment Categories
1. Design 
2. Language Knowledge
3. Problem Solving
4. Reliability

## Potential Exam Topics
* Collections - Lists, Tuples, Sets, Dictionaries
* Syntax - Declaring variables
* Methods/ Functions
    * Syntax for declaring functions and methods is the same ```def name():```
    * Difference? Methods defined within classes, functions outside classes.
* Control Flow -if, else, elif
* Loops - for loops and while loops
* Operators
  * Arithmetic - ```+ - * / > < =```
  * Boolean - ```is``` , ```is not```
  * Comparatives - ```and``` ,```or```
 * Built-in methods 
   * list methods - append(), pop(), remove() etc.
   * string methods - upper(), lower()
* OOP 
  * 4 pillars, inheritance, encapsulation, polymorphism, and abstraction 
  * How can you inherit a class from x to y?
  * Syntax : ```class Name:```
  * Keywords: class, self, super, \_\_init__
  * Declare a method that takes 4 arguments- no class is needed 
  
## Practice Questions
##### 1. Declare a list with numbers 1 to 5 and add 6 at the end.
```python
# Create a list making sure to use square brackets and print.
list=[1,2,3,4,5]
print(list)
# Use the append method to add 6 at the end
list.append(6)
# Print the new list
print(list)
```

##### 2. (a)Create a tuple with numbers 1 to 5 and add the number 2.2 at index 1
```python
my_tuple=(1,2,3,4,5)
print(my_tuple)
# Tuples are immutable so we convert to list
tuple_to_list=list(my_tuple)
# Insert the value at the required index.
tuple_to_list.insert(1,2.2)
# Convert back into tuple
tuple2=tuple(tuple_to_list)
# Print the amended tuple
print(tuple2)
```
##### (b) Create a dictionary and iterate to print the numbers up to 3.
```python
my_dict={"num1":1, "num2":2, "num3":3, "num4":4, "num5":5}
# Use for loop to iterate through values
for x in my_dict.values():
    # If the value is less than 4, print it
    if x<4:
        print(x)
```

#### 3. Declare a shopping dictionary with three items and their prices
```python
shopping={"eggs":0.89, "milk":1.09, "bread":1.00}
# Print the type of collection
print(type(shopping))
# Print the price of the item eggs
print(shopping["eggs"])
```

#### 4. Using the previous dictionary, update the price of eggs
```python
shopping["eggs"]=2
print(shopping)
```
#### 5. Declare an add method that takes two argument
```python
def add(num1,num2):
    return num1 + num2
print(add(5,10))
```


#### 6. Create a class called person with name and age. Then create an object of this class.
```python
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
# Create an object of the class
test=Person("Harry",40)
print(test.name)
print(test.age)
```
#### 7. Create a child class of the Person class which takes student id and course. Create an object and print the attributes.
```python
class Student(Person):
    def __init__(self,name, age, student_id,course):
        super().__init__(name,age)
        self.student_id=student_id
        self.course=course

student=Student("Ben",22,2901920,"DevOps")
print(student.name)
print(student.age)
print(student.student_id)
print(student.course)
```
#### 8. Create a dictionary with 4 items with prices. Calculate the total price of the items.
```python
dict2= {"bread":0.99,"eggs":0.89,"milk":1.09,"chocolate":1.00}
print(dict2["bread"] + dict2["eggs"] + dict2["milk"] + dict2["chocolate"])
```



# 9. Create a function to calculate the total price of the items. 
```python
def add_dict2():
    return sum(dict2.values())
print(add_dict2())
```

#### 10. (a) What is the super() method?
The super method allows one to access attributes from the parent class.
#### 10. (b) Add another item to the dictionary at index 3
```python
dict2= {"bread":0.99,"eggs":0.89,"milk":1.09,"chocolate":1.00}
dict2['kiwis']=3
print(dict2)
```
**Add kiwi at index 3 -- trick question, this won't work with dictionaries**


#### 11. Create a shopping list, iterate through and if rice is in list, stop
```python
shopping_list=['chicken','pasta','rice','eggs']
for x in shopping_list:
    if x=="rice":
        break
    print(x)
```
testing git
