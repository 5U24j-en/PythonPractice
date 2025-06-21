class Calculator:

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def subs(a,b):
        return a-b

    @staticmethod
    def mul(a,b):
        return a*b

    @staticmethod
    def div(a,b):
        return a/b


if __name__=="__main__":

    print(Calculator.add(5,5))
    print(Calculator.subs(5,5))

