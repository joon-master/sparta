print('Hello Sparta')
a = 3
b =4
print(a+b)
a = 3  # 숫자 형
b = '3' #문자형

print (a+int(b)) #b string 형을 int형으로 형변환을 했다.

# 리스트형
aList = []
aList.append(1)
print(aList)
# 리스트 : indexing '위치 값 하나' , slicing '범위 값 여러개'

#사전형 {} 사용
aDict = {'name':'joon'}
print(aDict['name'])

# 파이썬의 함수는 def 로 시작을 한다
def sum_all(a,b,c):
    return a+b+c

print(sum_all(1,2,3))

def oddeven(num):
    if num % 2 == 0:
        print(str(num)+"은 짝수 입니다.")
    else:
        print(str(num)+"은 홀수 입니다.")

oddeven(5)

f=['사과','배','감','귤','사과','배','감','귤','사과','배','감','귤']
count = 0
for fruit in f:
    if fruit =='사과':
        count +=1

print(count)

