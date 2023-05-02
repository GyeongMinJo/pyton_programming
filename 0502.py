# 0502
# 함수
#input 을 주면 output이 나오는것.

def multi(num1) :
    output_num = num1 * 3
    print("여기는 multi 함수 안입니다.")
    return output_num

print(multi(10))

def hello(n1,n2):
    print("안녕,", n1)
    print("안녕,", n2)
    
hello("홍길동","고길동")

num = 100
print("***num : ", num)

def addone() :
    num = 10
    print(" addone()", num+1)
    print(" addone()num : ", num)
    num = num * 8 +20
    return num
    
result1 = addone()
print("***num : ", num)



coffee = {"아메":2000,"라떼":3000,"티":2500}

def printmenu(**keyvalue) :
    for key in keyvalue :
        print(key,keyvalue[key])
    
printmenu(**coffee)

def func1(*num,**menu):
    result = 0
    for n in num:
        result = result + n
    print(result)
    
    for key in menu :
        print (key,menu[key])
        
lst1 = [1,2,1,2,1,2,3,4,67,9]

func1(1,2,1,2,1,2,3,4,67,9,아메=3000,핫초코=2000,핫도그=3000)
func1(*lst1,**coffee)
func1(1,2,1,2,1,2,3,4,67,9,**coffee)


def addone(x):
    return x +1

print(addone(100))

print((lambda x : x+1)(100))

print((lambda x , y : x+y)(100,200))


lst1 = [1,2,3,4,5,6,7]
lst2 = [1,2,3,4,5,6,7]
#map(함수,input 리스트)
print(list(map(lambda x : x+1,lst1)))
print(list(map(lambda x,y : x+y,lst1,lst2)))
