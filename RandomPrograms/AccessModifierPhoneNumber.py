class Phone:
    def __init__(self, n, p):
        self.name=n
        self.phone=p

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def update_phone(self, ph):
        self.phone=ph


if __name__=="__main__":
    obj1=Phone("david", 9123456789)
    obj2=Phone("elder", 8912345670)
    obj3=Phone("james", 7102345678)

    print(obj3.get_name())
    print(obj2.get_phone())
    print(obj1.get_name())
    print(obj1.get_phone())
    print(obj1.update_phone(9000000000))
    print(obj1.get_phone())