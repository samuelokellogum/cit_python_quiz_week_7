# No 1

class Animal:
    food_list = []
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def get_name(self):
        return self._name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self.age = age

    def get_food(self):
        return self._food

    def add_food(self, new_food):
        food_list.append(new_food)

    def remove_food():
        pass

class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        self.name = name
        self.age = age
        self.food = food

    def talk():
        print('Moew')    

class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        self.name = name
        self.age = age
        self.food = food

    def talk():
        print('Woff')

    
class Fish(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        self.name = name
        self.age = age
        self.food = food

    def talk():
        print('Blub')
    
class Cow(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)
        self.name = name
        self.age = age
        self.food = food

    def talk():
        print('Muuu')

cat = Cat()
dog = Dog()
fish = Fish()
cow = Cow()


#2 
def snail_solver():
    pass


#3 Return largest 

def return_largest_number():
    list_of_numbers = [22,45,78,90,100,23,1]
    list_of_numbers.sort()
    return list_of_numbers[-1]

#4 
def cal_upper_and_lower():
    phrase = input("Type in: ")
    phrase = list(phrase)

    u, l = 0, 0
    for i in phrase:
        if i.isupper():
            u = u + 1
        if i.islower():
            l = l + 1
        else:
            pass

    print("UPPER:", u)
    print("lower:", l)



#6 Write a Python program that lists out all the default as well as custom properties of the class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Samuel", 95)
print("Student class's object all properties")

print(dir(student))


#7 Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal methods.
my_stack = [] 
# append() function to push
# element in the stack
my_stack.append('a')
my_stack.append('b')
my_stack.append('c')
 
print('Initial stack')
print(my_stack)

print('\nElements popped from stack:')
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
 
print('\nStack after elements are popped:')
print(my_stack)


#8 Using list comprehension, write a program that takes a list of numbers and returns a list of the squares of the numbers.
data=[1,2,3,4,5,6,7] 
result = [i*i for i in data] 
print(result)