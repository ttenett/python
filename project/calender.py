
year = int(input('달력을 보고싶은 연도를 입력해주세요.'))
month = int(input('달력을 보고싶은 월을 입력해주세요.'))

# 입력받은 연도 윤년여부 판단
def leaf_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leaf_year = True
        else:
            leaf_year = True

# 입력받은 월의 날짜 판단 - 30, 31, 28
def what_month(month):
    match month:
        case 1, 3, 5, 7, 8, 10, 12:
            return 31
        case 4, 6, 9, 11:
            return 30
        case 2:
            if leaf_year == True:
                return 29
            else:
                return 28

# 달력 날짜 출력하기
for i in range(1, what_month(month)+1):
    print(i)







