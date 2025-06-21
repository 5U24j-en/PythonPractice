class Account:

    call_count=0                                        # Class Variable

    def __init__(self, paramID=1000, bal=0, a=18):        #self -- Instance Variable
        print("self value: ",id(self))
        self.AccID=paramID
        self.__balance=bal                              #Private Variable
        self._age1=a                                    #Protected Variable
        Account.call_count+=1                           #Class variable called using Class name

    def display(self):
        print(self.__balance)


    @classmethod                                        #Class method
    def count_func(cls):
        return cls.call_count

    @staticmethod                                       #static method
    def eligibility(bal,a):
        if bal>=100 and a>=18:
            print("eligible")
        else:
            print("Not eligible")
    @property                                           #property Method
    def age1(self):
        return self._age1

    @age1.setter                                        #property method validation function
    def age1(self, a):
        if int(a)<= 18:
            self._age1=18
        else:
            self._age1=a

class AccAction(Account):                               #Child Class
    def __init__(self, paramID, bal, a, act):
        super().__init__(paramID, bal, a)
        self.action=act

    def show(self):
        print(self.action)
        print(self.AccID)







if __name__=="__main__":
    r1=Account()

    r2=Account(1005,5000,19)


    Account.eligibility(1001, 18)           #Static Method Call
    Account.eligibility(1000, 4)            #Static Method Call
    Account.eligibility(10, 20)             #Static Method Call

    r3=Account(1006, 5000, 3)
    r3.age1=-10
    print(r3.age1)
    r3.age1=20
    print(r3.age1)

    print(Account.count_func())                     #calling a class method

    c1=AccAction(1006, 5001, 19,"add")
    c1.show()