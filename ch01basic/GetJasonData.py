filename = 'jumsu.json'

myfile = open(filename, mode='rt', encoding='UTF-8')
#mode: w 덮어쓰기, a 뒤이어쓰기, rt 텍스트로 읽어와서 처리
mystring = myfile.read()
print(type(mystring))
#파이썬은 데이터 타입 알기 어려우니까 type 함수를 쓰셈
myfile.close()

import json #모듈 임포트
jsondata = json.loads(mystring)
print(type(jsondata))

humanList = list() #전체 결과를 저장할 리스트


#리스트 타입이라 for 쓸 수 있음
for human in jsondata:
    name = human['name'] #['name']은 제이슨의 콜론 좌측의 항목명(key?)
    print('이름 : %s' % name)
    kor = float(human['kor']) #형변환
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

    _gender = human['gender'].upper() #문자열을 대문자로 만드는 함수
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    print(type(human))
    if 'hello' in human.keys():
        message = human['hello']
        print(type(message))
        print('메시지 : %s' % message)
        mytuple = (name, kor, eng, math, total, gender)
    humanList.append(mytuple) #리스트 안에 튜플을 담음(리스트에 담을 때는 append)
    # average = total / 3.0
#end for

print(humanList)
