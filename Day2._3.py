a = [1, 2, 3, 4, 5, 6]

print(a)

print(type(a))

print(a[0])

# print(a[-6]) index out of range vanera aauxa error

print(len(a))


a[0] = 100  # change the element by using index
print(a)


# Slicing

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[3:5])
print(a[:5])
print(a[1:])
print(a[:])

print("_-------------------------_")

# Append

a = [1, 2, 3]
a.append(4)
print(a)


# Empty list
a = []
a.append(2)
print(a)


print("#######" * 5)

# Insert

a = [1, 2, 3, 5, 6]
a.insert(3, 4)
a.insert(1, 999)
a.insert(399, 3)  # yesma pahile index 399 khojxa yadi vetena vane last ma gayer haldinxa
print(a)


print("------" * 10)

# Extends
a = [1,2,3]
b = [4,5,6]

a.extend(b)
print(a)


# Concate
a = [7,8,9]
b = [10,11,12]

c = a + b
print(c)


