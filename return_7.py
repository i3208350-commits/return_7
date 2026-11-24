# תרגיל 1
# def Hello_World():
#     print("Hello World")
# Hello_World()
# Hello_World()
# Hello_World()
# # תרגיל 2
# def show_welcom():
#     print("Welcome to the system")

# show_welcom()

# # תרגיל 3
# def show_menu():
#     print("""
#     ===== Main Menu =====
# 1. Start
# 2. Settings
# 3. Exit""")

# # תרגיל 4
# def show_numbers():
#     for i in range(11):
#         print(i)

# show_numbers()

# # תרגיל 5
# def show_even_numbers():
#     for i in range(101):
#         if i % 2 ==0:
#             print(i)

# show_even_numbers()

# # תרגיל 6
# def show_stars():
#     print("**********")
# show_stars()

# # תרגיל 7
# def greet(name):
#     print("Hello", name)
# greet("David")
# greet("Moshe")


# # תרגיל 8
# def show_age(age):
#     print(age)
# show_age(26)

# # תרגיל 9
# def calculate_sum(x,y):
#     print(x+y)
# calculate_sum(10,80)

# # תרגיל 10
# def calculate_average(a,b,c):
#     s=a+b+c
#     print(s/3)
# calculate_average(100,90,80)

# # תרגיל 11
# def check_even(x):
#     if x %2==0:
#         print("even")
#     else:
#         print( "non")
# check_even(72)

# # תרגיל 12
# def check_password(x):
#     if x=="123456":
#         print("Access Granted")
#     else:
#         print("Access Denied")

# # תרגיל 13
# def calculate_discount (price, discount):
#     total=price*(1-(discount/100))
#     print(total)

# calculate_discount (1000, 20)

# # תרגיל 14
# def show_range(x,y):
#     for i in range(x,y+1):
#         print(i)
# show_range(50,70)

# # תרגיל 15
# def print_rectangle(x,y):
#     for i in range(x):
        
#             print("*"*y)
# print_rectangle(5,3)

# # תרגיל 16
# def multiply (x,y):
#     return x*y

# # תרגיל 17
# def get_full_name(nam, famili):
#      return f"{nam}  {famili}"

# t=get_full_name("a", "v")
# print(t)

# # תרגיל 18
# def get_max(x,u):
#     if x>u:
#         return x
#     if u>x:
#         return u
# s=get_max(5,8)
# print(s)

# תרגיל 19
def is_positive (x):
    if x>0:
        return True
    else:
        return False

# # תרגיל 20
# def calculate_tax(x,y):
#     return x*(1+y/100)
# t=calculate_tax(100,18)
# print(t)

# # תרגיל 21
# def get_grade_status(m):
#     if m>90:
#         return "Excellent" 
#     if m>=75 and m<90:
#             return "Good" 
#     if m>59 and m<75:
#             return "Average" 
#     if m>60:
#             return "Failed" 

# # תרגיל 22
# def count_digits(x):
#     return len(x)

# # תרגיל 23
# def calculate_power(x,y):
#     return x**y
# # תרגיל 25
# def print_list(x):
#     coo=0
#     for i in (x):
#         coo+=i
#     return coo
# v=print_list([1,6,9,5])
# print(v)

# # תרגיל 24
# def print_list(x):
#     for i in x:
#         print(i)

# # תרגיל 26
# def get_list_average(x):
#     total=0
#     for i in x:
#         total+=i
#     return total


# # תרגיל 27
# def find_number(x,listi):
#     for i in listi:
#         if i ==x:
#             return True

# # תרגיל 28

# def find_number(x):
#     total=0
#     for i in x:
#         if i > total:
#             total=i
#     return total
# d=find_number([8,56,7])
# print(d)

# # תרגיל 29
# def get_even_numbers(c):
    
#     o=[nam for nam in c if nam % 2 ==0]
#     return o
# s=get_even_numbers([9,78])
# print(s)
# # תרגיל 30

# def  get_long_names (x):
#     l=[name for name in x if len(name)>3]
#     return l
           
# # תרגיל 31
# def reverse_list(x):
#     d=[d for d in x [::-1]]
#     return d
# v=reverse_list([8,7,54,3,3])
# print(v)

