# 조건에 따라서 다른 결과를 얻기위해서 사용하는 것

value  = 10
if value > 5:
  print('value is bigger than 5')

money = 10
if money > 100:
  item = 'apple'
else:
    item = 'banana'

print(item)

#성적처리 

score = int(input(('input your score: ')))

if 90 <= score <=100:
  grade = 'A'
elif 80 <= score < 90 :
  grade = 'B'
elif 70 <= score < 80 :
  grade = 'C'
elif 60 <= score < 70 :
  grade = 'D'
else: 
  grade = 'F'

print ('Your score is ' + str(score))
print ('Your grade is ' + grade)

# 조건식의 참과 거짓

print(bool(True))
print(bool(False))
print(bool(123))
print(bool(0))
print(bool(-1))
print(bool('APPLE'))
print(bool(''))   #string인데 내용이 없는 경우
print(bool())     #아예 아무것도 없는 경우

#반복문 (while and for)

value = 5
while value> 0:
  print(value)
  value -= 1

l = ['apple', 100, 15.23]

for i in l:
  print (i)

loop1 = [2,3,4,5,6,7,8,9]
loop2 = [1,2,3,4,5,6,7,8,9]

for i in loop2:
  print("2 * {0} = {1}".format(i,i*2))


#과제
#9단까지 도는 루프
loop1 = [2,3,4,5,6,7,8,9]
loop2 = [1,2,3,4,5,6,7,8,9]

for i in loop1:
  print('{0}단 - '.format(i))
  for j in loop2:
    print("{0} * {1} = {2}".format(i,j,i*j))


L = [1,2,3,4,5,6,7,8,9,10]

#break문을 사용하면 반복문을 중간에 멈출 수 있습니다. 

for i in L :
  if i>5:
    break
  print('Item: {0}'.format(i))

#continue문을 사용하면 해당 반복만 건너뛴다.
for i in L:
  if i % 2 == 0:
    continue
  print('Item: {0}'.format(i))

#range 함수를 사용하면 특정 범위의 숫자를 생성할 수 있다.
print(list(range(10)))
print(list(range(5,10)))    #range(시작, 끝)  끝 앞에서 끝나는 것 주의  
print(list(range(10,0,-1)))    #range(시작, 끝, 증가값)
print(list(range(0,10,2)))    

L = ['apple','orange','banana']

for i in L:
  print(i)


l = list(range(1,6))

[i**2 for i in l]
