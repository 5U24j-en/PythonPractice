def calculate(d1):
    L1=list(dict.keys(d1))
    L2=list(dict.values(d1))
    maxi=L2[0]
    mini=L2[0]
    for x in L2:
        if len(x)>len(maxi):
            maxi=x
        if len(x)<len(mini):
            mini=x
    index_max=L2.index(maxi)
    index_min=L2.index(mini)

    max1=L1[index_max]
    min1=L1[index_min]

    print("Word with Largest meaning is: ",max1, " -> " ,d1[max1])
    print("Word with Smallest meaning is: ",min1," -> " ,d1[min1])


def MaxiMini(d1):
    keys=list(d1.keys())
    values=list(d1.values())
    length=[len(x) for x in values ]

    maximum=max(length)
    minimum=min(length)

    max_index=length.index(maximum)
    min_index=length.index(minimum)

    print("Largest: ",keys[max_index]," -> ",values[max_index])
    print("Smallest: ",keys[min_index]," -> ",values[min_index])







if __name__ == '__main__':
    n=int(input("Welcome to our program. Please enter how many Word would you like to add in the dictionary: "))
    d1={}
    for i in range(n):
        key=input("Enter the Word: ")
        value=input("Enter the meaning: ")
        d1[key]=value

    #Long method
    calculate(d1)


    con=input("Do you want to continue(Y/N) : ").upper()
    if con=='Y':
        #Easy Method
        MaxiMini(d1)

