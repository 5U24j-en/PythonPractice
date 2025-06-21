class NegativeAge(Exception):

    def __init__(self):
        self.msg="ERROR. Invalid Input ( Negative Age )"

    def __str__(self):
        return self.msg


class Age:

    def __init__(self, a):
        self.age=a

    def showage(self):
        try:
            if self.age<0:
                raise NegativeAge
        except Exception as e:
            raise e

        else:
            if self.age >= 0 and self.age < 13:
                return "Kid"
            elif self.age >= 13 and self.age <=19:
                return "Teen"
            elif self.age > 19 and self.age <= 50:
                return "Young"
            else:
                return "Old"
        finally:
            print("End of Function")

if __name__=="__main__":
    try:
        x=int(input("Age: "))
        obj=Age(x)
        print(obj.showage())
    except NegativeAge as e:
        print(e)










