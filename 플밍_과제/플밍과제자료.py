
from random import random
num = int(random() * 1000)
while num < 100:
    num = int(random() * 1000)
while True:
    answer = input()
    if len(answer) != 3:
        print("숫자는 세 자리로 입력해야 합니다.")
        continue
        answer = int(answer)
    if answer > num:
        print("큽니다. 더 작은 수를 입력하세요.")
    elif answer < num:
        print("작습니다. 더 큰 수를 입력하세요.")
    else:
        print("맞췄습니다.")
        break




customers = {}  # 고객 정보 저장할 딕셔너리

while True:
    print("작업을 선택하세요.")
    print("1. 고객정보 입력")
    print("2. 고객명으로 정보 조회")
    print("3. 고객 아이디로 정보 조회")
    print("0. 종료")
    num = int(input(": "))

    if num == 1:
        id = input("고객아이디: ")
        name = input("이름: ")
        address = input("주소: ")
        job = input("직업: ")
        call = input("전화번호: ")
        customers[name] = {'id': id, 'address': address, 'job': job, 'call': call}
        print("고객 정보가 입력되었습니다.")

    elif num == 2:
        check_name = input("조회할 고객명을 입력하세요: ")
        if check_name in customers:
            customer_info = customers[check_name]
            print(f"{check_name} 고객님의 정보는 다음과 같습니다.")
            print(f"고객아이디: {customer_info['id']}")
            print(f"이름: {check_name}")
            print(f"주소: {customer_info['address']}")
            print(f"직업: {customer_info['job']}")
            print(f"전화번호: {customer_info['call']}")
        else:
            print(f"{check_name} 고객님의 정보는 존재하지 않습니다.")

    elif num == 3:
        check_id = input("조회할 고객 아이디를 입력하세요: ")
        found = False
        for name, info in customers.items():
            if info['id'] == check_id:
                print(f"고객 아이디 {check_id}의 정보는 다음과 같습니다.")
                print(f"고객아이디: {info['id']}")
                print(f"이름: {name}")
                print(f"주소: {info['address']}")
                print(f"직업: {info['job']}")
                print(f"전화번호: {info['call']}")
                found = True
                break
        if not found:
            print(f"{check_id} 고객님의 정보는 존재하지 않습니다.")

    elif num == 0:
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 작업 번호를 입력하세요.")






customerList = []
idList = []
nameList = []


num = int(input("작업을 선택하세요.\n1. 고객정보 입력\n2. 고객명으로 정보 조회\n3. 고객 아이디로 정보 조회\n:"))

while num == 1:
    print("고객정보를 입력합니다.")
    id = input("고객아이디:")
    idList.append([id])

    name = input("이름:")
    nameList.append([name])

    address = input("주소:")
    job = input("직업:")
    phone = input("전화번호:")
    print("고객정보가 입력되었습니다.")

    customerList.append([id, name, address, job, phone])
    num = int(input("작업을 선택하세요.\n1. 고객정보 입력\n2. 고객명으로 정보 조회\n3. 고객 아이디로 정보 조회\n:"))

if num == 2:
    search_name = input("조회할 고객명을 입력하세요:")
    for customer in nameList:
        if search_name in customer:
            print(f"{search_name} 고객님의 정보는 다음과 같습니다: \n고객아이디:{id}\n이름:{name}\n주소:{address}\n직업:{job}\n전화번호:{phone}")
        else:
            print(f"{search_name} 고객님의 정보는 존재하지 않습니다.")

    num = int(input("작업을 선택하세요.\n1. 고객정보 입력\n2. 고객명으로 정보 조회\n3. 고객 아이디로 정보 조회\n:"))

if num == 3:
    search_id = input("조회할 고객 아이디를 입력하세요:")
    for customer in idList:
        if search_id in customer:
            print(f"{search_id} 고객님의 정보는 다음과 같습니다:\n고객아이디:{id}\n이름:{name}\n주소:{address}\n직업:{job}\n전화번호:{phone}")
        else:
            print(f"{search_id} 고객님의 정보는 존재하지 않습니다.")

    num = int(input("작업을 선택하세요.\n1. 고객정보 입력\n2. 고객명으로 정보 조회\n3. 고객 아이디로 정보 조회\n:"))

elif num == 0:
    print("프로그램을 종료합니다.")