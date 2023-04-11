#0411
#리스트, 듀플, 딕셔너리
# 김, 이, 박, 최,
#리스트
#['김', '이', '박', '최']

#듀플
#('김', '이', '박', '최')

#딕셔너리 -> 사전 {key: value, k1:v1,  k2:v2,.....}
#adress= {'홍길동':'서울', '김길동':'부천', 'james' : '미국'}
#print(adress['홍길동'])

'''
#list
#숫자, int, floot, srting 다 가능함.
a = [10, 20, 30, 40, 50]
str_list = ['하', '호']
print(type(a))
print(a[0]," ",a[1]," ",a[len(a)-1])

#빈리스트 생성-> 하나씩 원소를 추가
list1=[]
#list2=list()
print(list1)
list1.append("python")
list1.append("java")
list1.append("c++")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
print(list1)
print(list1[0])

#list2 = ["python", "java", "c++"]
print("=========for 1========")
for i in range(len(list1)):
    print(list1[i])


print("=========for 2========")
for i in list1:
    print(i)

print("count  : ", list1.count("python"))
print("index  : ", list1.index("python"))
#"hahah".index("a")


#수정
list1[0]="AI"
list1[2]="IOT"
print(list1)

#['AI', 'java', 'IOT', 'python', 'python', 'python', 'python', 'python']
list2 = list1[0:3:1] # 0 ,1,2
print(list2)
list2 = list1[1:5:1] # 'java', 'IOT', 'python', 'python'
print(list2)
list2 = list1[1:len(list1):2] # 'java' ,'python','python'
print(list2)
list2 = list1[2:6:3] # 'IOT', 'python'
print(list2)
list2 = list1[::-1] #역순 'python', 'python', 'python', 'python', 'python' 'IOT' 'java' 'AI'
print(list2)

#list1 , list2
#list1 의 일부를 list3에 대입

list2 = list1[2:6:3]
print(list2)
list3 = [1,2,3,4,5,6,7,8]
print(list3)
list3[1]=list2
print(list3)

#list3[1:2]=list2
#print(list3)

#수정 불가 - > append, insert, 값 변경.x
#[1,2,3,4]
#(1,2,3,4,)  t1 + t2 => t3
#t1 +1 => t1
'''


'''
#list insert
food=[]
food.append("짜장면")
food.append("샌드위치")
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"제육")
print(food)

food.remove("제육")
print(food)

print("food.pop : ", food.pop())
print(food)
print("food.pop : ", food.pop())
print(food)
'''

'''
#extend
print(food)
dessert = ["커피","케잌","와플"]


food_list = food +dessert

print(food_list)

food.extend(dessert) #food + dessert
print(food)

#food.clear()
#del food
#print(food)
food.reverse()
print(food)

l1=["banana","apple","orange","mango"]
print(l1)
print("sorted(l1) :", sorted(l1))
print("l1         :", l1)

l1.sort()
print(l1)

a = "1"
print(type(a))
print(int(a)+5)
print(type(a))

'''

'''
#리스트 컴프리헨션
#0-10까지 있는 list 를 만들자
#1)
l3 = [0,1,2,3,4,5,6,7,8,9,10]
print(l3)
#2)
l3=[]
i=0
for i in range(11) :
    l3.append(i)
print(l3)
'''

#3)
#리스트 변수명 = [i for i in range()]

#l4 = [i for i in range(11)] # [0,1,2,3,....]
#print(l4)

#10
#0~10 까지 숫자의 제곱을 원소로 가지는 리스트를 작성하라
#l5 = [i**2 for i in range(11)] # [0,1,2,3,....]
#print(l5)

#11
#l6 = [i*3 for i in range(11)] # [0,1,2,3,....]
#print(l6)
#13
l7 = []
l7 = ["hellow" for i in range(10)] # [0,1,2,3,....]
print(l7)
