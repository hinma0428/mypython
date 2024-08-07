coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')
#요소들을 콤마로 연결하면, tuple로 인식합니다.

coffee03 = ('카푸치노', '마끼아또')

mytuple = coffee01 * 3
print(mytuple)

mylist = ['바닐라라떼', '플랫화이트']
coffee04 = tuple(mylist) #리스트를 튜플로 변환(역도 가능)

coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
#에스프레소 끝에 콤마 안 적으면 안 됨~~~
length = len(coffees)
print('요소 개수 : %d개' % length)
print(type(coffees))
print(coffees)

#coffees[1] = '우유'
#튜플은 아이템 할당 후 편집할 수 없다. (불변성)

#인덱싱과 슬라이싱
print('앞에서 3번째 요소 : %s' % coffees[3])
print('뒤에서 2번째 요소 : %s' % coffees[-2])

print('1~3번째 요소들 : ', end = '')
print(coffees[1:4])

print('4번째 이후 요소들 : ', end = '')
print(coffees[4:])

print('3번째까지의 요소들 : ', end = '')
print(coffees[:4])

mycount = coffees.count('아메리카노')
print(mycount)

myindex = coffees.index('콜드브루')
print(myindex) #제로 베이스!!

print('swap')
x, y = 3, 4
print('before x : %d, y : %d' % (x, y))
x, y = y, x
print('after x : %d, y : %d' % (x, y))