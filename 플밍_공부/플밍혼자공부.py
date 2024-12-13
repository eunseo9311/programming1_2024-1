'''

#포맷코드 %표현
print("%d is %s in English, %s in french, and %s in Korean." % (5,"five","cing","다섯"))
#format 함수
print("{0} is {1} in English, {2} in french, and {3} in Korean.".format(5,"five","cing","다섯"))
#format 함수
print('{num} is {eng} in English, {fra} in french, and {kor} in Korean.'.format(num=5,eng="five",fra="cing",kor="다섯"))
#f문자열
num = 5
eng =  "five"
fra = "cing"
kor = "다섯"
print(f'{num} is {eng} in English, {fra} in French, and {kor} in Korea.')



#포맷코드 %표현
"%10s" % "hi"
"0,4f" % 3.4214535435
"%10.4f" % 3.42516234
#format 함수
"{0:<10}".format("hi")
"{0:=^10}".format("hi")
y = 3.134523156365
"{0:10.4f}".format(y)
#f문자열
f'{"hi":=^10}'
y = 3.354532563543
f'{y:0.4f}'



a = 0.1
sum = 0.0
for i in range(0,10000):
    sum = sum + a
print("sum = " , sum)



a = list("Hello, world")
b = set("Hello, world")
print(a)
print(b)


a = "Life is too short, You need Python!"
b = "C is one of classical programming launguage"
s1 = set(a)
s2 = set(b)
print(s1|s2)
print(s1 - s2)



money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")


money = True
taxi = False
if money:
    print("돈이 있어요.")
    if taxi:
        print("택시를 탑니다")
    else:
        print("택시가 없어서 걸어갑니다.")
else:
    print("돈이 없어요.\n걸어갑니다.")


money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


pocket = ['cellphone','paper']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")


pocket = ['cellphone','paper']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


score = int(input("Enter ypur score:" ))
if score >= 90:
    grade = "A"
if score >= 80:
    grade = "B"
if score >= 70:
    grade = "C"
if score >= 60:
    grade = "D"
if score < 60:
    grade = "F"
print(grade)


score = int(input("Enter ypur score:" ))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)


score = int(input("Enter your score:" ))
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

message = "success" if score >= 60 else "failure"




score = int(input("Enter your score:" ))

match score:
    case score if score >= 90:
        grade = 'A'
    case score if score >= 80:
        grade = 'B'
    case score if score >= 70:
        grade = 'C'
    case score if score >= 60:
        grade = 'D'
    case _:
        grade = 'F'
print(grade)



score = int(input("Enter your score: "))
match score:
    case score if score >= 90:
        grade = 'A'
    case score if score >= 80:
        grade = 'B'
    case score if score >= 70:
        grade = 'C'
    case score if score >= 60:
        grade = 'D'
    case _:
        grade = 'F'
print(grade)


match grade:
    case 'A'| 'B' | 'C':
        print("PASS")
    case _ :
        print("FAIL")



n = int(input("숫자를 입력하세요: "))
print(n)
while n > 1:
    if n % 2 == 1:
        n = n*3 + 1
        print(n)
    else:
        n = n//2
        print(n)


print("<서울버스터미널>")
place = input("행선지를 입력하세요: ")
match place:
    case "대전":
        print('%s까지 소요시간은 4시간, 요금은 20000원 입니다.' % place)
    case "대구":
        print('%s까지 소요시간은 3시간, 요금은 30000원 입니다.' % place)
    case "광주":
        print('%s까지 소요시간은 3시간, 요금은 35000원 입니다.' % place)
    case "부산":
        print('%s까지 소요시간은 4시간, 요금은 40000원 입니다.' % place)
    case _ :
        print("운행하지 않는 행선지입니다.")



print("<서울버스터미널>")
place = input("행선지를 입력하세요: ")
match place:
    case "대전":
        time = 2
        money = 20000
    case "대구":
        time = 3
        money = 30000
    case "광주":
        time = 3
        money = 35000
    case "부산":
        time = 4
        money = 40000
    case _ :
        print("운행하지 않는 행선지 입니다.")
print(f'{place}까지의 소요시간은 {time}시간, 요금은 {money}입니다.')
print('{0}까지의 소요시간은 {1}시간, 요금은 {2}입니다.'.format(place,time,money))



import time
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    time.sleep(0.5)
    if treeHit == 10:
        print("나무 넘어갑니다.")
        time.sleep(0.5)



coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


coffee = 10
money = 300
while money:
    coffee = coffee - 1
    print("커피를 드립니다")
    if coffee == 0:
        print("커피가 없으므로 판매를 중지합니다.")
        break


a = 0
while a < 10:
    a = a+ 1
    if a % 2 == 0:
        continue
    print(a)


a = 0
while a < 20:
    a = a + 3
    if a % 2 != 0:
        continue
    print(a)


for i in "abcdefg":
    print(i)


test = ['one', 'two', 'three']
for i in test:
    print(i)

###
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first, last)

###
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

###
score = [90,25,67,45,80]
number = 0
for i in score:
    number += 1
    if i >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)



for i in range(10):
    if i == 5:
        break
    print(i)
print("End of Program")


###
score = [50,70,80,40,60]
for i in score:
    if i >= 60:
        print(f"축하합니다. 당신의 점수는 {i}입니다.")
    else:
        continue



add = 0
for i in range(1,11):
    add += i
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end= "  ")

##########
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')



for i in range(2,10):
    for j in range(1,10):
        print(i*j, end= "  ")


i = 0
while i < 5:
    print(i)
    i = i+1



for i in range(10):
    if i == 5:
        break
        print(i)
print("end")



for i in range(10):
    if i == 5:
        continue
    print(i)
print("end")


result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)



gugudan = [(x,y,x*y) for x in range(2,10) for y in range(1,10)]
print(gugudan)



a = [1,2,3,4,5,6,7,8,9]
b = ['홀수' if num % 2 == 1 else '짝수' for num in a]
print(b)



score = [98, 65, 77, 82, 56, 87, 92]
grades = ['A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' if s >= 60 else 'F' for s in score]
print(score)



result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)



result = []
for x in range(2,10):
    for y in range(1,10):
        result.append(x*y)
print(result)



a = [1,2,3,4]
result = []
for num in a:
    if num % 2 == 0:
        result.append(num*3)
print(result)



gugudan = [(x,y,x*y) for x in range (2,10) for y in range(1,10)]
print(gugudan)



gugudan = []
for x in range(2,10):
    for y in range(1,10):
        gugudan.append ((x,y,x*y))
print(gugudan)



a = [1,2,3,4,5,6,7,8]
b = ['홀수' if num % 2 == 1 else '짝수' for num in a]
print(b)




a = [1,2,3,4,5,6,7,8]
b =[]
for num in a:
    if num % 2 == 1:
        b.append('홀수')
    else:
        b.append('짝수')
print(b)



from random import random
num = int(random()*1000)
    if 1 and 1 in num:
        num = int(random()*1000)
    if 2 and 2 in num:
        num = int(random()*1000)




from random import random
digit = [0, 0, 0]
while 1:
    num = int(random() * 1000)
    if num < 100: continue
    digit[0] = num // 100
    digit[1] = num // 10 % 10
    digit[2] = num % 10
    if digit[0] != digit[1] and digit[1] != digit[2] and digit[0] != digit[2]:
        print(num)
        break
while 1:
    guessNum = input()
    guess = [int(i) for i in guessNum]
    status = [0, 0]
    for i in range(len(guess)):
        if guess[i] == digit[i]: status[0] += 1
        else:
            for j in range(len(digit)):
                if guess[i] == digit[j]: status[1] += 1
    print(f"{status[0]} strike {status[1]} ball")
    if status[0] == 3 and status[1] == 0: break




print("=== 원리금 계산 프로그램 ===")
저축금액 = int(input("저축금액 입력: "))
원금 = 저축금액
이자 = 저축금액 * 0.03
세금 = 이자 * 0.5
최종 = 원금 + 이자 + 세금
print("원금: ")
'''


