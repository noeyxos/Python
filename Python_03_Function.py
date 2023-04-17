#Function

def Times(a,b):
  result = a * b
  return result
  

print(Times)

print(Times(10,20))

#메모리 주소를 확인하는 명령
print(id(Times))

globals()

myTimes = Times
print(myTimes(10,20))

print(id(myTimes))

a = 10
b = 20
def sum1(x,y):
  return  x+y

print(sum1(a,b))

#변수의 범위 

g = 10
x = 20
def sum2(x,y):
  #x = 1
  global g
  g = g+1

  return x, y   #튜플로 인식 

print(sum2(x,20))
print(g)    

#함수의 인자(Parameter)

def Times(a=10, b=20):     #디폴트 값을 지정
  return a*b

print(Times(100,200))
print(Times(100))
print(Times(b=50))
print(Times())

def connectURL(protocol='https',server='naver.com',port='80'):
  address = protocol + '://'+server+':'+port
  return address

print(connectURL(server='microsoft.com',port='80'))

# 가변인자 함수
def test(*args):  #*가 가변인자를 뜻함
  print(type(args))
  print(args)

test(1,2,3,4,5)
test(1,2,3)
