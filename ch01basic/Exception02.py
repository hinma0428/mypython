def girlFriendCheck(findName):
    girlFriend = ['은하', '소원', '유주', '예린', '신비', '엄지']
    isMember = findName in girlFriend #in <- 조건식에 사용
    if isMember:
        message = '\"%s\" 님은 여자친구 멤버입니다.' % findName
        print(message)
    else:
        message = '\"%s\" 님은 여자친구 멤버가 아님.' % findName
        raise Exception(message)
#end def

name = '윤종신'

try:
    girlFriendCheck(name) #positional argument
except Exception as err:
    print('예외 발생 : {}'.format(err))
