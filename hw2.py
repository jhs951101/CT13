print('  이름    중간  기말  총점  평균  학점')

file = open('students.txt', 'r')

while True:
    data = file.readline()

    if not data:
        break
    else:
        infos = data.strip().split(',')
        infos[1] = int(infos[1])
        infos[2] = int(infos[2])
        
        sum1 = infos[1]+infos[2]
        avg = sum1/2

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(infos[0] + '     ' + str(infos[1]) + '   ' + str(infos[2]) + '   ' + str(sum1) + '   ' + str(avg) + '   ' + grade)
        
file.close()
