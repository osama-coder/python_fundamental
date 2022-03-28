# هناك ثلاث أنواع من البيانات شائعة الإستخدام
x = 1    # int
y = 2.8  # float
z = 1j   # complex


# generate random numbers
import random
print(random.randrange(1, 10)) # بترجع رقم صحيح بين ال1 وال10
print(random.randrange(1, 10)) # بترجع رقم صحيح بين ال1 وال10

mylist = ["apple", "banana", "cherry"]
print(random.choices(mylist, k = 14))    # بترجع 14 قيمة من الlist اللي أسمهاmylist