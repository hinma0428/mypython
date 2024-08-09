import pandas as pd
myencoding='UTF-8'

filename='./../data/kmdb_get_movie_list_100.csv'
#.현위치 ..상위폴더 /폴더구분자 (상대경로 지정방식)
dataframe=pd.read_csv(filename, encoding=myencoding)
# print(dataframe.info())

print('행 색인정보 확인')
print(dataframe.index)
print('행 색인정보 확인')
print(dataframe.columns)
print('컬럼별 데이터 유형 확인')
print(dataframe.dtypes)

# for column in dataframe.columns:
#     print(column)
#     print(dataframe[column].unique())
#     print('-'*30)
#
# print(sorted(dataframe['movieCd'].unique()))

print('숫자 형식만 필터링하기')
print('before count : ' + str(len(dataframe)))
dataframe = dataframe[dataframe['movieCd'].str.isdigit()]
print('after count : ' + str(len(dataframe)))

# print(dataframe['repGenreNm'].unique())
print('nan인 장르 제외')
print('before count : ' + str(len(dataframe)))
dataframe = dataframe[dataframe['repGenreNm'].notna()]
print('after count : ' + str(len(dataframe)))

# movieCd 열을 숫자 형식으로 변환
dataframe['movieCd'] = pd.to_numeric(dataframe['movieCd'])
print('컬럼별 데이터 유형 확인')
print(dataframe.dtypes)

# prdtYear 컬럼만 추출하기
prdtYear = dataframe['prdtYear']
print(type(prdtYear))

print('시리즈 요소 개수 확인 : ' + str(prdtYear.size))
print('형상 확인 : ' + str(prdtYear.shape))
print('len(prdtYear) : ' + str(len(prdtYear)))
print('count() : ' + str(prdtYear.count())) #non-NA만 센다
print('타입 확인 : ' + str(prdtYear.dtype))
print('누락된 데이터 있나요? : ' + str(prdtYear.hasnans))
print('모든 항목이 unique한가요? : ' + str(prdtYear.is_unique))

# print(prdtYear.value_counts()) # 중복체크 할 때 쓰면 좋은 함수

filename = './../data/kmdb_get_movie_list_100_new.csv'
dataframe.to_csv(filename, index=False, encoding='UTF-8')
print(filename + ' 파일이 저장되었습니다.')