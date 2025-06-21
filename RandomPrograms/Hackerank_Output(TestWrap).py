


def wrap(string, max_width):
    count = 0
    L1 = []
    while count < len(string):
        if len(string) % max_width == 0:
            L1.append(string[count:(count + max_width)])
            print(string[count:(count + max_width)])
        else:
            temp = len(string) % max_width
            if count < (len(string) - temp):
                L1.append(string[count:(count + max_width)])
                print(string[count:(count + max_width)])
            else:
                L1.append(string[count:len(string)])
        count += max_width

    return L1[-1]




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)