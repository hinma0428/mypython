total = 0
for i in range(1, 11):
    total += i
#end for
print('총합 01 : %d' % total)

total = 0
for i in range(1, 101, 3):
    total += i
#end for
print('총합 02 : %d' % total)

total = 0
for i in range(97, 1, -5):
    total += i
#end for
print('총합 03 : %d' % total)

total = 0
for i in range(1, 97, 5):
    total += i*i
#i**5 : i의 5승
#end for
print('총합 03 : %d' % total)

total = 0
for i in range(1, 6):
    total += i*(i+1)
#end for
print('총합 04 : %d' % total)