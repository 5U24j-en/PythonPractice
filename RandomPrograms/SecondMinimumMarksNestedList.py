if __name__ == '__main__':
    records=[[input("Enter Student Name: "), float(input("Enter the marks: "))] for x in range(int(input("Enter Number of records you want to add: ")))]

    d1 = dict(records)
    Name = list(d1.keys())
    Marks = list(d1.values())

    Sorted_marks = list(set(Marks))
    Sorted_marks.sort()
    Second_minimum = Sorted_marks[1]

    L1 = []

    for x in records:
        if x[1] == Second_minimum:
            L1.append(x[0])

    L1.sort()
    for x in L1:
        print(x)