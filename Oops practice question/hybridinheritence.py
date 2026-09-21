#basic exapmle
class A:
    def show_a(self):
        print("Class A")


class B(A):
    def show_b(self):
        print("Class B")


class C(A):
    def show_c(self):
        print("Class C")


class D(B, C):
    def show_d(self):
        print("Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()




#MRO
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


obj = D()
obj.show()

print(D.mro())

#super with hybrid

class A:
    def show(self):
        print("A")
        super().show()


class B(A):
    def show(self):
        print("B")
        super().show()


class C(A):
    def show(self):
        print("C")
        super().show()


class D(B, C):
    def show(self):
        print("D")
        super().show()


class X:
    def show(self):
        print("X")


obj = D()