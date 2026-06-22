# Membership operator

# in , not in

a = [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15]

print(10 in a)  # True
print(9 in a)  # False


# For Loop

a = [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15]

for i in a:
    print(i)
    print(i + 1)  # 1 add hudai janxa

# for data in "Kathmandu":
#     print(data)


print("####################################")
world_cup_data = {
    "tournament": "FIFA World Cup",
    "year": 2022,
    "host": "Qatar",
    "winner": "Argentina",
    "runner_up": "France",
    "golden_boot": "Kylian Mbappé",
    "golden_ball": "Lionel Messi",
    "total_teams": 32,
    "total_matches": 64,
    "total_goals": 172,
}

for j in world_cup_data:
    print(j)  # key haru print hunxa

print("/////////////////////////////////////")

for j in world_cup_data.values():
    print(j)  # value haru print hunxa

print("/////////////////////////////////////")
for key, value in world_cup_data.items():
    print(key, value)  # key ra value haru print hunxa


print("####################################")


# even, odd using for loop
a = [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15]
for i in a:
    if i % 2 == 0:
        print(i)

    else:
        print("This is Odd number")


print("----------------------------------------")

# Range function (start, stop, step)

for i in range(1, 10):
    print(i)  # 1 dekhi 9 samma print hunxa


print("----------------------------------------")


# using for loop and range function

# 2 X 1 = 2
# 2 X 2 = 4
# .......
# 2 X 10 = 20

num = 2
for i in range(1, 11):
    print(f" {num} X {i} = {num * i}")


print("///////////////////////////////")


# break , continue

A = [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15]
for i in A:
    if i == 10:
        break  # loop stop hunxa
    else:
        print(i)  # 10 samma print hunxa

print("_____________-------____________________")


a = [1, 2, 3, 4, 5, 7, 10, 11, 12, 13, 14, 15]
for i in a:
    if i == 10:
        continue  # loop skip hunxa
    print(i)  # 10 skip hunxa ra baki print hunxa


print("_____________-------____________________")
# only display float data from the list
mixed_list = [1, 2.5, "apple", 4, 5.5, "banana", 7, 8.8, "cat", 10]

for i in mixed_list:
    if isinstance(i, float):
        print(i)  # float data print hunxa
    else:
        continue  # continue le baki code skip garxa ra next iteration ma janxa


print("_____________-------____________________")

# Nested List

for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        print(i, j)  # i ra j ko combination print hunxa
    print("------")


print("_____________-------______-------_______________")


# sum of this list using for loop
a = [1, 2, 3, 4, 5, 5, 6]
total = 0
for i in a:
    total += i  # total = total + i
print(total)  # list ko sum print hunxa
