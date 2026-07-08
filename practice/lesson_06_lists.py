# Lesson 06A: List Basics

squares = [1, 4, 9, 16, 25]

print("Full List:")
print(squares)

print("First Item:", squares[0])

print("Last Item:", squares[-1])

print("Last three items:", squares[-3:])

print("Copy of squares list:", squares[:])

more_squares = squares + [36, 49, 64, 81, 100]

print("Combined List:", more_squares)

cubes = [1, 8, 27, 65, 125]

print("Wrong cube List:", cubes)

cubes[3] = 64

print("Corrected cube List:", cubes)

cubes.append(216)
cubes.append(7**3)

print("Final cubes list:", cubes)

# Lesson 06B: List methods

fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print("Original fruits:", fruits)

fruits.append("grape")
print("After append grape:", fruits)

fruits.remove("grape")
print("After remove grape:", fruits)

fruits.insert(0, "grape")
print("After insert grape at index 0:", fruits)

print("Index of grape:", fruits.index("grape"))

print("Index of orange:", fruits.index("orange"))

print("Index of first banana:", fruits.index("banana"))

print("Index of banana after index 5:", fruits.index("banana", 5))

print("Count of tangerine:", fruits.count("tangerine"))

print("Count of banana:", fruits.count("banana"))

vehicles = ["bike", "car", "bus", "car"]

print("vehicles:", vehicles)
vehicles.append("train")

print("vehicles after append train:", vehicles)

vehicles.remove("bike")
print("vehicles after remove bike:", vehicles)

vehicles.insert(0, "scooter")
print("vehicles after insert scooter at index 0:", vehicles)

print("Index of bus:", vehicles.index("bus"))
print("count of car", vehicles.count("car"))
print("Final List:", vehicles)

# Lesson 6B continued: More List methods

fruits = ["grape", "orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

print("Original Fruits:", fruits)

fruits_copy = fruits.copy()
print("Copied Fruits", fruits_copy)

fruits_copy.reverse()
print("Copied fruits after reverse:", fruits_copy)

fruits_copy.sort()
print("Copied fruits after sort:", fruits_copy)

removed_item = fruits.pop()
print("Removed items using pop:", removed_item)
print("Original fruits after pop:", fruits)

fruits.clear()
print("Original fruits after clear:", fruits)

marks = [80, 95, 60, 75, 95]

marks_copy = marks.copy()

marks_copy.sort()
print("Copied marks after sort:", marks_copy)

marks_copy.reverse()
print("Copied marks after reverse:", marks_copy)

removed_item = marks.pop()
print("Removed mark using pop:", removed_item)

marks.clear()
print("Original marks after clear:", marks)
print("Marks Copy:", marks_copy)

# Lesson 6C: del statement

numbers = [-1, 1, 66.25, 333, 333, 1234.5]

print("Original numbers:", numbers)

del numbers[0]
print("After deleting index 0:", numbers)

del numbers[2:4]
print("After deleting index 2 to 4:", numbers)

del numbers[:]
print("After deleting all items using del numbers[:]:", numbers)

numbers = [-1, 1, 66.25, 333, 333, 1234.5]
print("Numbers recreated:", numbers)

del numbers
print("The variable numbers is deleted now")

expenses = [100, 250, 500, 750, 1000]

del expenses[0]
print("After deleting first expenses:", expenses)

del expenses[1:3]
print("After deleting expenses from index 1 to 3:", expenses)

del expenses[:]
print("After deleting all items using del expenses[:] :", expenses)

# Lesson 6D: List Comprehensions

squares = []

for number in range(10):
    squares.append(number**2)

print("Squares using normal for loop:", squares)

squares_comprehension = [x**2 for x in range(10)]

print("Squares using list Comprehensions:", squares_comprehension)

cubes = []

for number in range(6):
    cubes.append(number**3)

print("Cubes using normal for loop:", cubes)

cubes_comprehension = [x**3 for x in range(6)]
print("Cubes using list comprehesions:", cubes_comprehension)

# Lesson 6D Continued: Filtering list comprehesions

vector = [-4, -2, 0, 2, 4]

doubled_vector = [x * 2 for x in vector]
print("Doubled Vector:", doubled_vector)

positive_vector = [x for x in vector if x >= 0]
print("Positive Vector:", positive_vector)

abs_vector = [abs(x) for x in vector]
print("Absolute vector:", abs_vector)

temperatures = [-5, 0, 12, 18, -2, 25]
print("Temperatures:", temperatures)

warm_temperatures = [temp for temp in temperatures if temp >= 15]
print("Warm temperatures: ", warm_temperatures)

doubled_temperatures = [temp * 2 for temp in temperatures]
print("Doubled Temperatures: ", doubled_temperatures)

# Lesson 6D continued: Calling methods iniside list comprehesions

fresh_fruit = [" banana", " loganberry ", "passion fruit "]

clean_fresh_fruit = [fruit.strip() for fruit in fresh_fruit]

print("Fresh fruit with extra spaces: ", fresh_fruit)
print("Clean fresh fruit: ", clean_fresh_fruit)

name = [" vignesh", "swetha ", " python "]

clean_name = [x.strip() for x in name]

print("Name with extra spaces: ", name)
print("Clean Name: ", clean_name)

upper_case = [x.upper() for x in clean_name]

print("Upper Case Name: ", upper_case)

# Lesson 6D continued: Creating tuple pairs

square_tuples = []

for x in range(6):
    square_tuples.append((x, x**2))

print("Square tuples using normal for loop: ", square_tuples)

square_tuples_comprehension = [(x, x**2) for x in range(6)]

print("Sqaure tuples using list comprehension: ", square_tuples_comprehension)

cube_tuples = []

for x in range(6):
    cube_tuples.append((x, x**3))
print("Cubes using normal for loop: ", cube_tuples)

cubes_tuples_comprehension = [(x, x**3) for x in range(6)]
print("Cubes tuples using list comprehension: ", cubes_tuples_comprehension)

# Lesson 6D continued: Flattening nested list

vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_vector = []

for elem in vector:
    for num in elem:
        flatten_vector.append(num)

print("Flatten vector using normal for loop: ", flatten_vector)

flatten_vector_comprehension = [num for elem in vector for num in elem]

print("Flatten vector using list comprehension: ", flatten_vector_comprehension)

groups = [[10, 20], [30, 40], [50, 60]]

flatten_groups = []

for x in groups:
    for y in x:
        flatten_groups.append(y)
print("Flatten group using normal for loop: ", flatten_groups)

flatten_groups_comprehension = [y for x in groups for y in x]
print("Flatten groups using list comprehension: ", flatten_groups_comprehension)
