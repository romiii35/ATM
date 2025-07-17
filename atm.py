# 프로젝트 시작
# balance : 초기 잔액을 설정하는 변수를 초기화해주세요.
# 금액은 여러분 마음대로 설정해주세요.

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할수 있도록 
# 사용 기능 입력을 받는 기능을 구현해주세요.(무한정 계속 떠 있게- 사람들이 시도때도 없이 많이온다.)

balance = 1000000

#무한루프?  while vs for
# while문과 for문
# while문은 조건을 달성할때까지(달성지점 필요), for문 횟수에 제한을 두고 시작
# 조건을 True로 준다. 

while True: #True이기에 무조건 실행-무한
    num = input("사용하실 기능의 번호를 선택해주세요 (1. 입금, 2. 출금, 3. 영수증보기, 4. 종료) : ")
        # num은 문자형이다. 그냥 input이라..
    if num == '4':  #4번은 종료 기능

        break # break 만나면 가장 가까운 반복문-바로 서비스 종료4

    if num == '1': #입금 기능 구현 -> feat/deposit 브랜치에서 작업
        deposit_amount = int(input('입금할 금액을 입력해주세요: ')) #str:5000 -> int
        balance += deposit_amount #balance = balance + deposit_amount
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은{balance}원 입니다.')
    if num == '2':
        pass

    if num == '3':
        pass
     
print(f'서비스를 종료합니다.현재 잔액은 {balance}원') # break 전, 입력가능

