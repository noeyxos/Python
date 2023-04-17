# List 
colors =['red','green','gold']
print(colors)
print(type(colors))

colors.append('blue')
print(colors)

colors.insert(1,'black')
print(colors)

colors.extend(['white','gray'])
print(colors)

colors += ['red'] #colors = colors + ['red']와 같음
print (colors) 

#실수하지 말 것 
colors += 'red' #[]없으면 결과값이 달라짐
print(colors)

print(colors.index('red'))
print(colors.index('red', 1))
print(colors.count('red'))

colors.pop()

colors.pop()

colors.pop(1)

print(colors)

#remove는 해당 값을 삭제 할 수 있습니다.
colors.remove('gold')
print(colors)

#sort는 알파벳 순서대로 정렬한다. 
colors.sort()
print(colors)
colors.reverse()
print(colors)

# 세트(set)
a = {1,2,3}
b = {3,4,5}

print(a,b)
print(type(a))

# 합집합, 교집합을 구할 수 있다.
print(a.union(b))         #합집합
print(a.intersection(b))  #교집합

print(a-b)    #차집합
print(a|b)    #합집합
print(a&b)    #교집합

#튜플(tuple)
t = (1,2,3)
print(type(t))

a,b = 1, 2  #파이썬에서는 (a,b) = (1,2)와 같음 
print(a,b)

a = 10
b = 20
(a,b) = (b,a) #괄호 없어도 동작 가능
print(a,b)

#타입의 전환도 무척 간단하다.
a = set((1,2,3))
print(type(a))
b = list(a)
print(type(b))
c = tuple(b)
print(type(c))
d = set(c)
print(type(d))

# in 연산자를 통해서 해당 값이 있는지 확인 가능하다.
a = set((1,2,3))
print(1 in a )  #(1이 a안에 있는가?)in 연산자는 데이터 타입에 상관없이 사용할 수 있다.

# 사전(Dictionary)

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#dict()함수는 생략이 가능하다
color ={'apple':'red','banana':'yellow'}
print(color)


print(color['apple'])
#print(color[0])   #dict타입은 인덱스가 없다! (오류발생)
#print(color['cherry'])  #dict안에 없는 것을 물어도 예외가 발생된다.  

color['cherry'] = 'red' #key가 없으면 추가를 해주고
print(color)

color['apple'] = 'green'  #key가 기존에 있으면 업데이트를 해준다. ( key는 중복 불가)
print(color)

print(color.keys())
print(color.values())
print(color.items())

# for 문을 사용해서 데이터 가져와보기
for k in color.keys():
  print(k)
for v in color.values():
  print(v)
for i in color.items(): #바로 튜플로 받아서 튜플로 출력하는게 가능
  print(i)
for (k,v) in color.items(): 
  print(k,v)


# Dict 에서 불필요한 아이템의 삭제 

del color['cherry']
print(color)

color.clear()
print(color)

#데이터 타입은 서로 혼용해서 사용하는 것이 가능하다.
d = {'age': 40.5 , 'job': [1,2,3], 'name':{'kim':2},'cho':1}
print(d)


#bool 타입 
isRight = False
print(type(isRight))

print(1<2)
print(1==2)
print(1!=2)

#논리 연산자
print(True and False)
print(True & True)
print(True or False)
print(True | False)
print(not True)

# 얕은 복사와 깊은 복사 
# call by reference 와 call by value
a = [1,2,3]
b = a
print(b)

a[0] = 38
print(a)
print(b)  #변수가 할당된 주소를 복사해오기 때문에 b도 같이 값이 변함

# Call by value
a = [1,2,3]
b = a[:]    #주소가 아닌것을 할당받을 때 이렇게 명시해야한다
a[0] = 38
print(a,b)

# copy module 을 사용하는 법
import copy

a = [1,2,3]
b = copy.deepcopy(a)  #b=a[:]깊은 복사 방법   
a[0] = 38
print(a,b)
