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





