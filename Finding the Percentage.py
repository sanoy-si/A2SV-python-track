if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print('%.2f'%(sum(student_marks[input()])/len(list(student_marks.items())[0][1])))
    
    
