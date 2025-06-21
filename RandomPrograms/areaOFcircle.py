import math

class Circle:

    def __init__(self, r):
        self.radius=float(r)

    def area(self):
        return math.pi*self.radius*self.radius

    def perimeter(self):
        return math.pi*2*self.radius



if __name__=="__main__":
    ra=input()
    act=Circle(ra)
    print(act.area())
    print(act.perimeter())