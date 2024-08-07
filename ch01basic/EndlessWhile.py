import random
answer = random.randint(1,100)
print('정답 : %d' % answer)
counter = 0

while True:
    su = int(input('1~100 정수 1개 입력 : '))
    counter += 1
    if answer > su:
        print('%d보다 큰 수입니다.' % su)
    elif answer < su:
        print('%d보다 작은 수입니다.' % su)
    else:
        print('정답.')
        break
    #end if
#end while
print('%d번 만에 맞힘.' % counter)