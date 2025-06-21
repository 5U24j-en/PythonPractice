def count_substring(string, sub_string):
    i=0
    x=0
    lstring=len(string)
    l=len(sub_string)
    while l<=lstring:
        temp=string[i:l]
        if temp==sub_string:
            x+=1
        i+=1
        l+=1



    return x


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)