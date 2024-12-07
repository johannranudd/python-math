import math

# svar = 8 - 2*3**2 + (7 - 5)**4/math.sqrt(64)
# print("svar:",svar)

# 1.38
# a = 6**2/4-2
# print("a:",a)

# b = math.sqrt(9) - 5 * 2**3*0.1
# print("b:",b)

# c = 1-2*(3-4)**5
# print("c:",c)


# Ex 13:

# n = 1 
# while n < 51:
#     partall = 2*n
#     print(partall)
#     n+= 1

# partall = 0
# while partall < 100:
#     partall = partall + 2
#     print(partall)

# Ex 14:

# for n in range(50):
#     oddetall = 2*n + 1
#     print(oddetall)

# for oddetall in range(1, 100 ,2):
#     print(oddetall)


# 1.40 
# a)
# n = 1000
# while n < 1200:
#     if (n%2 != 0):
#         print(n)         
#     n += 1

# option 2)
# n = 1001
# while n < 1200:
#     print(n)         
#     n += 2

# n = 1000
# for n in range(n, 1200, 1):
#     if (n%2 != 0):
#         print(n)

# option 2
# for n in range(1001, 1200, 2):
#     print(n)

# 1.41
# a)

# n = 500 
# while n <= 750:
#     if (n%2 == 0):
#         print(n)
#     n += 1

# option 2
# n = 500 
# while n <= 750:
#     print(n)
#     n += 2

# for n in range(500, 751, 2):
#     print(n)

# option 2:
# for n in range(500, 751, 1):
#     if (n%2 == 0):
#         print(n)


# Ex 15:

# A = {0}
# B = {0}

# for n in range(0, 31, 1):
#     if (n%3 == 0):
#         A.add(n)
#     if (n%4 == 0):
#         B.add(n)

# option 2:
# for n in range(0, 31, 3):
#         A.add(n)
# for n in range(0, 31, 4):
#         B.add(n)

# print("A =", A)
# print("B =", B)
# C = A.intersection(B)
# print("C =", C)

# 1.42 
# a)

A = {0}
B = {0}

for n in range(0, 41, 1):
    if (n%4 == 0):
        A.add(n)
    if (n%5 == 0):
        B.add(n)

print("A =", sorted(A))
print("B =", sorted(B))
C = A.union(B)
print("C =", C)