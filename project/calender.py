import datetime

year = int(input('달력을 보고싶은 연도를 입력해주세요.'))
month = int(input('달력을 보고싶은 월을 입력해주세요.'))


# 입력받은 연도 윤년여부 판단
def is_leaf_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 입력받은 월의 마지막 날짜 판단 - 30, 31, 28
def what_lastday(year, month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            if is_leaf_year(year):
                return 29
            else:
                return 28

# 달력 출력하기

day_of_week = '일 월 화 수 목 금 토'
print('====================')
print(f'    {year}년  {month}월     ')
print('====================')
print(day_of_week)

days = what_lastday(year, month)
for i in range(1, days + 1):
    print(i, end=' ')

# weekday() 써서 업데이트 해보기
now = datetime.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

first_day = datetime.date(year, month, 1).weekday()  

# 첫번째주 출력해보기
print('    ' * first_day, end='')  # 첫 번째 날짜 전까지 공백 추가
for day in range(1, 8 - first_day + 1):  # 첫 주의 날짜 출력
    print(f'{day:2}', end=' ')

# if __name__ == '__main__':
#     main()

# print(f'{year:^10}년 {month:^10}월') ->    2025   년     2     월



