from budget import*


def print_menu():
    print("My BudgetApp")
    print("1. 지출 추가")
    print("2. 지출 내역 보기")
    print("3. 지출 내역 삭제")
    print("4. 통계")
    print("5. 프로그램 종료")
    

def main():
    while True:
        print_menu()
        choice = input("메뉴를 선택하시오: ")
        
        if choice == '1':
            add_expense    
        elif choice == '2':
            view_expenses
        elif choice == '3':
            delete_expense
        elif choice == '4':
            statistic_ex
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴입니다. 다시 선택하세요. ")
            
if __name__ == "__main__":
    main()