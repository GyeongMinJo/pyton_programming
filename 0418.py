#0418 python 수업 1교시
#튜플 , 딕셔너리 , 집합
lst = []
# 수정, 변경, 일부 원소 삭제 가능

#수정이 불가학목들.->튜플
t1 = (1,2,3,4)
print(t1)
t2 = ()
print(t2)
t3 = 1,2,3,4,5,3,3,10,3
print(type(t3))

print(t3.index(3))
print(t3.count(3))

# +, *

t4 = 1,2,3,4,5,3,3,10,3
t5 = 100,200,300
print('t4+t5 : ',t4+t5)
print('t4 : ', t4)
print('t5 : ', t5)

print('t4 : ', t4)
print(sorted(t4)) # 원본이 안바뀜.
print('t4 : ', t4)
#lst.sort() #원본이 바뀜.

#dictionary
#key : value
#1001:"홍길동", 1002:"김길동"

d1={1001:"홍길동", 1002:"김길동",1003:"박길동",1004:"고길동"}
print(d1[1001])
#print(d1[0])

#d2={}
#강자에 대한 dictinoary
d2 = dict()
d2['강좌명'] = '파이썬'
d2['개설 요일'] = '화요일'
d2['년도'] = 2003
d2['수강생'] = ['김','이','박']
print("d2 : ",d2)
print(d2['수강생'])
print(len(d2))

month = {10:"1월",20:"2월",30:"3월",40:"4월",50:"5월",60:"6월",70:"7월",80:"8월",90:"9월",100:"10월",110:"11월",120:"12월",}

    
print('month.keys() :', month.keys())
print('month.values(): ',month.values())
print('month.items() :', month.items())

for i in range(10,121 ,10) : 
    print(month[i])
#0418 2교시
for kim in month.keys():
    print(month[kim])
    
for m in month.values() : 
    print(m)
    
for item in  month.items() :
    print(item)
    print(item[1])
    
for k,v in month.items() : 
    print(k)
    print(v)
for i in month : 
    print(i)
    print(month[i]) 
    
print(month.pop(10))# index에 있는 item 을 제거,.
print(month)
print(month.popitem())# index에 있는 item 을 제거,.
print(month)

month.update({30:'March'})
print(month)
month.update({150:'15월'})
print(month)
month.update({30:'300월'})
print(month)


#dictionary-tuple-list 변환
#tuple - 변경불가 수정 x 
#tuple -> list 유자찿 추가 => tuple 변경
#list -> tuple 수강신청 전 수강생 변경, -> tuple 
#tuple, list => dictionary
seql = ['a','b','c','d']
seqt = tuple(seql)
print(seqt)
print(type(seqt))

seql2 = list(seqt)
print(seql2)
print(type(seql2))

seqd = dict(enumerate(seql))
print(seqd)
print(type(seqd))
#6-3 까지 하기...
#zip
#list, tuple 가  여러개 -> 하나의 튜플의 조합으로 된 리스트로  .
l1 = ['1조','2조','3조']
YA = ['홍','김','이'] 
YB = ['최','한','James']

z = zip(l1,YA,YB)

print(type(z))
print(z)
print(list(z))
print(tuple( zip(l1,YA,YB)))

#
l10 = ['한식',    '양식',    '중식',   '분식']
l11 = ['전주식당','딕터로빈',  '취영루',  '토마토']
l12 = ['제육',    '파스타',    '짬뽕', '김밥']

print(list(zip(l10,l11,l12)))


l100 = list(zip('ABCD',l10,l11,l12))
for i in l100 : 
    print(i[0],i[1], i[2],i[3])




'''
#for i in range(4) : 
#    print(l10[i], l11[i], l12[i])
    
l100 = list(zip(l11,l10,l12))
for i in l100 : 
    print(i[0],i[1], i[2])
#리스트 길이가 다르면 제일 짧은거 기준으로 묶임

'''


#zip list1, list2 => list 3
#a,b
#[(a1,b1),(a2,b2)]

l10 = ['한식',    '양식',    '중식',   '분식']
l11 = ['전주식당','딕터로빈',  '취영루',  '토마토']
l12 = ['제육',    '파스타',    '짬뽕', '김밥']

#dictionary
print(list(zip(l10,l11)))
print(dict(zip(l10,l11)))


print(dict(zip(l10,zip(l11,l12))))


print(list(enumerate(l11)))
print(dict(enumerate(l11)))