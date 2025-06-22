


class AccountBalanceException(Exception):
    pass


class Account:

    count=0
    obj = []
    list_names = []


    def __init__(self, xname, xbal):

            self.accID=Account.count+2001
            self.name = xname
            self.accBalance = xbal
            print("New Work Object created ",id(self))
            Account.count+=1

    @property
    def accBalance(self):
        return self._accBalance


    @accBalance.setter
    def accBalance(self, xbal):
        if xbal<5000:
            self._accBalance=xbal
            raise AccountBalanceException("ALERT! Balance less than 5000.")
        else:
            self._accBalance=xbal

    def showdetails(self):
        print("Name: ",self.name)
        print("Account Number: ", self.accID)
        print("Balance: ",self.accBalance)


    @classmethod
    def addAccount(cls):
        while True:
            cls.n = input("Enter the number of accounts you want to add: ")
            try:
                cls.n = int(cls.n)
                break
            except Exception as e:
                print("Invalid Input Try Again --->ERROR == ", e)


        for i in range(cls.n):
            while True:
                cls.tname = str(input("Enter name: "))
                if all(x.isalpha() for x in cls.tname.split()):
                    break
                else:
                    print("Invalid Name ")

            Account.list_names.append(cls.tname)
            while True:
                try:
                    cls.tbal = int(input("Enter Deposit Balance: "))
                    Account.obj.append(Account(cls.tname, cls.tbal))
                    break

                except Exception as e:
                    print("Invalid Input!! Try Again   ",e)


        print(cls.obj)
        print(Account.count)
        print("Action End")



    def withdraw(self, xwithdraw):
        try:
            self.accBalance-=xwithdraw
        except Exception as e:
            print("WARNING ",e,"Balance = ",self.accBalance)

        else:
            print("New Balance = ",self.accBalance)
        finally:
            print("Event Completed")

    def deposit(self, xdeposit):
        try:
            self.accBalance+=xdeposit
            print("New Balance = ", self.accBalance)
        except Exception as e:
            raise e
        finally:
            print("Event Completed")


if __name__=="__main__":

    print("<==== WELCOME TO BANK PROGRAM ====>\n\n")

    var_try='y'
    while True:

        print("1.)  Add Accounts")
        print("2.) Show Account Details")
        print("3.) Withdraw Money")
        print("4.) Deposit Money\n\n")

        while True:
            try:
                ch = input("Enter your choice: (1/2/3/4): ")
                if ch=='1':
                    while True:
                        try:
                            ch2 = input("Do you want to add account:(y/n)").strip().lower()
                            if ch2 == 'n':
                                print("You selected No. Action Ended")
                                break
                            elif ch2 == 'y':
                                Account.addAccount()

                                break
                            else:
                                print("Invalid Input!! Try Again ")
                                continue

                        except Exception as e:
                            print(e, "Invalid Input Try Again ")

                    break


                elif ch=='2':
                    llb=0

                    while True:
                        name_show = input("Enter the name: ")
                        if llb==0:

                            for x in Account.list_names:
                                if x==name_show:
                                    i=Account.list_names.index(name_show)
                                    Account.obj[i].showdetails()
                                    llb=1
                                    break
                            if llb==0:
                                print("Account Not Found")
                            break

                    break

                elif ch=='3':
                    while True:
                        try:
                            name_1=input("Enter the name: ")
                            amt=int(input("Enter the Amount: "))
                            if amt<0:
                                print("Invalid Input. Please Enter Positive Amount")
                            else:
                                xyz=0
                                for x in Account.list_names:
                                      if x==name_1:
                                          i = Account.list_names.index(name_1)
                                          Account.obj[i].withdraw(amt)
                                          xyz=1
                                          break
                                if xyz==0:
                                    print("Account Not found")
                                break
                        except Exception as e:
                            print("Invalid Input!! Try Again   ERROR ==> ",e)


                    break
                elif ch=='4':
                    while True:
                        try:
                            name_1=input("Enter the name: ")
                            amt=int(input("Enter the Amount: "))
                            if amt<0:
                                print("Invalid Input. Please Enter Positive Amount")
                            else:
                                xyz=0
                                for x in Account.list_names:
                                      if x==name_1:
                                          i = Account.list_names.index(name_1)
                                          Account.obj[i].deposit(amt)
                                          xyz=1
                                          break
                                if xyz==0:
                                    print("Account Not found")
                                break
                        except Exception as e:
                            print("Invalid Input!! Try Again   ERROR ==> ",e)



                    break
                else:
                    print("Invalid Input!!! TRY AGAIN ")

            except Exception as e:
                print(e)

        try:
            var_try=input("Do you want to continue(y/s)? : ").strip().lower()
            if var_try=='n':
                print("Thank you!! Program Ended")
                break
            elif var_try=='y':
                print("your choice was y \n")
            else:
                print("Invalid Input!! Please try again")

        except Exception as e:
            print(e)





















