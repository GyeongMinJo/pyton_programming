''' 자료형 확인

print("hello")
print(3)
print(10.4)

print(type("hello"))
print(type(3))
print(type(10.4))

i,j,k = 3,5,"hello" 
print(i,j,k)

'''

'''
3 = ii 
print(ii)
'''

''' 대입연산자 돌려보기

a = 100
b=5
a += b
print("a +=b : a=", a)

a = 100
b=5
a -= b
print("a -=b : a=", a)

a = 100
b=5
a *= b
print("a *=b : a=", a)

a = 100
b=5
a /= b
print("a /=b : a=", a)

a = 100
b=5
a %= b
print("a %=b : a=", a)

a = 100
b=5
a //= b
print("a //=b : a=", a)

a = 100
b=5
a **= b
print("a **=b : a=", a)

'''
''' 인풋 해보기
name = input("너의 이름은?")
print("저의 이름은 ",name,"입니다.")
'''
'''
age = input("나이는?")
print("저는",age,"살 입니다.")
print(type(age))  

print("우리 아빠는 저보다 30살 많은",int(age) + 30,"이에요.")
#int()
#float()
#str()

a=10
str_a=str(a)
print("type(a):", type(a))
print("type(str_a)):",type(str_a))
'''

planet = input('원하는 행성은?')
strRadius = input(planet + '반지름은?')
radius = int(strRadius)

length = 2*3.14*radius
print(planet,'반지름:',radius)
print(planet,"둘레길이:",length)