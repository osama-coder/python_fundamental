# Creating Variables عمل متغير
x = 5    # int
y = "John"    # str

# Casting تغيير نوع المتغير
x = str(3)    # x will be string -->> str
y = int(3)    # y will be integer -->> int
z = float(3)  # z will be 3.0 -->> float

# get the variable Type type(variable)معرفة نوع المتغير نستخدم الدالة
x = 5
y = "John"
print(type(x))
print(type(y))

# assign multiple values إدخال أكثر من قيمة في نفس الوقت
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Global Variables وهي المتغيرات المعرفة خارج الدالة وتكون معروفة داخل وخارج دوال الكلاس
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# The global Keyword تستخدم لجعل المتغر المعرف بعدها معروف علي جميع مستوي الكلاس
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)