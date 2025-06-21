if __name__ == '__main__':
    N = int(input())
    L1 = []
    for i in range(0,N):
        input1 = [x for x in input().split()]
        #print(input1)
        if input1[0] == "insert":
            e = int(input1[2])
          #  print(e)
            i = int(input1[1])
            L1.insert(i,e)
           # print(i)
        elif input1[0]=="print":
            print(L1)
        elif input1[0]=="remove":
            e=int(input1[1])
            L1.remove(e)
        elif input1[0]=="append":
            e=int(input1[1])
            L1.append(e)
        elif input1[0]=="sort":
            L1.sort()
        elif input1[0]=="pop":
            L1.pop()
        elif input1[0]=="reverse":
            L1.reverse()
        else:
            input1.clear()
            continue
        input1.clear()
