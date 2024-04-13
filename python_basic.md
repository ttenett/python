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
