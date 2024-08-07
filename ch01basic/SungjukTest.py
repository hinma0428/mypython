def sunjukInfo(name, kor, eng = 50, math = 60): #매개변수의 디폴트값 지정
    #파이썬엔 디폴트값을 지정할 수 있으므로 오버로딩/오버라이딩 개념이 없다
    total = kor + eng + math
    average = total / 3.0
    if average >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'

    print('%s 학생의 정보' % name)
    print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
    print('총점 : %d, 평균 : %.2f, 합격 여부 : %s' % (total, average, passOrFail))
#end def

name, kor, eng, math = '김철수', 50, 60, 70
sunjukInfo(name, kor, eng, math) #positional argument
sunjukInfo('박영희', 80)

sunjukInfo(math=30, eng=90, name='심현철', kor=100) #keyword argument
sunjukInfo('권유정', 50, math=70) #방식을 혼합할 때는 positional을 우선해 쓴다.