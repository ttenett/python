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
```python
while 조건 부분: # 그 명령을 실행하기 위한 조건
    수행 부분 # 반복적으로 실행하고 싶은 명령들
```
- 조건 부분 : 불린 값으로 계산되는 식. x < 3
- 수행 부분 : 반복적으로 출력 또는 변수 수정 등. i = i + 1
- 조건 부분이 True 수행부분을 계속 반복함. 수행부분은 반드시 들여쓰기를 해야 함.

```python
i = 1
while i <= 3:
    print("나는 잘생겼다!)
    i += 1
```
- 만약 동일한 print를 4번 실행하고 싶을 경우, 조건문을 시작하기 전 변수 i에 정수 1을 지정함. 그리고 수행 부분에서 변수의 값을 1씩 늘려줌.

문제 희안하게 품

Q. while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력해 보세요.
```python
내답ㅋㅋㅋㅋㅋ;;
jjaksu = 0
i = 1
while i <= 50:
    jjaksu += 2
    print(jjaksu)
    i += 1

모범답
i = 1
while i <= 50:
    print(i * 2)
    i += 1
```

Q2. while문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
```python
n = 1
while 116 > i >= 100:
    
    i = (n *= 23)
    print(i)
해당 코드에서 발생하는 문제는 i = (n *= 23) 부분에 있습니다. Python에서는 *=와 같은 복합 할당 연산자를 사용할 때, 이를 표현식의 일부로 사용할 수 없습니다. 즉, 복합 할당 연산자는 단독으로 사용되어야 하며, 다른 표현식의 일부로 사용될 수 없습니다. 또한, 코드에서 i 변수가 초기화되지 않았으며, while 루프의 조건이 올바르게 설정되지 않았습니다.

수정된 코드는 다음과 같습니다:


n = 1
i = 0  # i를 초기화합니다.
while 116 > i >= 100:
    n *= 23  # n을 23배 합니다.
    i = n  # i에 n의 값을 할당합니다.
    print(i)
하지만, 위 코드는 여전히 while 루프의 조건 116 > i >= 100 때문에 루프가 시작되지 않습니다. i가 초기에 0으로 설정되어 있고, 이 조건을 만족하는 i의 값으로 업데이트되지 않기 때문입니다. 코드의 의도에 따라 조건을 수정하거나 다른 접근 방식을 고려해야 할 수 있습니다.

예를 들어, 단순히 n의 값을 23배씩 증가시키면서 특정 범위 내의 값을 출력하려는 경우, 다음과 같이 코드를 수정할 수 있습니다:


n = 1
while n < 116:  # n이 116보다 작은 동안 반복합니다.
    n *= 23  # n을 23배 합니다.
    if n >= 100:  # n이 100 이상인 경우에만 출력합니다.
        print(n)
이 코드는 n이 116보다 작은 동안 n을 23배씩 증가시키고, n이 100 이상일 때만 값을 출력합니다.

100 이상의 자연수 중 가장 작은 23의 배수를 출력하려고 하는데요.

일단 배수란 무엇일까요? 23의 배수는 23으로 나누어떨어지는 수입니다. 즉 i를 23으로 나눈 나머지(i % 23)가 0이 될 것이라는 의미입니다.

그러면 우리는 무엇을 해야 할까요? 100이 23으로 나누어떨어지는지 확인하고, 101이 23으로 나누어떨어지는지 확인하고, 102가 23으로 나누어떨어지는지 확인하고... 이런 식으로 100부터 시작해서 23으로 나누어떨어지는 수가 있을 때까지 계속 1씩 늘리면서 확인하면 됩니다.

i를 23으로 나눈 나머지(i % 23)가 0이 될 때까지 while문을 반복하면 됩니다. 코드로 표현해 볼게요.

i를 23으로 나눈 나머지가 0이 아닐 동안


while i % 23 != 0
i를 1씩 늘린다


i += 1
모범 답안

i = 100
while i % 23 != 0:
    i += 1

print(i)
```

## if문
- while문과 동일하게 조건부분과 실행부분이 있음.
```python
while 다운로드 안 받은 이미지가 있다:
    다음 이미지를 본다
    if 이미지가 png인 파일이다:
        이미지를 다운로드 받는다
    else:
        print("png가 아닙니다!")
```
- else + if : elif 문, 조건문 밑에 조건문을 추가하고 싶을때 사용.

# 프로그래밍과 데이터 in파이썬
- index : 리스트에서 요소의 위치. 리스트는 0부터 시작한다. print(변수명[0])
- indexing : 인덱스를 통해 요소를 받아오는 것. 
- numbers[-1] : 오른쪽 끝 마지막 숫자부터 -1, -2, -3 순서임.
- len(numbers): length, 리스트의 개수 출력함
- del numbers[3] : delete 3번 인덱스 삭제
- numbers.append(3) : 추가 연산, 리스트의 오른쪽에 요소를 추가해줌. 무조건 제일 오른쪽에 추가.
- numbers.insert(4, 3) : 삽입 연산, numbers 4번 인덱스에 37을 삽입. 원하는 위치에 값을 넣을 수 있음. 원래 있던 값들은 오른쪽으로 한칸씩 밀려남. 