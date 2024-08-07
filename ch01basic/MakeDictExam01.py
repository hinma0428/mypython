#dict : map과 유사
#cf) map -> put

coffees = dict() #empty dict
#dict['key'] = value

coffees['에스프레소'] = 1000
coffees['에스프레소'] = 1500 #overwrite 가능
coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마끼아또'] = 4000
print(coffees)

targetItem = '카페라떼'
bool = targetItem in coffees
print('is bool true? %s' % bool)

if bool:
    print('%s 키가 있습니다.' % targetItem)
else:
    print('%s 키가 없습니다.' % targetItem)

#핫초코가 있는지 확인하고 없으면 5000원으로 추가해 주세요.
targetItem = '핫초코'
bool = targetItem in coffees
if not bool:
#값을 부정하고자 할 때는 not을 사용함.
    coffees[targetItem] = 5000
    print('%s를 추가함.' % targetItem)

print(coffees.keys())
print(coffees.values())

targetValue = 6000
bool = targetValue in coffees.values()
if not bool:
    coffees['아이스크림'] = targetValue
    print(coffees)

listCoffee = ['바닐라라떼', '라벤더', '딸기라떼', '콜드브루']

#for(String key:listCoffee){
# 출력(key);}
for key in listCoffee:
    print(key)
for idx in range(len(listCoffee)):
    coffees[listCoffee[idx]] = (idx + 7) * 1000

#값이 없으면 null을 반환하는 게 아니라 오류가 뜨므로 예외처리 필요.
targetList = ['라벤더', '우유커피']
for key in targetList:
    try:
        price = coffees[key]
        message = '품명 : %s, 가격 : %d' % (key, price)
        print(message)
    except KeyError:
        print('%s가 존재하지 않아서 추가함.' % key)
        coffees[key] = 5000
    #end try
#end for

targetItem = '둥글레차'
price = coffees.get(targetItem, 3000)
print('품명 : %s, 가격 : %d' % (targetItem, price))

del coffees['에스프레소']

for(key, value) in coffees.items():
    message = '항목 %s의 단가는 %d원.' % (key, value)
    print(message)
#end for

#500원 인상: 카페라떼, 카푸치노
#500원 인하: 핫초코
for key in coffees.keys():
    if key == '카페라떼' or key == '카푸치노':
        #key == '카페라떼' or '카푸치노'라고 적으면 안 됨! (오류코드도 안 뜸...)
        #그냥 '카푸치노'라고만 적으면 (key == 없이 뒤에 의미있는 문자열이 붙을 시) 무조건 true로 판단됨. '핫초코'가 들어와도 True로 뱉음. 그래서 핫초코가 5500원이 되어버림.
        #if key in ('카페라떼' or '카푸치노'): <- OK
        coffees[key] += 500
    elif key == '핫초코':
        coffees[key] -= 1000
    else:
        pass
    #end if
    print('=================')
    message = '항목 %s의 단가는 %d원.' % (key, coffees[key])
    print(message)
#end for

coffees.clear()

if len(coffees) == 0:
    print('mydict is empty')
else:
    print('mydict is not empty')




#print(coffees)