'''
########     야구게임      #########3
from random import random
digit = [0, 0, 0]
while 1:
    num = int(random() * 1000)
    if num < 100: continue
    digit[0] = num // 100
    digit[1] = num // 10 % 10
    digit[2] = num % 10
    if digit[0] != digit[1] and digit[1] != digit[2] and digit[0] != digit[2]:
        print(num)
        break
while 1:
    guessNum = input()
    if len(guessNum) < 3:
        print("세 자리 수를 입력해주세요.")
        continue
    guess = [int(i) for i in guessNum]
    status = [0, 0]
    for i in range(len(guess)):
        if guess[i] == digit[i]: status[0] += 1
        else:
            for j in range(len(digit)):
                if guess[i] == digit[j]: status[1] += 1
    print(f"{status[0]} strike {status[1]} ball")


a = [i*j for i in range(2,10) for j in range(1,10)]
print(a)





# 고객 정보를 저장할 리스트 선언
고객_리스트 = []

while True:
    # 메뉴 출력
    선택 = input("작업을 선택하세요. 1. 고객정보 입력 2. 고객명으로 정보 조회 3. 고객 아이디로 정보 조회 : ")

    if 선택 == '1':
        # 고객 정보 입력
        고객_아이디 = input("고객 아이디: ")
        이름 = input("이름: ")
        주소 = input("주소: ")
        직업 = input("직업: ")
        전화번호 = input("전화번호: ")
        # 입력 받은 고객 정보를 리스트에 추가
        고객_리스트.append({'고객_아이디': 고객_아이디, '이름': 이름, '주소': 주소, '직업': 직업, '전화번호': 전화번호})

    elif 선택 == '2':
        # 고객명으로 정보 조회
        찾는_이름 = input("조회할 고객의 이름: ")
        찾은_고객 = [고객 for 고객 in 고객_리스트 if 고객['이름'] == 찾는_이름]
        if 찾은_고객:
            for 고객 in 찾은_고객:
                print(f"고객 아이디: {고객['고객_아이디']}, 이름: {고객['이름']}, 주소: {고객['주소']}, 직업: {고객['직업']}, 전화번호: {고객['전화번호']}")
        else:
            print("고객이 존재하지 않습니다.")
            break

    elif 선택 == '3':
        # 고객 아이디로 정보 조회
        찾는_아이디 = input("조회할 고객의 아이디: ")
        찾은_고객 = [고객 for 고객 in 고객_리스트 if 고객['고객_아이디'] == 찾는_아이디]
        if 찾은_고객:
            for 고객 in 찾은_고객:
                print(f"고객 아이디: {고객['고객_아이디']}, 이름: {고객['이름']}, 주소: {고객['주소']}, 직업: {고객['직업']}, 전화번호: {고객['전화번호']}")
        else:
            print("아이디가 존재하지 않습니다.")
            break
    else:
        print("잘못된 선택입니다. 다시 시도해주세요.")



print("=== 원리금 계산 프로그램 ===")
print(f'{"원리금 계산 프로그램":=^20}')
print("{0:=^20}".format("원리금 계산 프로그램"))
print(f'{'%s':=^20}' % "원리금 계산 프로그램")


######  고객정보 입력받기  ########
customers = []

while True:
    print("작업을 선택하세요.\n1. 고객정보 입력\n2. 고객명으로 정보 조회\n3. 고객 아이디로 정보 조회")
    choice = input()

    if choice == '1':
        customer_id = input("고객 아이디를 입력하세요: ")
        name = input("이름을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        job = input("직업을 입력하세요: ")
        phone_number = input("전화번호를 입력하세요: ")
        customers.append({'고객아이디': customer_id, '이름': name, '주소': address, '직업': job, '전화번호': phone_number})
        print("고객 정보가 입력되었습니다.")

    elif choice == '2':
        search_name = input("조회할 고객명을 입력하세요: ")
        found = False
        for customer in customers:
            if customer['이름'] == search_name:
                print(
                    f"고객아이디: {customer['고객아이디']}, 이름: {customer['이름']}, 주소: {customer['주소']}, 직업: {customer['직업']}, 전화번호: {customer['전화번호']}")
                found = True
        if not found:
            print("입력받은 고객님의 정보는 존재하지 않습니다.")
            break

    elif choice == '3':
        search_id = input("조회할 고객 아이디를 입력하세요: ")
        found = False
        for customer in customers:
            if customer['고객아이디'] == search_id:
                print(
                    f"고객아이디: {customer['고객아이디']}, 이름: {customer['이름']}, 주소: {customer['주소']}, 직업: {customer['직업']}, 전화번호: {customer['전화번호']}")
                found = True
        if not found:
            print("입력받은 고객님의 정보는 존재하지 않습니다.")
            break

    elif choice == '0':
        print("프로그램을 종료합니다.")
        break



# 사용자로부터 저축금액 입력받기
저축금액 = float(input("저축금액을 입력하세요: "))

# 원금(정수로 변환)
원금 = int(저축금액)

# 이자 계산 (0.25를 곱한 값, 정수로 변환)
이자 = int(원금 * 0.25)

# 세금 계산 (이자의 0.5를 곱한 값, 정수로 변환)
세금 = int(이자 * 0.5)

# 최종금액 계산 (원금 + 이자 - 세금)
최종금액 = 원금 + 이자 - 세금

# 출력
print(f"원금: {원금:>10}원")  # 원금 출력
print(f"이자: {이자:>10}원")  # 이자 출력
print(f"세금: {세금:>10}원")  # 세금 출력
print(f"최종금액: {최종금액:>7}원")  # 최종금액 출력




##########        야구게임       ##########
## def 사용한거
from random import random


def generate_unique_number():
    while True:
        num = int(random() * 1000)
        if num >= 100 and len(set(str(num))) == 3:
            return num


def validate_input(input_str):
    return input_str.isdigit() and len(input_str) == 3 and len(set(input_str)) == 3


def compare_numbers(num, guess):
    num_str = str(num)
    guess_str = str(guess)
    strike = 0
    ball = 0
    for i in range(3):
        if guess_str[i] == num_str[i]:
            strike += 1
        elif guess_str[i] in num_str:
            ball += 1
    return strike, ball


num = generate_unique_number()
print("세 자리 숫자가 생성되었습니다. (모든 자리의 숫자는 서로 다릅니다)")

strike = 0
ball = 0

while strike != 3 or ball != 0:
    user_input = input("세 자리 숫자를 입력하세요: ")
    while not validate_input(user_input):
        print("입력이 잘못되었습니다. 세 자리 숫자를 입력해 주세요. 모든 자릿수는 서로 달라야 합니다.")
        user_input = input("세 자리 숫자를 입력하세요: ")
    guess = int(user_input)
    strike, ball = compare_numbers(num, guess)
    print(f"{strike} 스트라이크, {ball} 볼")

print("정답입니다!")




##########        야구게임       ##########
### def 안 쓴거
from random import random

# 세 자리 서로 다른 숫자가 나올 때까지 반복
while True:
    num = int(random() * 1000)
    num_list = [int(d) for d in str(num) if num >= 100 and num <= 999]
    if len(num_list) == 3 and len(set(num_list)) == 3:
        break

# 게임 시작
strike = 0
ball = 0

while strike != 3 or ball != 0:
    # 사용자 입력 받기
    while True:
        user_input = input("세 자리의 숫자를 입력하세요: ")
        user_list = [int(d) for d in user_input if user_input.isdigit() and len(user_input) == 3]
        if len(user_list) == 3 and len(set(user_list)) == 3:
            break
        else:
            print("세 자리의 서로 다른 숫자를 입력해주세요.")

    # strike, ball 초기화
    strike = 0
    ball = 0

    # strike, ball 계산
    for i in range(3):
        if num_list[i] == user_list[i]:
            strike += 1
        elif user_list[i] in num_list:
            ball += 1

    print(f"Strike: {strike}, Ball: {ball}")

# 게임 종료
print(f"정답입니다! 숫자는 {num}였습니다.")




##########        야구게임       ##########
### 리스트 컴프리헨션 사용한거임
from random import random

# 숫자 생성
while True:
    num = int(random() * 1000)
    num_list = [int(d) for d in str(num)]
    if len(num_list) == 3 and len(set(num_list)) == 3:
        break

# 게임 시작
strike, ball = 0, 0
while strike != 3 or ball != 0:
    strike, ball = 0, 0  # strike와 ball 초기화
    # 사용자 입력 검증
    while True:
        user_input = input("세 자리 숫자를 입력해주세요(각 자리 숫자는 서로 달라야 합니다): ")
        if user_input.isdigit() and len(user_input) == 3 and len(set(user_input)) == 3:
            guess_list = [int(d) for d in user_input]
            break
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")

    # strike와 ball 계산
    strike = sum([num_list[i] == guess_list[i] for i in range(3)])
    ball = sum([d in num_list for d in guess_list]) - strike

    print(f"{strike} 스트라이크, {ball} 볼")

print("정답입니다!")




# 리스트 컴프리헨션 예제
num = [1,2,3,4,5]
new = [x for x in num]
print(num)
s = [x*3 for x in num]
print(s)




name = '송은서'
age = 22
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
'''


