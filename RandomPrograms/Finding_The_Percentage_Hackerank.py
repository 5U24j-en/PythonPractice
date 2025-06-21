
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    L2= list(student_marks.keys())
    count=0
    sum1=0
    for x,y in student_marks.items():
        if query_name==x:
            for i in y:
                sum1+=i
                count+=1
            avg=sum1/count
            print("{:.2f}".format(avg))


    # Simple Solution --> student_marks is a Dictionary and Use sum function

    print("{:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))