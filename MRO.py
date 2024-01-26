class A:
    def hablar(self):
        print("hola desde A")

class F:
    def hablar(self):
        print("hola desde F")
        
class B(A):
    pass
 
class C(A):
    pass

class D(B,C):
    pass
        
d = C()

B.hablar(d)
