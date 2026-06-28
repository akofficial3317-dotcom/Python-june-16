

for i in [1,2,3,4,5,6]:   # Using list in loop
    print(i)



for z in "Broadway":         # Using String in Loop
    print(z)



# Using Dictionary

a = {
    "Name" : "Ram",
    "Address" : "Nepal"
}

for i in a.items():
    print(i)

for i in a.values():
    print(i)


for i in a:           # The output will be same as items(). 
    print(i, a[i])


# Range 

for i in range(1,20,1):
    print(i)





print("__________________________")

# Multiplication table using range

num = int(input("Enter the Number: "))

for i in range(1,11):
    print(f"{num} X {i} = {num * i}")



print("======================================")

# Break, continue

# Break
num = int(input("Enter the Number: "))

for i in range(1,11):
    if i == 7:
        break          # loop chaldai janxa nai jaha i == 7 aauxa vane yehi thau ma break garxa ani tala jadain
    print(f"{num} X {i} = {num * i}")



print("-_-_-_-_-_-_"*10)

# Continue

num = int(input("Enter the Number: "))

for i in range(1,11):
    if i == 7:
        continue          # loop chaldi janxa nai jaha i == 7 aauxa vane 7 lai xodera baki sabai print garxa
    print(f"{num} X {i} = {num * i}")


print("-------------------------------")
# Nested Loop

for i in range(1,5,1):
    for j in range(2,5):
        print(i,j)


print("============================================")

a = [10, 20, 10, 10]

for i in set(a):
    for j in range(1,11,1):
        print(f"{i} x {j} = {i * j}")
    print("\n")





# append in list 
result = []
for i in range(1,5):
    data = int(input(f"Enter the {i} number: "))
    result.append(data)



for i in set(result):
    for j in range(1,11,1):
        print(f"{i} x {j} = {i * j}")
    print("\n")



# Take multiple numbers as input
a = list(map(int, input("Enter numbers separated by space: ").split()))

for i in a:
    print(f"\nMultiplication Table of {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")





