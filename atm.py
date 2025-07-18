# 프로젝트 시작
# balance : 초기 잔액을 설정하는 변수를 초기화해주세요.
# 금액은 여러분 마음대로 설정해주세요.

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할수 있도록 
# 사용 기능 입력을 받는 기능을 구현해주세요.(무한정 계속 떠 있게- 사람들이 시도때도 없이 많이온다.)

balance = 1000000
# 초기화 : 사용하기 위해 미리 만드는것, 초기화 특정값을 넣어서 만들거나, 빈 값을 넣어서 만듭니다.(제일 위에 만드는게 좋다, 발란스 뒤에 오는게 좋다. while뒤도 상관없지만, 매번 초기화되기에 불가//...)
receipts = [] #[('입금', balance, deposit_amount),'출금', balance, withdraw_amount ] # 일어나는 순간에 데이터를 넣어야한다..
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
        receipts.append(('입금', deposit_amount, balance))  #보안!!!!!! ->'입금' 입금한 금액(deposit_amount) 보안!!->튜플로 만들기
   
    if num == '2':
        withdraw_amount = int(input('출금할 금액을 입력해주세요:'))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount #balance = balance + withdraw_amount
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
        receipts.append(('출금', withdraw_amount, balance))
    
    if num == '3':
        if receipts:
        # [('입금', 3000, 13000), ('출금', 5000, 8000), ]
            for i in receipts:
            # i = ('입금', 3000, 13000)
            # i[0] => '출금'
                print(f"{i[0]}: {i[1]}원 | 잔액 : {i[2]}")
        else:
            print("영수증 내역이 없습니다.")      
     
print(f'서비스를 종료합니다.현재 잔액은 {balance}원 입니다.') # break 전, 입력가능

# if문 :  문장으로 작성된 규칙