# # תרגיל 32
# def count_occurrences(x,n):
#     co=0
#     for i in x:
#         if i ==n:
#             co+=1
#     return co

# # תרגיל 33
# def remove_duplicates(x):
#     v=[]
#     for i in x:
#         if i not in v:
#             v.append(i)
#     return v

# # תרגיל 34
# def calculate_final_price(x,o):
#     y=x*(1-o/100)
#     if y>500:
#         return y*(0.95)
#     else:
#         return y

# # תרגיל 35
# coonet=0
# c=0
# def check_list(x):
#     for i in x:
#         if i % 2 ==0:
#             c+=1
#         else:
#             coonet+=1
#     return c,coonet,len(x)
# # תרגיל 36
# def analyze_grades (x):
#     d=max(x)/len(x)
#     co=0
#     c=max(x)
#     b=min(x)

#     for i in x:
#         if i>59:
#             co+=1
#     return co, c ,b,d 
# # תרגיל 37
# def validate_user(x,v):
#     if len(x)>0 and len(v)>5:
#         return True
#     return False

# תרגיל 38
# def search_students(c,x):
#     for i in c:
#         if i["name"]==x:
#             return i
       
#     return None

# # תרגיל 39
# def calculate_cart_total(cart):
#     total=0
#     for i in cart:
#         total+=i["price"]
#     return total


# cart = [    {"name": "Laptop", "price": 4500, "quantity": 1},    {"name": "Mouse", "price": 80, "quantity": 2},    {"name": "Keyboard", "price": 150, "quantity": 1}]
# x=calculate_cart_total(cart)
# print(x)

# # תרגיל 40
# def  get_fibonacci(n):
#     listi=[0,1]
#     for i in range(n):
#         listi.append(listi[-1]+listi[-2])
#     return listi
# s=get_fibonacci(1000)
# print(s)



# # תרגיל 41
# name = "David"
# def show_name():
# 	name = "Moshe"
# print(name)
# show_name()
# print(name)

# # תרגיל 42
# counter = 10
# def increase():
# 	counter = 20
# 	print(counter)
# increase()
# print(counter)

# # תרגיל 43
# number=10
# def ggg(number):
#     number+=10
#     return number

     
# a=ggg(number)
# print(number)

# # תרגיל 44
# def listi(o):
#     o.append(10)
#     return o

# d=[5,7]
# u=listi(d)
# print(u)

# # תרגיל 45
# def crait(listi):
    
#     j=[listi[::2]]
#     j.append(12)
#     return j
# a=crait([1,2,3,4,5,6,7,89])
# print(a)

# פרויקט מסכם
students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]

def show_students(students):
                print(students)
def add_student(students):


            name=input("enter name")
            age=int(input("enter age"))
            grade= int (input(" enter grade"))
            new={"name": name,
                 "age": age,
                 "grade":grade}
            students.append(new)
def search_student(students, name):
    
    print("ooo")
    for i in students:
        if i["name"]==name:
              print(i)
def update_grade(students, name, grade):
      for i in students:
            if i["name"]==name:
                i["grade"]=grade
def remove_student(students, name):
      for i in students:
                if i["name"]==name:
                    students.remove(i)
                    print(students)
def get_passing_students(students):
      listi=[]
      for i in students:
            if i["grade"]>=60:
                 listi.append(i)
                 return listi
                  
      
           
def show_menu():
    while True:
        print("""===== Student Management =====

        1. Show all students
        2. Add student
        3. Search student
        4. Update student grade
        5. Remove student
        6. Show passing students
        7. Show class statistics
        8. Show students above average
        0. Exit""")
        cohos=input("enter cohos")
        if cohos =="1":
            
            show_students(students)
        if cohos =="2":
           print("llll")          
           add_student(students)
        if cohos =="3":
            name=input("enter name")
            search_student(students, name)
        if cohos =="4":
            name=input("enter name")  
            grade=int(input("grade"))
            update_grade(students, name, grade)
        if cohos =="5":
                name=input("enter name")  
                remove_student(students, name)
        if cohos =="6":
              a=get_passing_students(students)
              print(a)
        if cohos =="7":
              

        if cohos =="0":
            break
show_menu()