'''
print("=== 원리금 계산 프로그램 ===")
print(f'원리금 계산 프로그램':=^20) f문자열     { } 중괄호를 안 했음
print('%s':=^20.format("원리금 계산 프로그램")) 포맷함수    0번째에 대입해야하는거 하고 {}중괄호로 넣어주기
print() 문자열 포매팅    이거 하려먼 f문자열이랑 같이 써야하는데
'''

'''

print(f'{"원리금 계산 프로그램":=^20}')
print("{0:=^20}".format("원리금 계산 프로그램"))
print(f'{'%s':=^20}' % "원리금 계산 프로그램")

A = [{'국어점수' : 49, '수학점수' : 43, '영어점수' : 49}]


###2번째꺼
result = [(x, y, z) for x in range(1, 13) for y in range(1, 13) for z in range(1, 13) if 30 <= x * y * z <= 200]

#3번
반복문을 써야해
그리고 변수 하나를 9로 선언해두고
한번 반복문 돌때마다 그 변수를 1씩 감소시켜
그리고 print문에서 %10d이거 활용하라할걸

#4번
처음 입력받을때
변수명 = [i for i in input().split()]하면
저렇게 리스트 컴프리헨션 활용하면
띄어쓰기 단위로 문자가 분리되서 단어별로 리스트에 들어가
그러면 조건문 활용하고 len()활용해서
글고 변수 하나더 선언해서
for문 속에서 반복하면서
리스트 요소 하나마다 길이를 5기준으로 판단해서 5보다 클때
하나더 선언한 변수를 1씩 추가하도록해서
최종적으로 그 변수를 출력하면 단어개수가나와


#5번
나는 리스트안에 튜플을 집어넣었어
먼저 계산할 분수 두개 튜플로 입력해두고
리스트 넣고
변수 선언해서 덧셈뺄셈곱셈 나눗셈을 어펜드로 리스트에 넣었고
덧셈뺄셈 등등의 연산은 미리 넣어둔 리스트 속 튜플을 인덱싱으로 불러와서 연산했어
그리고 처음에 입력해둔 튜플 두개를 정렬했어 sort()
뺄셈에서 음수안나오려고 한거고
덧셈뺄셈 로직에서는 경우의수를 두개를 생각해야해 분모가 같을때 다를때
그렇게 해서 만든걸 어펜드로 넣고
어펜트로 추가한 튜플을 출력해야한다는거
마지막에 인덱싱 활용해서 리스트속에 있는 튜플을 출력하면 끝

'''





