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
