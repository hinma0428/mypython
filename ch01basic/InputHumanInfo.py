print('이름 입력 : ', end='')
name = input()
age = int(input('나이 입력 : '))
# input 함수는 반환타입이 문자열입니다.
height = float(input('키 입력 : '))
print('% 포맷 코드로 출력')
print('이름 : %s' % name)
print('나이 : %d' % age)
print('키 : %.2f' % height)

print('문자열 함수 format() 사용')
message = '내 이름은 {}이고, 나이는 {}세입니다.\n제 키는 {}cm입니다.'
print(message.format(name, age, height))

import datetime
x = datetime.datetime.now()
print(x)