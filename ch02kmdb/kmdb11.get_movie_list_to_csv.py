import urllib.request
import urllib.parse
import json, math

#타겟 사이트에서 발급받은 키
#pip: python installer package(?)
service_key = 'b746b9ef111c02493bcabce7495d99d1'

def getDataFromWeb(url):
#url 정보를 이용해 해당 웹사이트에서 json 데이터를 읽어옵니다.
    req = urllib.request.Request(url) #url library(url 문자열을 넣어서 요청객체 구현)
    try:
        response = urllib.request.urlopen(req) #응답객체
        # http 응답이 성공이면 200을 반환/404 not found
        if response.getcode() == 200:
            #바이트 타입을 문자열로 변환하여 반환합니다.
            return response.read().decode('UTF-8')
    except Exception as err:
        print('크롤링 실패', err, '확인 요망')
        return None
#end def getDataFromWeb

def movieExtractor(pageNumber, pageSize, thisYear): #파라미터(요청 인터페이스-요청 변수-)는 대소문자 구분!
    end_point = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'

    parameter = '?key=' + service_key
    parameter += '&CurPage=' + str(pageNumber)
    parameter += '&itemPerPage=' + str(pageSize)
    parameter += '&openStartDt=' + str(thisYear)

    movie_name = '행복의 나라'
    encoded_movie_name = urllib.parse.quote(movie_name, encoding='UTF-8')
    parameter += '&movieNm=' + encoded_movie_name

    print('[' + encoded_movie_name + ']')


    url = end_point + parameter
    # print(url)

    jsonData = getDataFromWeb(url)

    if jsonData == None:
        return None
    else:
        try:
            return json.loads(jsonData)
        except Exception as err:
            print('JSON 데이터에 문제 있음.')
            print(err)
            return None
        #end try
    #end if
# end def movieExtractor

import pandas as pd #as(alias): 별칭
#영화정보를 저장할 데이터프레임(2차원)
movieTable = pd.DataFrame()

def makeMovieTable(movieData):
    for onemovie in movieData['movieListResult']['movieList']:
        # print(onemovie['movieNm'])
        onedict = {
            '영화코드': onemovie['movieCd'],
            '영화제목': onemovie['movieNm'],
            '영어제목': onemovie['movieNmEn'],
            '제작년도': onemovie['prdtYear'],
            '개봉일자': onemovie['openDt'],
            '장/단편': onemovie['typeNm'],
            '개봉예정': onemovie['prdtStatNm'],
            '개봉국가': onemovie['nationAlt'],
            '장르': onemovie['genreAlt'],
            '대표국가': onemovie['repNationNm'],
            '대표장르': onemovie['repGenreNm']
        }
        # print(onedict)
        oneframe = pd.DataFrame(onedict, index=[0])
        print(oneframe)

        global movieTable #전역변수임을 알리기 위하여 global 키워드 사용 <-> 지역변수
        #이번에 생성된 데이터프레임 oneframe을 movieTable에 누적시킴.
        movieTable = pd.concat([movieTable, oneframe]) #concat (문자열) 결합 concatenation(연결, 연쇄, 연속)

        print('=' * 30)
# end def makeMovieTable

print('크롤링 중... 잠시만 기다려 주세요.')

startYear, endYear = 2024, 2025
pageSize = 100

for thisYear in range(startYear, endYear):
    print('%s년도 크롤링 중...' % thisYear)
    pageNumber = 1

    while True:
        movieData = movieExtractor(pageNumber, pageSize, thisYear)
        # print(movieData)

        try:
            totCnt = movieData['movieListResult']['totCnt']
        except Exception as err:
            #이번 페이지에 존재하지 않으면 다음 페이지로 넘어가세요.
            pageNumber += 1
            continue

        if pageNumber == 1:
            print('데이터 총 개수 : ' + str(totCnt)) #1페이지일 때만 전체 개수 출력.
        if totCnt == 0: #0이면 더 이상 존재하지 않는 것으로 간주.
            break

        totalPage = math.ceil(totCnt/pageSize)
        print('진행 중인 페이지 : ' + str(pageNumber) + '/' + str(totalPage))

        makeMovieTable(movieData)

        if pageNumber == 1:
            #if pageNumber == totalPage #마지막 페이지에 도달하면 끝내기
            break
        pageNumber += 1 #다음 페이지로 이동하기
    #end while
#end for

print('크롤링 완료.')
print(movieTable)
print(type(movieTable))
#pandas의 object는 객체가 아니고 문자열임.
print(movieTable.info())

#csv(comma separate value): 텍스트 형식 파일로 엑셀에서 열 수 있다.
filename = 'kmdb.get_movie_list.csv'
movieTable.to_csv(filename, index=False, encoding='UTF-8')
print(filename + ' 파일이 저장됨.')

