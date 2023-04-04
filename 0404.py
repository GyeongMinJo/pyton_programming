'''
str = "파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은"
newstr=str.replace("파이썬은","자바")
newnewstr = "파이썬,하하하,호호호,히히히,우우우"
'''

'''
print('{}+{}={}'.format(2,3,5))

a,b=5,10.000
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(a,b,a+b)) #이 ()안에있는걸 배열로 생각하고 중괄호안에 그 순서대로 들어감
print('{2}+{0}={1}'.format(a,b,a+b)) 
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b)) #정수는 %,십진수 d 소수는 f
print('{0:d}+{1:f}={2:f},{3:s}'.format(a,b,a+b,"hdhdh")) #s 해서 문자열도 가능
'''

'''
print("str : ",str)
print("newstr: ",newstr)

print("str.count('파이썬')",str.count("파이썬"))
print('->'.join(str))# 글자 하나하나 뒤에 문자 삽입
'''

'''
print(str.find("썬")) # 값의 몇번째에 나오는지 알려주는 파 0번쨰 이 1번쨰 썬 2번째
print(str.index("썬")) # 파인드랑 인덱스는 거의 똑같음 허나 없는걸 찾으면 파인드는 -1리턴 인덱스는 에러를 리턴함

print(str.find("자바")) #이친구는 -1 ->있는지없는지 모를떄 찾을떄 쓰기
print(str.index("자바")) #이친구는 에러 ->확실할떄쓰기 아님 에러라 멈춤
'''

'''
print(str.split())# 공백이으로 나두면 띄어쓰기인 공백을 기준으로 짤라줌
print(newnewstr.split(","))
'''

'''
value = False #True
print(type(value))
print(int(value))

print(bool(0),bool(1),bool(1.33),bool(-12))
print(bool("dasgsagsd"),bool("-1"),bool(""))#""은 False 이다
'''
'''
if 조건:
    실행문
else 
    실행문2   
'''
'''
#오전? 오후?
hour = 13
if hour < 12:
    print("12시가 않지나서 오전입니다")
elif hour<19 : 
    print("12시가 지나고 ,18시가 안지났으니 오후입니다.")

else :
    print("18시가 지났으니 저녁입니다.")

#장학금
#score < 200 50만원을 줌
#200 <= score < 400 100만원
#400 <= score < 500 10000만원줌
score_str = input("점수는? ")
print(type(score_str))
score = int(score_str)
if score < 200 :
    print("50만원획득")
elif score < 400 :
    print("100만원 획득")
else :
    print("1000만원 획득")
'''
'''
#점심식사
answer = input("서브웨이 먹을래?")
if answer == 'yes'or'응':
    print("8호관 1층")
else :
    again_anser = input("학식 먹을래?")
    if again_anser == 'yes'or'응':
        print("8호관 3층")
    else :
        print("넌 굶어라")
'''

'''
#반복문
#for
for i in 1,3,4,5,6,8 :
    print(i)
        
print("range1") 
for i in range(0,11,1) :
    print(i)
sum=0
print("range2")    
for i in range(11) :
    sum = sum + i
    print(i,"번쨰 sum은",sum)
else :
    print("for 문의 조건이 만족하지않습니다.")
    print("i가 range(11)에서 벗어남.")
    print("for문이 break나 countinue로 종료된게 아니라 정상종료시에만 실행")    
print("sum: ", sum)
'''
'''
#놀이기구 탑승
#4명 탑승가능
#키 150이상
i=0
while i<=3 :
    print("4명이 탈수있는 놀이기구에 어서오세요")
    print("현재",i,"명 탑승중입니다")
    print("남은좌석수 : ",4-i)
    a_str=input("당신의 키는?")
    a=int(a_str)
    if a>150 :
        i=i+1
        print("놀이기구에 탑승했습니다")
    else :
        print("키가 기준에 맞지않아 탈승 할 수 없습니다.")
else :
    print("탑승인원이 4명이 꽉차서 출발합니다.")
    print("즐거운 시간되세요")
'''

'''
while 조건:
    수행문
'''
'''
i=10
while i>5:
    print(i,"는 5보다 크다")
    i = i-1
n=1
while n<=5:
    print(n, end='  **   ')
    n=n+1
else:
    print("while이 잘 끝났습니다")
    print("현재 n의 값은 ",n,"입니다")
'''

#continue , break
#반복문 중간에 반복을 더이상 하지않고 실행을 종료가 목적
#반복만 안쪽에서 실행된다.
#주로 if문 안쪽에서 사용됨 if안에 있지만 if를 끝내는게아니라 그위에 for while 을 끝내는거임
#for while 둘다 사용
#continue는 n차시중 만나면 n+1 차시를 하는거
#break는 n차시중에 그냥 나가는거 

#input으로 입력을 받는데,
#무한반복.
#exit이라는 값을 받으면 ,입력받는 것을 종료
 
#apple을 받으면,넌 이단어를 입려했다.를 출력하지않게하기
while True:
    str=input("단어를입력하시오.")
    if str == 'exit' :
        print("exit 을 입력하여 종료합니다.")
        break
    else :
        if str=='apple':
            print("apple을 입력받았음")
            print("continue를 실행함")
            continue
        
        print(str,str,str,"을 입력하셨습니다.")
    print("저는 아직 while 안에 있어요.")
print("while 종료")
#그외에 단어를 입력받으면 해당 단어를 3번찍어줄것
#continue , break 활용 해본다.