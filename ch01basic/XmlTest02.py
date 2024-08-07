from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {
    'kong':('꽁치', 60, 80, 70),
    'nuri':('누리', 50, 70, 95),
    'gori':('고리', 100, 100, 100),
    'hyva':('휘바', 90, 80, 50)
}
print(mydict)

#ctrl + space
xmlData = Element('students') #루트 엘리먼트

for key, mytuple in mydict.items():
    # print('key : %s' % key)
    # print(mytuple)
    cat = SubElement(xmlData, 'student')
    cat.attrib['id'] = key #키의 속성(?)

    kor = mytuple[1]
    eng = mytuple[2]
    math = mytuple[3]

    total = kor + eng + math
    average = total / 3.0

    cat.attrib['총점'] = str(total)
    cat.attrib['평균'] = '%.3f' % average

    SubElement(cat, '이름').text = mytuple[0]
    SubElement(cat, '국어').text = str(kor)
    SubElement(cat, '영어').text = str(eng)
    SubElement(cat, '수학').text = str(math)
#end for
def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def

indent(xmlData)

# <tag>속성 attribute </tag>
xmlFile = 'xmlTest_02.xml'
ElementTree(xmlData).write(xmlFile, encoding='UTF-8')
print(xmlFile + ' 파일이 생성됨.')