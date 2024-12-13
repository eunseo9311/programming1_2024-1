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