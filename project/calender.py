
year = int(input('연도를 입력해주세요.'))
month = int(input('달을 입력해주세요.'))

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
        case 1:
            return 31