'''
##############################내꺼 1번





##############################내꺼 2번
combinations = [(x, y, z) for x in range(1, 13) for y in range(1, 13) for z in range(1, 13) if 10 <= x + y + z <= 30]



##############################내꺼 3번
# 변수 선언
star = 11

# 반복문을 사용하여 별 출력
for i in range(1, star + 1, 2):
    # 각 줄의 별을 중앙에 정렬하여 출력
    print("{:^11}".format('*' * i))
    star -= 2  # 반복할 때마다 변수를 2씩 감소




##############################내꺼 4번
# 사용자로부터 길이가 50 이상인 문자열 입력받기
input_string = input("길이가 50 이상인 문자열을 입력하세요: ")

# 조건에 맞는 문자의 개수 세기
uppercase_count = len([char for char in input_string if 'A' <= char <= 'Z'])
lowercase_count = len([char for char in input_string if 'a' <= char <= 'z'])
whitespace_count = len([char for char in input_string if char in [' ', '\n', '\t']])
digit_count = len([char for char in input_string if '0' <= char <= '9'])
# 특수 문자 개수 세기, 여기서는 알파벳, 숫자, 공백을 제외한 모든 문자를 특수 문자로 간주
specialchar_count = len([char for char in input_string if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9' or char in [' ', '\n', '\t'])])

# 결과 출력을 위한 카테고리와 개수를 리스트로 저장
categories = ["대문자", "소문자", "공백 문자", "숫자", "특수 문자"]
counts = [uppercase_count, lowercase_count, whitespace_count, digit_count, specialchar_count]

# for문을 이용해 각 카테고리의 개수 출력
for i in range(len(categories)):
    print(f"{categories[i]} 개수: {counts[i]}")





##############################내꺼 5번
# 다항식의 계수를 리스트로 표현
poly1 = [-1, -1, 1]  # x^2 - x - 1
poly2 = [-4, 0, 1, 1]  # x^3 + x^2 - 4

# 다항식 곱셈 결과를 저장할 리스트 초기화
result_poly = [0] * (len(poly1) + len(poly2) - 1)

# 다항식 곱셈 수행
for i in range(len(poly1)):
    for j in range(len(poly2)):
        result_poly[i + j] += poly1[i] * poly2[j]

# x=5를 대입하여 결과 다항식의 값을 계산
x = 5
result_value = 0
for i in range(len(result_poly)):
    result_value += result_poly[i] * (x ** i)

print("다항식 곱셈의 계수: ", result_poly)
print("x=5일 때 다항식의 값: ", result_value)
'''