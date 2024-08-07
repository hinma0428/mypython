from xml.etree.ElementTree import parse

tree = parse(source='Car_info.xml')

myroot = tree.getroot() #Tree : 최상위
print(type(myroot))

carList = myroot.findall('car') #findall의 반환타입 리스트
print(type(carList))
print('총 car 수 : %d' % len(carList))

for currCar in carList: #currCar = <car>
    print('car 구성 정보')
    brand = currCar[0].text
    brandName = currCar[0].attrib['name']
    model = currCar[1].text
    year = currCar[2].text
    color = currCar[3].text

    print('브랜드 : %s' % (brand))
    print('브랜드 이름 : %s' % (brandName))
    print('모델 : %s' % (model))
    print('출시년도 : %s' % (year))
    print('색상 : %s' % (color))
    print('-' * 30) #하이픈 30개 출력

#end for