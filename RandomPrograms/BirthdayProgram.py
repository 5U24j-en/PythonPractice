def findbirthday(d1):
    con= True
    while con:
        name = input("Enter name to find the birthday: ")
        if name in d1:
            print(d1[name])
        else:
            print("Record Not Found!!")
        Ans = input("Do you want to retry?(Y/N) : ").upper()
        if Ans=="N":
            con=False






if __name__ == '__main__':
    print("Welcome !. This program creates a record of user and their birthdays and search them :)")
    size=int(input("Enter number for record you want to add: "))
    d1={}
    for i in range(size):
        key=input("Enter Name: ")
        value=input("Enter Birthday(DD/MM/YYYY) : ")
        d1[key]=value

    findbirthday(d1)

