
# Functions

def hello():
    print("Hello World")

# hello()
print(hello())   # It return None



def math ():
    return[1,9]

print(math())



# name1 = input("Enter your name: ")

# def num():
#     print("Name is: ",name1)

# num()


# Positional Argument 

def add (a,b):
    return a + b

print(add(1,10))
print(add(20,11))




def user_info(fname, lname):
    return f'My name is {fname} {lname}'


print(user_info("Sharma", "Hari"))
print(user_info("Hari", "Sharma"))


print("Keyword args")

# Keyword Argument

print(user_info(lname="Sharma", fname="Ram"))



# Question 2: Library Fine Calculator

# def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
#     if not isinstance(borrowed_days, int) or \
#        not isinstance(allowed_days, int) or \
#        not isinstance(fine_per_day, int):
#         print("error: number should be int")

#         return

#     if borrowed_days > allowed_days:
#         fine = (borrowed_days - allowed_days) * fine_per_day
#     else:
#         fine = 0

#     print(fine)


    
# calculate_fine("python",10,5,10) # 50
# calculate_fine("html",1.9,5,10) # error number should in int
# calculate_fine("html",1,"5",0) # error number should in int




