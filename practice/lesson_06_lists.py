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
