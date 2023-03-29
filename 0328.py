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

'''
planet = input('원하는 행성은?')
strRadius = input(planet + '반지름은?')
radius = int(strRadius)

length = 2*3.14*radius
print(planet,'반지름:',radius)
print(planet,"둘레길이:",length)
'''

'''
#str  시퀀스를 가지고 있음
var = "python"
ch1 = var[0]
print(var[0],"",var[1],"",var[2])
#p
print(var[0],":",var[-6])
print("length of var : ",len(var))

#print("PYTHON"[0],"PYTHON"[2])

#print(var[15])  len 보다 작은수를 넣어야 구동 인덱스값이 오류임 
'''

'''
#슬라이싱 할떄 마지막수에 -1 한 숫자만큼만나옴 1:5 라고하면 1~4에있는 칸까지만 표현함
print("PYTHON"[1:5])
print("PYTHON"[2:4])
print("PYTHON"[0:3])
print("PYTHON"[0:6])
print("PYTHON"[0:len("PYTHON")])

#-1로 하는건 시험에 안냄, 2진수 10진수 진수나오는건 시험에안나옴
print("PYTHON"[-5:-1])
'''

'''
#시작과 끝을 비우면 처음부터와 끝까지라고 생각 둘다 생략하면 모두
print("PYTHON"[:3])
print("PYTHON"[:4])
print("PYTHON"[1:])
print("PYTHON"[3:])
print("PYTHON"[:])#전체 반환
'''

'''
str = 'Monty python'
print(len(str))

print(str[0:5],str[6:],str[6:12])
print(str[-12:-7],str[-6:],str[-6:0]) # 스타트 첨자는 엔드 첨자 보다문자열 왼쪽에 위치해야함 그렇지않으면 공백을 줌 오류는 안뜸

#str[start : end : step] 가있었는데 안쓰면 1로 생략이 되는거였음 이젠 점프 넣어볼거임
#cat[0:3]->cat ,cat[0:3:2]->ct만 나옴
#cat[::-1]->tac 로 거꾸로 나옴
print("PYTHON"[5:0:-1])
print("PYTHON"[-1:-7:-1])

print("abcdef"+"\b"+"c")
print("hello\nworld")
print("ahahahah\vaghahhahah")
print("aaaaaaaaa\vbbbbbbbb\vcccccccccc")
print("aaaaaaaaa\'bbbbbbbb\'cccccccccc")
print("aaaaaaaaa\"bbbbbbbb\"cccccccccc") #오류 나옴 a 와 c사이에 \" 를하거나 ''겉에 작은 걸로바꾸고 안에 큰걸로 쓰기
print('aaaaaaaaa"bbbbbbbb"cccccccccc')

'''
#string method
str_var ="하하하하"

print(str_var.replace("하","호"))

str_var2 = "안녕하세요.파이썬. 파이썬.파이썬. 파이썬.파이썬. 파이썬.파이썬. 파이썬.파이썬. 파이썬. 수업입니다."
print(str_var2.replace("파이썬","자바"))#str_var2에는 저장되있는게 바뀌는게아님 휘발성 조건
str_var3 = str_var2.replace("파이썬","자바")
str_var4 = str_var2.replace("파이썬","자바",3)

print("str_var2",str_var2)
print("str_var3",str_var3)
print("str_var4",str_var4)

# 실수를 입력받음.
# 102.345

a = input("실수를 적으시오")
a1 = a.replace(".","")
sum = int(a1[0])+int(a1[1])+int(a1[2])+int(a1[3])+int(a1[4])+int(a1[5])

print("sum:",sum)