with open('students.txt', 'w') as file:
    for n in range(0, 5, 1):
        name = input('이름 입력 : ')
        mid = input('중간고사 점수 : ')
        final = input('기말고사 점수 : ')
        
        file.write('%s, %s, %s\n' %(name, mid, final))
