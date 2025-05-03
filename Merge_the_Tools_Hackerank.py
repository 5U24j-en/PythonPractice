
def merge_the_tools(string, k):
    t=[]
    x=k
    for i in range(1,len(string)+1):
        if i%k==0:
            t.append(string[i-k:i])           


    for i in t:
        final=[]
        temp=0
        while temp<len(i):
            if i[temp] not in final:
                final.append(i[temp])
            temp+=1
        for i in final:
            print(i,end="")
        print("")
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)