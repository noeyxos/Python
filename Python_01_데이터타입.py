print('Hello World')

# 변수 규칙
a = 1
b = 2
#2a = 3 항상 변수는 문자로 시작해야 한다. 
student_count= 100 # 가급적 풀 워드로 짓는다.
address = ''       # 가급적 정확한 영어로 짓는다. 
print(a * b, student_count)

# 대소문자를 구별한다. 
friend = 1
Friend = 10
print(friend)

# 예약어는 사용할 수 없다. 
for = 1

# 숫자형 
year = 2023
month = 4
print(year, month)

year = 2023
print(type(year)) # type() 데이터의 타입을 확인하는 함수
year = '이천이십삼년'
print(type(year))

# 8진수
# 정수 앞에 0o를 붙이면 8진수
print(0o10)
# 정수 앞에 0b를 붙이면 2진수
# 정수 앞에 0x를 붙이면 16진수
print(0b10)
print(0x10)

# 다음은 10진수를 받아서 각 진수로 변환하는 방법 (결과가 문자형)

print(oct(38))  # 10진수 38을 8진수로 변환
print(hex(38))  # 10진수 38을 16진수로 변환
print(bin(38))  # 10진수 38을 2진수로 변환

# 파이썬의 정수 타입
print(type(1))      #int
print(type(2**31))  #2의 31승 파이썬 3.0 int 형으로 정수형 통합

# 실수의 표현
print(type(3.14))
print(type(314e-2))
print(type(3 - 4j))    # 복소수
x = 3 - 4j
print(x.imag)         # imag는 허수부
print(x.real)         # real는 실수부
print(x.conjugate())  # conjuage는 켤레 복소수 확인

# 원의 넓이와 삼각형 넓이 구하기
r = 2
circle_area = (r ** 2) * 3.14
print(circle_area)

x = 3
y = 4
triangle_area = x * y / 2
print(triangle_area)

# 문자형 실습
print('Hello World')
print("Hello World")
print("Welcome to 'Python World'")

print('''
항상 태양을 바라보아라
그리하면 너는 그림자를 볼 수 없을 것이다. 

              - 헬렌켈러
''')

print('\t탭 \n다음줄')

print('py' 'thon')
print('py' + 'thon')

print('py' * 3)

a = 'Python'

print(a[0])
print(a[0+1])
print(a[2])

a[0] = 'A' # index read-only 속성이라 수정은 불가능합니다.

# index를 이용해서 범위를 설정할 수 있다. 
print(a[0:1])
print(a[1:4])
print(a[:2])      #생략은 해당 방향의 끝을 나타낸다.
print(a[2:])
print(a[-2:])
print(a[:])
print(a[::2])

# 데이터 타입의 변환
print(str(3.14))      # 문자형으로 변환
print(int('49'))      # 정수형으로 변환
print(float(23))      # 실수형으로 변환
