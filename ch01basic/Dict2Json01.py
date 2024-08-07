
#사전의 중첩
humanDict = {
    'age' : 10, 'name' : '꽁치', 'hobby' : '누워 있기', 'address' : {'city' : 'seoul', 'gu' : '은평구', 'zipcode' : '12345'}
}

print(type(humanDict))
print(humanDict)

import json
humanString = json.dumps(humanDict, ensure_ascii=False) #dump는 사전 형식을 문자열로 변환할 때
print(type(humanString))
print(humanString)

humanJson = json.loads(humanString) #문자열을 제이슨으로 변환
print('이름 : %s' % humanJson['name'])
print('취미 : %s' % humanJson['hobby'])
print('나이 : %s' % humanJson['age'])
print('시도 : %s' % humanJson['address']['city']) #중첩 데이터 호출
print('군구 : %s' % humanJson['address']['gu'])
print('우편번호 : %s' % humanJson['address']['zipcode'])
