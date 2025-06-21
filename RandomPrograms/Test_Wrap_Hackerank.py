def wrap(string, max_width):
    count=0

    while count<len(string):
        if len(string)%max_width==0:
            print(string[count:(count+max_width)]) #L1.append(string[count:(count+max_width)])
        else:
            temp=len(string)%max_width
            if count<(len(string)-temp):
                print(string[count:(count+max_width)]) #L1.append(string[count:(count+max_width))
            else:
                print(string[count:len(string)])  #L1.append(string[count:len(string))
        count+=max_width

    # Simple using range and step range(start,end,step)

    for i in range(0, len(string)+1, max_width):
        temp=string[i:i+max_width]
        if len(temp)==max_width:
            print(temp)
        else:
           return temp



if __name__ == '__main__':
    string=input()
    max_width=int(input())

    result1=wrap(string, max_width)

    print(result1)