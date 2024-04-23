# 자료형

## 문자열 포매팅
### 가장 오래된 방식 (% 기호)
```python
name = "최지웅"
age = 32

print("제 이름은 %s이고 %d살입니다." % (name, age))
```

- 이제는 잘 쓰지 않는 오래된 방식입니다. %s, %d와 같은 '포맷 스트링'이라는 것을 사용. C나 자바 등 많은 언어들에서 이와 유사한 방식으로 문자열을 포매팅 함.

### 현재 가장 많이 쓰는 방식 (format() 메소드)
```python
name = "최지웅"
age = 32

print("제 이름은 {}이고 {}살입니다.".format(name, age))
```
2020년 2월 기준, 파이썬 커뮤니티에서 가장 많이 사용하는 방식.

### 새로운 방식 (f-string)
```python
name = "최지웅"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")
```
제 이름은 최지웅이고 32살입니다.
- 파이썬 버전 3.6부터 새롭게 나온 방식. 아직 완전히 대중화되지는 않았지만 좋은 평을 받고 있기 때문에, 곧 f-string을 더 많이 사용하게 될 것 같다.

## 불대수
- 불 대수의 값 = 진리값. 
  
- 불 대수의 연산 : and, or, not
- AND : x와 y가 모두 참일때만 참.
- OR : x와 y중 하나라도 참이면 x or y 는 참.
- NOT : 참이면 거짓으로, 거짓은 참으로 만들어 줌. 
  ex) NOT 대한민국의 수도는 서울이다.(NOT True) -> 대한민국의 수도는 서울이 아니다. = False
  ex) NOT 2는 1보다 작다.(NOT False) -> 2는 1보다 작지 않다. = True

### 불린형
- 불린은 따옴표 없이 써야 함. 따옴표 쓰면 문자열이 됨.
print(True True)
print(True False)
print(False True)
print(False False)
and 일때 T,F,F,F
or 일때 T,T,T,F
not True = False, not False = Ture

## type 함수
print(type())함수를 쓰면 자료형을 알 수 있음. 3 , 3.0, "3" 
함수 또한 하나의 자료형이다. 

# 추상화
## 변수 이해하기 
x = x + 1 에서 '=' 는 '같다'의 의미가 절!대!아님. 지정 연산자(assignment operator)라고 함. 오른쪽의 값을 왼쪽 변수에 넣으라는(지정해주라는) 의미.

## 함수의 실행 순서
- 함수를 실행하다 = 호출하다.
  - 함수를 정의하는것과 실행하는것은 다름.
  - 함수 실행 : 함수명()
  - return이 없는 함수는 기본적으로 None이 반환됨. 코드상에서 함수를 통해 값을 받기 위해서는 return이 필요. return은 출력하기 위해 필요한 게 아니라 함수에서 나오는 어떤 결과 값을 받기 위해서 필요.
- python에서는 들여쓰기로 함수의 범위를 나타내므로, 들여쓰기 깊이를 맞추는 것에 매우 민감하다. 다른 언어에서는 {}를 사용해서 범위를 정하지만, python에서는 들여쓰기한 깊이가 같다면 같은 {}에 감싸져 있는 함수로 보면 됨.

### return문의 역할
- 값 돌려주기 / 함수 즉시 종료하기
- 함수에 리턴문이 없으면 리턴값이 없다는 의미에서 None이 호출됨.
- return 문에 반환할 값이 명시되지 않으면 None 을 반환.

```python
def first():
    message = "코드잇"
    return message

def second():
    message = "codeit"
    print(message)

def third():
    message = None
    print(message)
    return message
# 테스트 코드
print(first())
second()
print(third())
```
third() 함수를 호출하면 함수 본문이 실행. 그래서 print(message) 에 의해 None 이 한번 출력. 그리고 함수에 return 이 없으므로 None 이 호출한 결괏값으로 반환.

### 옵셔널 파라미터
- 파라미터에 '기본값(default value)'을 설정할 수 있음. 기본값을 설정해 두면, 함수를 호출할 때 파라미터에 값을 꼭 넘겨주지 않아도 됨. 이런 파라미터를 '옵셔널 파라미터(optional parameter)'라고 함.
- 옵셔널 파라미터는 모두 마지막에 있어야 함. 아래처럼 옵셔널 파라미터를 중간에 넣으면 오류가 발생
```python
def myself(name, nationality="한국", age):  -> def myself(name, age, nationality="한국"):이게 맞는거거
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("ㅇㅇㅇ", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
print()
myself("ㅇㅇㅇ", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때
```
### Syntactic Sugar
- 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 하는 문법을 'Syntactic Sugar'라고 함

