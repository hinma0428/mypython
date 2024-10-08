coffees = set() #empty set(집합)

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노')

print(len(coffees))

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

newItem = ['콜드브루', '고구마라떼', '디카페인커피']
coffees.update(newItem)

#집합은 순서가 없으므로 인덱싱, 슬라이싱이 불가
#print(coffees[3])

print(coffees)

targetItem = '카푸치노'
bool = targetItem in coffees
print('%s 존재 : %s' % (targetItem, bool))

targetItem = '마끼아또'
if not targetItem in coffees:
    coffees.add(targetItem)
#end if

targetItem = '믹스커피'
coffees.remove(targetItem)

try:
    targetItem = '바닐라라떼'
    coffees.remove(targetItem)
except KeyError:
    print('%s는 목록에 없음.' % targetItem)

print('반복문을 사용한 출력')
for element in coffees:
    print(element)
#파이썬에서 일반 for를 쓰려면 len 어쩌구저쩌구 range 써야 함
# for idx in range(len(listCoffee)):
#     coffees[listCoffee[idx]] = (idx + 7) * 1000

coffee01 = set(['고구마라떼', '에스프레소', '아메리카노', '마끼아또'])
coffee02 = set(['아메리카노', '마끼아또', '카페라떼', '디카페인커피'])

union_set = coffee01.union(coffee02)
print('합집합01 : %s' % union_set)

union_set = coffee01 | coffee02
print('합집합02 : %s' % union_set)

intersection_set = coffee01.intersection(coffee02)
print('교집합01 : %s' % intersection_set)

intersection_set = coffee01 & coffee02
print('교집합02 : %s' % intersection_set)

difference_set_01 = coffee01.difference(coffee02)
print('차집합01 : %s' % difference_set_01)

difference_set_02 = coffee02 - coffee01
print('차집합02 : %s' % difference_set_02)

symmetric_difference_set = coffee01.symmetric_difference(coffee02)
print('차집합들의 합집합 : %s' % symmetric_difference_set)

super_set = set(['고구마라떼', '에스프레소', '아메리카노', '마끼아또'])
sub_set_01 = set(['고구마라떼', '에스프레소'])
sub_set_02 = set(['바닐라라떼', '마끼아또'])
boolTest = sub_set_01.issubset(super_set)
if boolTest:
    print('집합01은 수퍼집합의 부분집합임.')
else:
    print('집합01은 수퍼집합의 부분집합이 아님.')
boolTest = super_set.issuperset(sub_set_02)
if boolTest:
    print('수퍼집합은 집합02의 상위집합임.')
else:
    print('수퍼집합은 집합02의 상위집합이 아님.')