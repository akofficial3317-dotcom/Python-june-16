
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

def calculate_fine(book_name, borrowed_days, allowed_days, fine_per_day):
    if not isinstance(borrowed_days, int) or \
       not isinstance(allowed_days, int) or \
       not isinstance(fine_per_day, int):
        print("error: number should be int")

        return

    if borrowed_days > allowed_days:
        fine = (borrowed_days - allowed_days) * fine_per_day
    else:
        fine = 0

    print(fine)


    
calculate_fine("python",10,5,10) # 50
calculate_fine("html",1.9,5,10) # error number should in int
calculate_fine("html",1,"5",0) # error number should in int


print("_-_-_-_-_-_-_-_-_-"*5)

# POstional Argument
        
def add(*args):
    if len(args) == 0:
        return "Please provide any number"
    total = 0
    for i in args:
        if isinstance(i, int):
            total = total + i
    return total



print(add(1,2,"sudan","tets"))
print(add(1,2,3))
print(add(1,2,3,4))
print(add())



# Keywords Arguments

print("==================================")

def all(*args, **kwargs):
    print(*args)
    print(kwargs)


all(1,2,3,4, "hari", "Ram", 1,2, name = "Shyam")  # pahile possitional arguments (args) ani tespaxi Keywords arguments (**kwargs) bala aauxa
all(1,2,3,4, "hari", "Ram", 1,2)   # yeta **kwargs ko {} yo empty aauxa.



print("==========================================================")

def marksheet(student_name, *subjects, **extra):
    total = 0
    for i in subjects:
        total = total + i[1]
        # total += i[1]
    return (f"{student_name}'s total marks is {total} and percentage is {total/len(subjects)} and class teacher is {extra.get('class_teacher')}")




print(marksheet(
    "Sudan Bhandari",
    ("Mathematics", 92),
    ("Science", 88),
    ("English", 85),
    ("Social Studies", 81),
    class_teacher="Mr. Sharma",
    grade_level="Grade 10",
    attendance="96"
))