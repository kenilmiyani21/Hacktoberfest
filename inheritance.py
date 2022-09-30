'''
Single Level Inheritance
-> Inheritance is defined as the capability of one class to derive or inherit the properties from some other class and use it whenever needed. Inheritance provides the following properties:
-> It represents real-world relationships well.
-> It provides reusability of code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
-> It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
'''


class A:  # super class, parent classs, Base class
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')


class B(A):  # Derived class, childclass
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')


a = A()
a.feature1()
a.feature2()

b = B()
b.feature3()
b.feature4()

# -----------------------------------------
# inherit

a = B()
a.feature1()
a.feature2()
a.feature3()
a.feature4()


# ---------------------------------------
# Object calling
class A:
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print('feature1 is working')


class B(A):
    # def __init__(self):
    # 	print('__init__ of B')

    def feature4(self):
        print('feature4 is working')


b = B()

'''
-> IF we want to call both class's init method we use Super() method.
-> It refers to parent class. So we can access all the methods of parent class.
'''


# ex.

class A:
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print('feature1 is working')


class B(A):
    def __init__(self):
        super().__init__()
        print('__init__ of B')

    def feature4(self):
        print('feature4 is working')


b = B()

'''
-> If we have 2 super class -> that time object use MRO(Method Resolution Order) 
-> It will start from Left to Right.
-> Ex. 2 class.. A and B. So it will take A's init.
'''


# ex.

class A:
    def __init__(self):
        print("__init__ of A")

    def feature1(self):
        print('feature1 is working')


class B:
    def __init__(self):
        print('__init__ of B')

    def feature4(self):
        print('feature4 is working')


class C(A, B):
    def __init__(self):
        super().__init__()
        print("__init__ of C")


c = C()