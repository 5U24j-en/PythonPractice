if __name__ == '__main__':
    s = input()
    print(any(item.islower() for item in s))