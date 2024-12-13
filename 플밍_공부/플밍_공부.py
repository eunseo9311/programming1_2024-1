num = 0
count = 0
while num < 100: 
#조건식에 있는 변수가 계속 발생해야 언젠간 그 조건을 만족하지 않는 경우가 발생한다. 이걸 생각하면서 프로그램 작성하기.
    count += 1 #count = count + 1
    num += count #num =num + count
    print(f"{count}: {num}")


num = 0
while num < 100;
    print(f"count: {num}")
    num += 1



num = None
while num != 0:
    #조건식의 변수가 계속 변하는지를 보면서 조건식이 끝나는지를 봐야한다.
    #무한루프가 도는 것이 간간히 발생하기 때문이다.
    num = int(input("숫자를 입력하세요: "))
    if num == 666:
        print("악마의 숫자입니다.")
        break




num = None
while True:
    print("유기현 넌 나를 영원히 벗어날 수 없어!")




a = 100
while a < 1000:
    print("너는 나를 영원히 벗어날 수 없어!")
    a = a - 100 #이건 무한루프. 변수가 조건식에 얽혀있는 경우 변수가 변화하지 않거나 영원히 조건을 벗어날 수 없다면 무한루프.
    # a = a + 100 일케 하면 종료됨




let str = '';

for (let i = 0; i < 9; i++){
    str 
    #for 문의 구성 중요함.
}



marks = [90,25,67,45,80]
number = 0
for mark in marks:
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")





marks = [
    {"id": 500, "mark": 70},
    {"id": 77, "mark": 50},
    {"id": 123, "mark": 80},
    {"id": 883, "mark": 75},
    {"id": 12, "mark": 55}
]

for item in marks:
    mark = item["mark"]
    if mark >= 60:
        print(f"{item["id"]}번 학생은 합격입니다.")
    else:
        continue

    print(f"{item["id"]}번 학생의 점수는 {mark} 입니다.")



#구구단
print("구구단")

i = 2
while i < 10 :
    print()
    print("===", )




#for 문의 경우에는 아무 조건이 없으면 무한루프를 만들 수 있는데
#파이썬에서만 그렇고 다른 언어에서는 그렇지 않다



#여기까지가 플밍_6주차_수업




#6주 1강
score = int(input("점수를 입력하세요 : "))
if score >= 90 :
    print("장학금 대상자입니다.")
print("수고하셨습니다.")




#6주 1강
temp = int(input()"기온을 입력하세요: "))
if temp >= 20:
    print("반팔 입으세요")
else:
    print("긴팔 입으세요")
print("좋은 하루 보내세요 :)")





#6주 2강 5쪽
score = int(input("점수가 몇 점이에요?: "))
if score >= 90:
    print("장학금 대상자입니다.\n축하합니다.")
else:
    print("장학금 대상자가 아닙니다.\n다음 학기를 노려봅시다.")
print("수고하셨습니다.")





#6주차 2강 7쪽
# 내 코드
nowHour = int(input("지금 몇시인가요?"))
if nowHour >= 7:
    lastHour = nowHour - 6
    print("현재 시간: ",nowHour)
    print("이전 시간: ",lastHour)
if nowHour <= 6 and nowHour > 0: 
    # && 은 파이썬에서 안 쓰는 연산자임. and, or 이런걸 사용해야한다.
    lastHour = 24 - nowHour #이렇게 하면 안됨. 여기가 틀림.
    print("현재 시간: ",nowHour)
    print("이전 시간: ",lastHour)

# 정답
nowHour = int(input("지금 몇시인가요?"))
lastHour = nowHour - 6
if lastHour < 0:
    lastHour += 24
print("현재 시간: ",nowHour)
print("이전 시간: ",lastHour)





#6주차 2강 확인 문제1
n = int(input("정수를 입력하세요: "))
if n > 0:
    print("입력하신 %d는 양수입니다.") % n
elif n = 0:
    print("입력하신 %d는 0입니다.") % n
else:
    print("입력하신 %d는 음수입니다.") % n
print("프로그램을 종료합니다.")





score = int(input("시험 점수를 입력하세요: "))
if score >= 90:
    print("시험을 아주 잘 봤군요. 축하해요.")                                                                                      
elif score >= 80:
    print("시험을 괜찮게 봤군요. 수고했어요.")
elif score >= 70:
    print("시험을 좀 못봤군요. 다음에는 잘 봐요.")
else :
    print("완전히 망했군요. 공부를 열심히 합시다.")
print("시험 공부하느라 수고했습니다. 오늘은 푹 쉬어요 :)")





Htemp = int(input("최고 기온을 입력하세요: "))
Ltemp = int(input("최저 기온을 입력하세요: "))
기온차 = Htemp - Ltemp
if Htemp >= 20:
    print("반팔 옷을 추천합니다.")
elif Htemp >= 15:
    print("긴팔 옷을 추천합니다.")
else:
    print("가벼운 외투를 챙기세요.")
if 기온차 >= 15:
    print("외투를 챙기세요.")
elif 기온차 >= 10:
    print("일교차가 크니 건강 유의하세요.")




#컴사고_6주차_수업




from random import random
num = int(random()*1000)
if num < 100 :
    print("숫자는 세 자리로 입력해야 합니다.\n작습니다. 더 큰 수를 입력하세요.")
    num = int(random()*1000)
elif num > 1000 :
    print("숫자는 세 자리로 입력해야 합니다.\n큽니다. 더 작은 수를 입력하세요.")
    num = int(random()*1000)


#플밍과제2