## 변수의 scope
- scope : 변수가 사용 가능한, 유효한 범위
- 로컬 변수(local variable) : 변수를 정의한 함수 내에서만 사용 가능, 파라미터도 로컬 변수. 함수에서 변수를 사용하면, 로컬 변수를 먼저 찾고 나서 로컬 변수가 없으면 글로벌 변수를 찾음. 
- 글로벌 변수(global variable) : 모든 곳에서 사용 가능. 함수 밖에서 정의한 변수

## 상수(constant)
- 절대로 바뀌지 않음. 어떤 일이 있어도 수정하지 않겠다는 의지.  
- 모든 글자를 대문자로 씀. 이유 1) 일반 변수와 상수를 구분짓기 위해. 2) 실수를 하지 않기 위해.

## 스타일
- 이해하기 쉬운 코드 = 좋은 스타일을 가진 코드 = 가독성이 좋은 코드
- 프로그램의 목적과 숫자의 의미를 알기 쉬운 코드. 
- 변수 지정, 화이트 스페이스(띄어쓰기나 빈 줄)로 가독성 높이기
- 함께 작업하는 사람과 맞춰야 함. 스타일 가이드임!
- 파이썬은 PEP8 이라는 표준코딩 스타일 가이드가 있음. 이걸 잘 보고 따르면 됨.
- PEP 8 원본 문서(PEP 8 – Style Guide for Python Code)를 참고.[text](https://peps.python.org/pep-0008/) [text](https://pep8.org/)

```python
이름
이름 규칙
모든 변수와 함수 이름은 소문자로 쓰고, 여러 단어일 경우 _로 나눠주세요.
# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good
some_variable_name = 1

def some_function_name():
    print("Hello")

모든 상수 이름은 대문자로 쓰고, 여러 단어일 경우 _로 나눠주세요.
# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14
의미 있는 이름(변수)

# bad (의미 없는 이름)
a = 2
b = 3.14
print(b * a * a)

# good (의미 있는 이름)
radius = 2
PI = 3.14
print(PI * radius * radius)
의미 있는 이름(함수)

# bad (의미 없는 이름)
def do_something():
    print("Hello, world!")

# good (의미 있는 이름)
def say_hello():
    print("Hello, world!")

화이트 스페이스
들여쓰기
들여쓰기는 무조건 스페이스 4개를 사용하세요.
# bad (스페이스 2개)
def do_something():
  print("Hello, world!")

# bad (스페이스 8개)
i = 0
while i < 10:
        print(i)

# good (스페이스 4개)
def say_hello():
    print("Hello, world!")

함수 정의
함수 정의 위아래로 빈 줄이 두 개씩 있어야 합니다. 하지만 파일의 첫 줄이 함수 정의인 경우 해당 함수 위에는 빈 줄이 없어도 됩니다.
# bad
def a():
    print('a')
def b():
    print('b')

def c():
    print('c')

# good
def a():
    print('a')


def b():
    print('b')


def c():
    print('c')

괄호 안
괄호 바로 안에는 띄어쓰기를 하지 마세요.
# bad
spam( ham[ 1 ], { eggs: 2 } )

# good
spam(ham[1], {eggs: 2})

함수 괄호
함수를 정의하거나 호출할 때, 함수 이름과 괄호 사이에 띄어쓰기를 하지 마세요.
# bad
def spam (x):
    print (x + 2)


spam (1)

# good
def spam(x):
    print(x + 2)


spam(1)

쉼표
쉼표 앞에는 띄어쓰기를 하지 마세요.
# bad
print(x , y)

# good
print(x, y)

지정 연산자
지정 연산자 앞뒤로 띄어쓰기를 하나씩 넣어 주세요.
# bad
x=1
x    = 1

# good
x = 1

연산자
기본적으로는 연산자 앞뒤로 띄어쓰기를 하나씩 합니다.
# bad
i=i+1
submitted +=1

# good
i = i + 1
submitted += 1

하지만 연산의 '우선 순위'를 강조하기 위해서는, 연산자 앞뒤로 띄어쓰기를 붙이는 것을 권장합니다.
# bad
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# good
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

코멘트
일반 코드와 같은 줄에 코멘트를 쓸 경우, 코멘트 앞에 띄어쓰기 최소 두 개를 입력해 주세요.
# bad
x = x + 1# 코멘트

# good
x = x + 1  # 코멘트
```

- 대괄호는 리스트를 생성하거나 리스트에서 index로 접근을 할 때 사용하는 기호
- 중괄호는 딕셔너리를 생성할 때 사용


# 제어문
## while 반복문
잔디잔디

