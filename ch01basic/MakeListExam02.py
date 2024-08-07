#리스트, 튜플, 사전, 세트

#coffees = [] #empty list

coffees = list()
coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인커피')
coffees.append('카페라떼')

count = len(coffees)

#indexing
print('요소 개수 : %d' % count)
print('앞에서 2번째 음료 : %s' % coffees[2])
print('뒤에서 1번째 음료 : %s' % coffees[-1])

#slicing : 순서가 있는 건(sequence, 리스트/튜플/문자열) 전부 슬라이싱 가능
print('1~3번째 음료 : %s' % coffees[1:4]) #zero base
print('3번째 이후 모든 음료 : %s' % coffees[3:])
print('0~2번째 모든 음료 : %s' % coffees[:3])

print('모든 음료 : %s' % coffees[::])

print('#오름차순 asc')
coffees.sort()
print(coffees)

print('#내림차순 desc')
coffees.sort(reverse=True)
print(coffees)

import random
random.shuffle(coffees)
print(coffees)