import random

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

#4 Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
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

#5
def roll():
    return random.choice([1,2,3,4,5,6])

class player(object):
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour
        
    def score(self, score):
        self.score = score    
    def getscore(self):
        return self.score
    
    def getname(self):
        return self.name
    def __str__(self):
        return 'NAME: ' + self.name + '\nCOLOUR: ' + self.colour + '\nSCORE: ' + str(self.score)
    

class game(object):
    def __init__(self, playr, trails):
        self.trails = trails
        self.playr = playr
        
    def gaming(self):
        throw = 0
        score = 0
        for i in range(self.trails):
            throw = roll()
            if throw == 6:
                throw = throw + roll()
            score = throw + score    
        return score
        
    def __str__(self):
        return self.playr.getname() + str(self.score)
tri = 123        
    


david = player('david', 24, 'green')
collins = player('collins', 25, 'yellow')
levi = player('levi', 14, 'red')
davin = player('davin', 13, 'blue')
print("-----------Playing Dice Game--------------\n" )

davidscr = game(david, tri)
collinsscr = game(collins, tri)
leviscr = game(levi, tri)
davinscr = game(davin, tri)

scr = []
scr.append(zackscr.gaming())
scr.append(johnyscr.gaming())
scr.append(kinascr.gaming())
scr.append(usherscr.gaming())

scrsort = sorted(scr)
for el in scrsort:
    print(el)

david.score(scr[0])
collins.score(scr[3])
levi.score(scr[2])
davin.score(scr[1])

print(david, '\n')
print(collins, '\n')
print(levi, '\n')
print(davin, '\n')

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


#9 Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).

class Queue:
	# __init__ function
	def __init__(self, capacity):
		self.front = self.size = 0
		self.rear = capacity -1
		self.Q = [None]*capacity
		self.capacity = capacity
		
	def isFull(self):
		return self.size == self.capacity
		
	def isEmpty(self):
		return self.size == 0
	
	def EnQueue(self, item):
		if self.isFull():
			print("Full")
			return
		self.rear = (self.rear + 1) % (self.capacity)
		self.Q[self.rear] = item
		self.size = self.size + 1
		print("% s enqueued to queue" % str(item))

	def DeQueue(self):
		if self.isEmpty():
			print("Empty")
			return
		
		print("% s dequeued from queue" % str(self.Q[self.front]))
		self.front = (self.front + 1) % (self.capacity)
		self.size = self.size -1
		
	# Function to get front of queue
	def que_front(self):
		if self.isEmpty():
			print("Queue is empty")

		print("First item is", self.Q[self.front])
		
	# Function to get rear of queue
	def que_rear(self):
		if self.isEmpty():
			print("Queue is empty")
		print("Rear item is", self.Q[self.rear])


# Main
if __name__ == '__main__':

	queue = Queue(30)
	queue.EnQueue(10)
	queue.EnQueue(20)
	queue.EnQueue(30)
	queue.EnQueue(40)
	queue.DeQueue()
	queue.que_front()
	queue.que_rear()


#10 Using a while loop, implement merge sort algorithm.
def merge(left, right):
	if not len(left) or not len(right):
		return left or right

	result = []
	i, j = 0, 0
	while (len(result) < len(left) + len(right)):
		if left[i] < right[j]:
			result.append(left[i])
			i+= 1
		else:
			result.append(right[j])
			j+= 1
		if i == len(left) or j == len(right):
			result.extend(left[i:] or right[j:])
			break

	return result

def mergesort(list):
	if len(list) < 2:
		return list

	middle = int(len(list)/2)
	left = mergesort(list[:middle])
	right = mergesort(list[middle:])

	return merge(left, right)
	
seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq);
print("\n")
print("Sorted array is")
print(mergesort(seq))

# Code Contributed by Mohit Gupta_OMG
